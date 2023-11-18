from abstractfactory import Factory
from recommend.search.indeedsearch import Indeed

class Indeedfactory(Factory):

    def create(self, location, job_title):
        return Indeed(location, job_title)