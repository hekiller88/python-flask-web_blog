__author__ = 'lhe'

import pymongo

# 这是一个无实例的class
class Database(object):
    # these 2 var will be the same for every Database objects
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        # need to access URI through static class Database
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, query):
        Database.DATABASE[collection].insert(query)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
