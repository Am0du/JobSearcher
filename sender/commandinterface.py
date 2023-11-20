from abc import ABC, abstractmethod


class CommandInterface(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def reverse(self):
        pass
