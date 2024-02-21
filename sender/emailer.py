import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from sender.model import Model
import os
import uuid


class Emailer:
    def __init__(self):
        self._email_add = os.environ.get('email_address')
        self._email_pass = os.environ.get('email_password')
        self._message = MIMEMultipart()
        self._model = Model()
        self._unique = str(uuid.uuid4())

    def make_csv(self, uid: str):
        """from the Job content in the db, a csv file is created for emailing"""
        data = self._model.find(uid=uid)
        email_add = data['email']
        job_content = data['job_content']
        job_title = data['job_search']
        df = pd.DataFrame(job_content)
        df.to_csv(f'../sender/Temp_file/{job_title + self._unique}.csv', index=False)
        self.send_mail(email_add, job_title, uid)

    def send_mail(self, email_add: str, job_title: str, uid: str):
        """"Structures the parameters for emailing """
        # Email message
        print('fdggdf')
        body = 'Your Jobsearch csv is ready'
        self._message['From'] = self._email_add
        self._message['To'] = email_add
        self._message['Subject'] = f'JobSearcher: Your search {job_title} csv file'

        self._message.attach(MIMEText(body, 'plain'))

        filename = f'../sender/Temp_file/{job_title + self._unique}.csv'

        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={job_title}.csv')
        self._message.attach(part)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=self._email_add, password=self._email_pass)
            connection.sendmail(from_addr=self._email_add, to_addrs=email_add, msg=self._message.as_string())

        self.update_status(uid, {'status': 'True'})


    def update_status(self, uid: str, value: dict) -> bool:
        """Updates the status in the db after emailing """
        self._model.update(uid, value)
        return True
