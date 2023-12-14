from flask import Flask, jsonify, request
import os
from jobsearcher import JobSearcher
from sender.command import Command


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('s_key')


@app.route('/api/search', methods=['GET'])
def search():
    data = request.get_json()
    job_title = data.get('job_title')
    job_location = data.get('location')
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
        return jsonify(result), 400

@app.route('/api/send-mail', methods=['POST'])
def send_mail():
    data = request.get_json()
    job_content = data.get('result')
    if job_content:
        uid = cd.insert(job_content)
        result = {
            'status': 'success',
            'code': 201,
            'message': 'Request successful, sending in progress',
            'id': uid
        }
        return result
    else:
        result = {
            'status': 'unsuccessful',
            'code': 400,
            'message': 'Request unsuccessful, request payload does not contain <result>'
        }
        return result

@app.route('/api/check-status', methods=['GET'])
def check_status():
    data = request.get_json()
    uid = data.get('id')

    if uid:
        if cd.status(uid):
            result = {
                'status': 'success',
                'code': 200,
                'message': 'Request successful, email has been sent',
            }
            return result
        else:
            result = {
                'status': 'success',
                'code': 200,
                'message': 'Request successful, but email has not been sent',

            }
            return result
    else:
        result = {
            'status': 'unsuccessful',
            'code': 400,
            'message': 'Request unsuccessful, request payload does not contain <id>'
        }
        return result


if __name__ == '__main__':
    jb = JobSearcher()
    cd = Command()
    app.run(debug=True)