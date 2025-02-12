# Census Data Import Tool using WatchDog library
# Erin Silver 12-2-25

import pandas as pd
from dict_lib import us_state_to_abbrev, cols_labels
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent
from typing import Union

RENT_PATH = "./rent_tracts/"
LOOKUP_PATH = "./tracts_states/"

def read_census_tract(path):
    with open(path, "r") as f:
        # We want the label, without quotes, in chunks. Some files use ; for ,.
        header = f.readline().replace("'", "").replace('"', "").replace(";", ",").split(",")
        header[3] = header[3].replace("!!Estimate", "")
        for i in range(len(header)):
            header[i] = header[i].strip()
        # Alter formattings
        try:
            # Transform tract number into 6-digit tract code per census specifications.
            tract = int(float(header[1].replace("Census Tract ", "")) * 100)
        except ValueError:
            print(f"Malformed census tract code in {path}, please manually check...")
            return False

        # Store attributes
        entry = [us_state_to_abbrev[header[3]],
                 tract,
                 header[3],
                 header[2]]

        f.readline()

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
            self.census_tract_df = pd.DataFrame(columns = cols_labels)
        self.most_recent_state = ""
        self.most_recent_lookup = pd.DataFrame()
        self.processed_files = []

    def add_entry(self, entry):
        # Remove state code.
        entry.pop(0)
        # Ensure there's a TRACTCE to match.
        try:
            lookup_tract = self.most_recent_lookup[self.most_recent_lookup["TRACTCE"] == entry[0]]
        except KeyError:
            print(f"Malformed census tract code in {event.src_path}, please manually check...")
            entry = False
        else:
            # Get lat/lon from the matching.
            entry.insert(3, lookup_tract["LATITUDE"].values[0])
            entry.insert(4, lookup_tract["LONGITUDE"].values[0])

        if entry:
            self.census_tract_df.loc[len(self.census_tract_df)] = entry

    # callback for File/Directory created event, called by Observer.
    def on_created(self, event: Union[DirCreatedEvent, FileCreatedEvent]):
        # check if it's File creation, not Directory creation
        if isinstance(event, FileCreatedEvent):
            if event.src_path not in self.processed_files:
                new_census_tract = read_census_tract(event.src_path)

                # extract state code to determine lookup table.
                new_state = new_census_tract[0].lower()
                # don't reload the lookup table if it's already loaded.
                if new_state != self.most_recent_state:
                    try:
                        self.most_recent_lookup = pd.read_csv(LOOKUP_PATH + new_state + ".csv")
                        self.most_recent_state = new_state
                    except FileNotFoundError:
                        print(f"State lookup table for {new_state} not found. Skipping...")
                        self.most_recent_lookup = False
                        self.most_recent_state = ""

                if isinstance(self.most_recent_lookup, pd.DataFrame):
                    if new_census_tract:
                        self.add_entry(new_census_tract)
                        self.processed_files.append(event.src_path)


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
        # Save data frame to csv.
        event_handler.census_tract_df.drop_duplicates().to_csv("census_tracts.csv", index=False)


if __name__ == '__main__':
    main()