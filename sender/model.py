from pymongo import MongoClient
from bson import ObjectId
import os

class Model:
    def __new__(cls, *args, **kwargs):

        if not hasattr(Model, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)
            cls.instance._client = MongoClient(os.environ.get('mongo_db'))

        return cls.instance

    def __init__(self):
        self._user = self.instance._client.jobsearcher.user

    def insert(self, *args) -> str:
        """Adds data into the database"""
        if args is None:
            raise TypeError('Argument "args" cannnot be None')
        for arg in args:
            self._user.insert_one(arg)
            data = self._user.find_one({'email': arg['email']})
            return data['_id']

    def find(self, uid: str) -> dict:
        """Searches for data that _id is <uid> in the collection"""

        data = self._user.find_one({'_id': ObjectId(uid)})
        if data is None:
            raise ValueError(f'{uid} does not exist')
        return data

    def update(self, uid: str, new_value: dict) -> bool:
        """update the _id that matches <uid> with the new entry <new_value>"""

        result = self._user.update_one({'_id': ObjectId(uid)}, {'$set': new_value})
        if result.matched_count == 0:
            return False
        else:
            return True


