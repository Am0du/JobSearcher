from abstractfactory import Factory
from recommend.search.jobbermansearch import Jobberman


class Jobbermanfactory(Factory):

    def create(self, location, job_title):
        return Jobberman(location, job_title)