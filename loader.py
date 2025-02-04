"""A loader class to display while data is being loaded."""

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

class Loader:
    """A loader class that defines the object."""

    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        Initialize loader object with arguments.

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout
        
        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        """Start the loader thread."""
        self._thread.start()
        return self
    

    def _animate(self):
        """Show animation steps until stop is called."""
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)


    def stop(self):
        """Stop the loader thread."""
        self.done = True
        cols = get_terminal_size((180, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)


    def __enter__(self):
        """Start thread execution."""
        self.start()
        

    def __exit__(self, exc_type, exc_value, tb):
        """Stop the thread execution."""
        self.stop()
