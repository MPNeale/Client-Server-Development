from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient
        self.client = MongoClient('mongodb://%s:%s@localhost:54099' % (username, password))
        self.database = self.client.AAC
        
# create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary
            print("Creation succesful")
            return bool(True)
        else:
            raise Exception("Nothing to save, data parameter is empty")
            return bool(False)
            
# read method to implement the R in CRUD
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data, {"_id":False})
        else:
            raise Exception("Nothing to find, data parameter is empty")
            
    def readAll(self, data):
        if data is not None:
            return self.database.animals.find(data, {"_id":False})
            
# update method to implement U in CRUD
    def update(self, condition, data):
        if condition is not None and data is not None:
            return self.database.animals.update(condition, data)
        else:
            raise Exception("Nothing to update, condition or data parameter is empty")
            
# delete method to implement D in CRUD
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data)
        else:
            raise Exception("Nothing to delete, data parameter is empty")