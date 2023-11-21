from searcher.factory.indeedfactory import IndeedFactory
from searcher.factory.jobbermanfactory import JobbermanFactory
from threading import Thread


def job_search(provider, location, job_title):
    return provider.job_search(location, job_title)


class JobSearcher:
    def __init__(self, location, job_title):
        self.__location = location
        self.__job_title = job_title
        self.__indeed_factory = IndeedFactory()
        self.__jobberman_factory = JobbermanFactory()

    def searcher(self):
        """ Search for jobs across the various job mechanism in place """
        indeed_provider = self.__indeed_factory.create()
        jobberman_provider = self.__jobberman_factory.create()

        indeed_result = Thread(target=job_search, )
