import requests
from bs4 import BeautifulSoup
from searcher.search.searchinterface import Search


OPTIONS = {
    'accounting': 'accounting-auditing-finance',
    'admin': 'admin-office',
    'building': 'building-architecture',
    'community': 'community-social-services',
    'consulting': 'consulting-strategy',
    'creative': 'creative-design',
    'customer': 'customer-service-support',
    'driver': 'driver-transport-services',
    'engineering': 'engineering-technology',
    'estate': 'estate-agents-property-management',
    'farming': 'farming-agriculture',
    'food': 'food-services-catering',
    'health': 'health-safety',
    'hospitality': 'hospitality-leisure',
    'hr': 'human-resources',
    'legal': 'legal-services',
    'management': 'management-business-development',
    'marketing': 'marketing-communications',
    'medical': 'medical-pharmaceutical',
    'product': 'product-project-management',
    'quality': 'quality-control-assurance',
    'research,': 'research,-teaching-training',
    'sales': 'sales',
    'tech': 'software-data',
    'supply': 'supply-chain-procurement',
    'trades': 'trades-services'
}

KEYS = ['accounting', 'admin', 'building', 'community', 'consulting', 'creative', 'customer', 'driver', 'engineering',
        'estate', 'farming', 'food', 'health', 'hospitality', 'human', 'legal', 'management', 'marketing', 'medical',
        'product', 'quality', 'research,', 'sales', 'tech', 'supply', 'trades', 'it', 'pharmacy']


def title_selector(job_title):
    ''' Ensure the job_title is passed in the right format '''
    job_title = job_title.lower().split()

    for key in KEYS:
        if job_title[0] == key:
            return OPTIONS[key]


class JobberMan(Search):

    def search(self, location, job_title):
        """Seacrhes jobberman with specified location and job title"""
        jb = title_selector(job_title)
        if jb is None:
            _response = requests.get(url=f'https://www.jobberman.com/jobs/{location}').text
        else:
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



