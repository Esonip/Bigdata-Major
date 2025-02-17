from pymongo import MongoClient

class MongoHandler:
    def __init__(self, host = "mongodb://localhost:27017/", db_name = 'crawler_data', collection_name = 'data'):
        self.client = MongoClient(host)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        
    def save_to_mongo(self, data):
        if isinstance(data, list):
            self.collection.insert_many(data)
        else:
            self.collection.insert_one(data)
        print("Saved to MongoDB")