from abstractfactory import Factory
from searcher.search.jobbermansearch import JobberMan


class JobbermanFactory(Factory):

    def create(self):
        return JobberMan()