from abc import ABC, abstractmethod

class Factory(ABC):

    @abstractmethod
    def create(self, location, job_title):
        pass
