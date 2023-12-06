from searcher.search.searchinterface import Search
import requests
from bs4 import BeautifulSoup


class Jooble(Search):

    def search(self, location, job_title):
        ''' Searches Jooble with specified location and job title '''

        url = f'https://ng.jooble.org/SearchResult?p=2&rgns={location}%2C%20FCT&ukw={job_title}'

        _response = requests.get(url=url).text
        _soup = BeautifulSoup(_response, 'lxml')

        _job_content = _soup.find_all(name='article', class_='ojoFrF rHG1ci V5WdkE')

        _jobs = []
        for content in _job_content:
            job = {'title': content.find(name='a', class_='jkit_Efecu').get_text(strip=True),
                   'employer': content.find(name='div', class_='E6E0jY').text.split(',')[0][:-len(location)],
                   'salary': 'Not listed',
                   'description': content.find(name='div', class_='PAM72f').text.replace('\r\n',' ')
                   .replace('\xa0...', '').replace('...\xa0', '').replace('â\x80\x93', ''),
                   'location': location,
                   'link': content.find(name='a', class_='jkit_Efecu').get('href')

                   }
            _jobs.append(job)

        return(_jobs)

jb = Jooble()

jb.search('abuja', 'IT support')
