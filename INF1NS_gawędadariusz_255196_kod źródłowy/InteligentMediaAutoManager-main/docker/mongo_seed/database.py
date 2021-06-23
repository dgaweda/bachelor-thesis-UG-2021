from pymongo import MongoClient

from pymongo import MongoClient
import json

mongo = MongoClient(host="localhost",
                                 port=27017,
                                 username="mongodbuser",
                                 password="mongoPassword"
                                 )["db"]["comments"]

def main():
    with open('mongoSeed.json') as data:
        data_dct = json.load(data)

    result = mongo.insert_one(data_dct)
    print('Inserted post id %s ' % result.inserted_id)

if __name__ == "__main__":
    main()

  #  db.auth("mongodbuser","mongoPassword")