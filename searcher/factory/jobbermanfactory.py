from abstractfactory import Factory
from searcher.search.jobbermansearch import JobberMan


class Jobbermanfactory(Factory):

    def create(self,):
        return JobberMan()