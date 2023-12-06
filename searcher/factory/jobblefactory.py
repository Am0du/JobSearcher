from searcher.factory.jobfactory import Factory
from searcher.search.jobblesearch import Jooble


class JoobleFactory(Factory):
    def create(self):
        return Jooble()


