from abstractsearch import Search

class Indeed(Search):
    def __init__(self, location, job_title):
        super().__init__(location, job_title)

    def jobsearch(self):
        pass