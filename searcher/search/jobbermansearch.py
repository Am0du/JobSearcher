import requests
from bs4 import BeautifulSoup

from searchinterface import Search


class JobberMan(Search):

    def search(self, location, job_title):
        _response = requests.get(url=f'https://www.jobberman.com/jobs/{job_title}/{location}').text

        _soup = BeautifulSoup(_response, 'lxml')

        # To get Job titles
        _job_titles = _soup.find_all(name='p', class_='text-lg')
        _job_titles = [job_title.get_text(strip=True) for job_title in _job_titles]

        # To get job employer
        _job_employer = _soup.find_all(name='a', class_='text-loading-animate-link')
        _job_employer = [job_employer.get_text(strip=True) for job_employer in _job_employer]

        # Salary
        _job_salary = _soup.find_all(name='span', class_='mr-1')
        _job_salary = [job_salary.get_text(strip=True) for job_salary in _job_salary]


        # Job Summary
        _job_summaries = _soup.find_all(name='p', class_='md:pl-5')
        _job_summaries = [job_summary.get_text(strip=True) for job_summary in _job_summaries]

        # Job Link
        _job_links = _soup.find_all(name='p', class_='text-link-500')
        _job_links = [job_link.find('a') for job_link in _job_links]
        _job_link = [f"https://www.jobberman.com{link.get('href')}" for link in _job_links if link is not None]


        jobs = []
        for i in range(len(_job_employer)):
            job = {'title': _job_titles[i],
                   'employer': _job_employer[i],
                   'salary': _job_salary[i],
                   'description': _job_summaries[i],
                   'location': location,
                   'link': _job_link
                   }
            jobs.append(job)

        return jobs


