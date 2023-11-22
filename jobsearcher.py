from searcher.factory.indeedfactory import IndeedFactory
from searcher.factory.jobbermanfactory import JobbermanFactory
from threading import Thread


def job_search(provider, location, job_title):
    return provider.job_search(location, job_title)


class JobSearcher:
    def __init__(self):
        self.__location = None
        self.__job_title = None
        self.__indeed_factory = IndeedFactory()
        self.__jobberman_factory = JobbermanFactory()

    def searcher(self, location, job_title):
        """ Search for jobs across the various job mechanism in place """
        self.__location = location
        self.__job_title = job_title
        indeed_provider = self.__indeed_factory.create()
        jobberman_provider = self.__jobberman_factory.create()

        # indeed_result = Thread(target=job_search, )
