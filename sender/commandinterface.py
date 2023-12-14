from abc import ABC, abstractmethod
from sender.emailer import Emailer
from sender.model import Model

class CommandInterface(ABC):
    def __init__(self):
        self.emailer = Emailer()
        self.model = Model()

    @abstractmethod
    def execute(self, uid: str) -> str:
        pass

    @abstractmethod
    def status(self, uid: str):
        pass

    # @abstractmethod
    # def reverse(self, uid: str) -> str:
    #     pass

    @abstractmethod
    def insert(self, args):
        pass

