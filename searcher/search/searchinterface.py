from abc import ABC, abstractmethod

class Search(ABC):


    @abstractmethod
    def job_search(self, location, job_title):
        pass
