# Census Data Import Tool using WatchDog library
# Erin Silver 12-2-25

import pandas as pd
from abbrevs import us_state_to_abbrev
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent
from typing import Union

RENT_PATH = "./rent_tracts/"
LOOKUP_PATH = "./tracts_states/"

def read_census_tract(path):
    with open(path, "r") as f:
        # We want the label, without quotes, in chunks.
        header = f.readline().replace("'", "").replace('"', "").split(",")
        header[3] = header[3].replace("!!Estimate", "")
        for i in range(len(header)):
            header[i] = header[i].strip()
        # Alter formattings
        try:
            # Transform tract number into 6-digit tract code per census specifications.
            tract_float = int(float(header[1].replace("Census Tract ", "")) * 100)
            tract_string = str(tract_float)
            while len(tract_string) < 6:
                tract_string = '0' + tract_string
        except ValueError:
            print(f"Malformed census tract code in {path}, please manually check...")
            return False

        # Store attributes
        entry = [us_state_to_abbrev[header[3]],
                 header[1],
                 header[3],
                 header[2]]

        for line in f.readlines():
            entry_line = line.strip().split('","')
            entry.extend([entry_line[1].replace(',', ""),
                          entry_line[2].replace('"', "").replace("±", '')])

    return entry

class CensusTractHandler(FileSystemEventHandler):
    """Custom handler for Watchdog"""

    def __init__(self):
        # List to store path
        try:
            self.census_tract_df = pd.read_csv("census_tracts.csv")
        except FileNotFoundError:
            self.census_tract_df = pd.DataFrame()
        self.most_recent_state = ""
        self.most_recent_lookup = pd.DataFrame()


    # callback for File/Directory created event, called by Observer.
    def on_created(self, event: Union[DirCreatedEvent, FileCreatedEvent]):
        # check if it's File creation, not Directory creation
        if isinstance(event, FileCreatedEvent):
            # if so, do something with event.src_path - it's path of the created file.
            new_state = "nc"
            # don't reload the lookup table if it's already loaded.
            if new_state != self.most_recent_state:
                try:
                    self.most_recent_lookup = pd.read_csv(LOOKUP_PATH + new_state + ".csv")
                    self.most_recent_state = new_state
                except FileNotFoundError:
                    print(f"State lookup table for {new_state} not found. Skipping...")
                    self.most_recent_lookup = False
                    self.most_recent_state = ""

            new_census_tract = read_census_tract(event.src_path)
            if self.most_recent_lookup:
                try:
                    lookup_tract = self.most_recent_lookup[self.most_recent_lookup["TRACTCE"] == new_census_tract[1]]
                except KeyError:
                    print(f"Malformed census tract code in {event.src_path}, please manually check...")
                    new_census_tract = False
                else:
                    new_census_tract.append(lookup_tract["LATITUDE"])
                    new_census_tract.append(lookup_tract["LONGITUDE"])

            if new_census_tract:
                self.census_tract_df.loc[len(self.census_tract_df)] = new_census_tract

def main():
    event_handler = CensusTractHandler()
    observer = Observer()

    observer.schedule(event_handler, RENT_PATH, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == '__main__':
    read_census_tract("./rent_tracts/ACSDT5Y2019.B25056-2025-02-12T204241.csv")