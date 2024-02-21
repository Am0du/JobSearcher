from fastapi import FastAPI
from searcher.jobsearcher import JobSearcher
from sender.command import Command
from concurrent.futures import ThreadPoolExecutor
import uvicorn
from request import Item, Mail, Status

jb = JobSearcher()
cd = Command()

app = FastAPI()


@app.get('/api/search')
def search(item: Item):
    job_title = item.job_title
    job_location = item.location
    if job_title or job_location:
        result = {
            'status': 'success',
            'code': 200,
            'message': 'Request successful',
            'result': jb.searcher(location=job_location, job_title=job_title)
        }
        return result, 200
    else:
        result = {
            'status': 'unsuccessful',
            'code': 400,
            'message': 'Request successful, request payload does not contain the <job_title> or <location>',
        }
        return result, 400


@app.post('/api/send-mail', )
def send_mail(mail: Mail):
    search_result = mail.search_result
    email_add = mail.email_address
    search_title = mail.search_title
    if search_result and email_add and search_title:
        db_data = {
            'email': email_add,
            'search_title': search_title,
            'job_content': search_result,
            'status': False
        }
        uid = cd.insert(db_data)
        print(uid)


        result = {
            'status': 'success',
            'code': 201,
            'message': 'Request successful, sending in progress',
            'id': uid
        }
        return result, 201
    else:
        result = {
            'status': 'unsuccessful',
            'code': 400,
            'message': 'Request unsuccessful, request payload does not contain <result>'
        }
        return result, 400


@app.get('/api/check-status')
def check_status(status: Status):
    uid = status.id

    if uid:
        if cd.status(uid):
            result = {
                'status': 'success',
                'code': 200,
                'message': 'Request successful, email has been sent',
            }
            return result, 200
        else:
            result = {
                'status': 'success',
                'code': 102,
                'message': 'Request successful, but email has not been sent',

            }
            return result, 102
    else:
        result = {
            'status': 'unsuccessful',
            'code': 400,
            'message': 'Request unsuccessful, request payload does not contain <id>'
        }
        return result, 400



