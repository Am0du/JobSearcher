from abc import ABC, abstractmethod

class Search(ABC):


    @abstractmethod
    def search(self, location, job_title):
        pass
