from searcher.factory.indeedfactory import IndeedFactory


def job_search(provider, location, job_title):
    return provider.job_search(location, job_title)


class JobSearcher:
    def __init__(self, location, job_title):
        self.__location = location
        self.__job_title = job_title
        self.__indeed = IndeedFactory()

    def search(self):

        job_search(self.__indeed.create(), location=self.__location, job_title=self.__job_title)

