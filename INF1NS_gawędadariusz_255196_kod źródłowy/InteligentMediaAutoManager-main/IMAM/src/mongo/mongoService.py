import logging
import sys
import sys
from pymongo import MongoClient


class MongoClientService:
    def __init__(self, db_name, collection_name, host, port, username, password):
        try:
            client = MongoClient(host=host,
                                 port=int(port),
                                 username=username,
                                 password=password
                                 )
            self.db = client[db_name][collection_name]
        except:
            logging.debug("Server had problem while trying connecting  with mongodb.")
            logging.debug("Oops!", sys.exc_info()[0], "occurred.")

    def create(self, userName, description, commentsSet):
        self.db.insert_one({'author_name': userName, 'description': description, 'commentsSet': commentsSet})

    def readOneById(self, id):
        return self.db.find_one({'_id': id})

    def readOneByAuthor(self, author):
        return self.db.find_one({'author_name': author})

    def readAll(self):
        return self.db.find()

    def updateComment(self, id, comment):
        self.db.updateOne({'id': id}, {'$set': {'comment': comment}})

    def updateDesc(self, id, describe):
        self.db.updateOne({'id': id}, {'$set': {'describe': describe}})

    def updateAuthor(self, id, userName):
        self.db.updateOne({'id': id}, {'$set': {'authorName': userName}})
