import json
import unittest

from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

from mongo.mongoService import MongoClientService


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.userName = "mongodbuser"
        self.dbName = "testDB"
        self.hostName = "localhost"
        self.port = 27017
        self.collectionName = "comments"
        self.password = "mongoPassword"
        self.mongo = MongoClientService(db_name=self.dbName, collection_name=self.collectionName,
                                        host=self.hostName,
                                        port=self.port,
                                        username=self.userName,
                                        password=self.password
                                        )

        self.raw_client = MongoClient(
            host=self.hostName,
            port=self.port,
            username=self.userName,
            password=self.password
        )
        self.raw_client["testDB"]["comments"].drop()
        with open('mongoSeed.json') as data:
            data_dct = json.load(data)

        result = self.raw_client["testDB"]["comments"].insert_one(data_dct)
        logging.debug(('Inserted post id %s ' % result.inserted_id)

    def testConnection(self):
        try:

            client = MongoClient(
                host=self.hostName,
                port=self.port
            )
            client.server_info()
            self.assertEqual(True, True)
        except ConnectionFailure:
            self.assertEqual(False, True)

    def testAuthentication(self):
        self.raw_client.server_info()
        self.assertRaises(ConnectionFailure)

    def testAuthentication(self):

        client = MongoClient(
            host=self.hostName,
            port=self.port,
            username=self.userName,
            password=self.password
        )
        client.server_info()

    def testAuthenticationWithWrongCreds(self):

        with   self.assertRaises(OperationFailure):
            client = MongoClient(
                host=self.hostName,
                port=self.port,
                username="wrong",
                password=self.password
            )
            client.server_info()

    def test_read(self):
        comments_list = []
        all = self.mongo.readAll()  # read all comments form db
        for comment in all:
            logging.debug((comment)
            comments_list.append(comment)
        self.assertEqual(comments_list.__sizeof__() > 0, True)

    def test_create(self):
        self.mongo.create("patryk", "test", ["typical comment", "lol nice!"])  # read all comments form db
        record = self.mongo.readOneByAuthor("patryk")  # read all comments form db

        self.assertEqual(record["author_name"],
                        "patryk")

    def canReadNotExistingRecord(self):
        self.mongo.create("patryk", "test", ["typical comment", "lol nice!"])  # read all comments form db
        self.mongo.create("patryk", "test", ["typical comment", "lol nice!"])  # read all comments form db
        record = self.mongo.readOneByAuthor("patryk")  # read all comments form db

        self.assertEqual(record["commentSet"],
                         {'_id': ObjectId('60bffb9aebe111b51da485ea'),
                          'author_name': 'patryk',
                          'commentsSet': ['typical comment', 'lol nice!'],
                          'description': 'test'})
