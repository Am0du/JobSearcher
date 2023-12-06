from searcher.factory.jobblefactory import JoobleFactory
from searcher.factory.jobbermanfactory import JobbermanFactory
from concurrent.futures import ThreadPoolExecutor


def job_search(provider, location, job_title):
    return provider.search(location, job_title)


class JobSearcher:
    def __init__(self):
        self.__location = None
        self.__job_title = None
        self.__jooble_factory = JoobleFactory()
        self.__jobberman_factory = JobbermanFactory()

    def searcher(self, location, job_title):
        """ Search for jobs across the various job mechanism in place """
        self.__location = location
        self.__job_title = job_title
        jobble_provider = self.__jooble_factory.create()
        jobberman_provider = self.__jobberman_factory.create()

        with ThreadPoolExecutor(max_workers=2) as executor:
            # Submit jobs and retrieve future objects
            jobberman_result = executor.submit(job_search, jobberman_provider, self.__location, self.__job_title)
            jobble_result = executor.submit(job_search, jobble_provider,  self.__location, self.__job_title)

            # Wait for both threads to complete and get results
            results = [jobberman_result, jobble_result]


            # Retrieve and print results
            job_list = [content.result() for content in results]
            job_list = job_list[0] + job_list[1]

        return job_list


jb = JobSearcher()
jb.searcher('abuja', 'software-data')
