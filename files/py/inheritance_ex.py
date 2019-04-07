from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# base class
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("file is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("file is already closed")
        self.opened = False

    @abstractmethod
    def read(self):     # abstracts this method so every driven class should have it defined
        pass


class FileStream(Stream):
    def read(self):
        print("reading file...")


class NetworkStream(Stream):
    def read(self):
        print("reading from network...")


stream = NetworkStream()
stream.open()
# stream.open()         # raises error
stream.read()
stream.close()
