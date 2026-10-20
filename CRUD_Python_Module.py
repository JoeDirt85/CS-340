# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        #  
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        try:
            if data is not None: 
                self.database.animals.insert_one(data)  # data should be dictionary 
                return True
            else: 
                raise Exception("Nothing to save, because data parameter is empty") 
        except Exception as e:
            return False
            
    # Create method to implement the R in CRUD.
    def read(self, data):
        try:
            result = list(self.database.animals.find(data))
            return result
        except Exception as e:
            return list()
        
        # Create method to implement the U in CRUD. 
    def update(self, data, new_data, many=False): 
        try:
            update_values = {"$set" : new_data}
            if many is False:
                result = self.database.animals.update_one(data, update_values)
                return result.modified_count
            else:
                result = self.database.animals.update_many(data, update_values)
                return result.modified_count
        except Exception as e:
            return 0
            
        # Create method to implement the D in CRUD
    def delete(self, data, many=False):
        try:
            if many is False:
                result = self.database.animals.delete_one(data)
                return result.deleted_count
            else:
                result = self.database.animals.delete_many(data)
                return result.deleted_count
        except Exception as e:
            return 0
            