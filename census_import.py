# Census Data Import Tool using WatchDog library
# Erin Silver 12-2-25

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent
from typing import Union

PATH = "./rent_tracts/"


class CustomHandler(FileSystemEventHandler):
    """Custom handler for Watchdog"""

    def __init__(self):
        # List to store path
        self.path_strings = []

    # callback for File/Directory created event, called by Observer.
    def on_created(self, event: Union[DirCreatedEvent, FileCreatedEvent]):
        print(f"Event type: {event.event_type}\nAt: {event.src_path}")

        # check if it's File creation, not Directory creation
        if isinstance(event, FileCreatedEvent):
            # if so, do something with event.src_path - it's path of the created file.
            self.path_strings.append(event.src_path)

            print(f"Path content: \n{self.path_strings}")

def main():
    event_handler = CustomHandler()
    observer = Observer()

    observer.schedule(event_handler, PATH, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == '__main__':
    main()