from abc import ABC, abstractmethod

class Search(ABC):
    def __init__(self, location, job_title):
        self._location = location
        self._job_title = job_title


    @abstractmethod
    def jobsearch(self):
        ...
