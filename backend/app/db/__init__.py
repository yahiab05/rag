from os import environ

password = "rtkMqFbfPUwIclvL"
username = "yahiaboukharrata092_db_user"
appName = "rag"
def connect():
    from pymongo import MongoClient
    from pymongo.server_api import ServerApi

    _uri = f"mongodb+srv://{username}:{password}@{appName}.lbpiqmb.mongodb.net/?retryWrites=true&w=majority"
    _client = MongoClient(_uri, 
                        server_api=ServerApi('1'), 
                        tls=True,
                        serverSelectionTimeoutMS=3000,  # 3 seconds
                        connectTimeoutMS=3000,
                        socketTimeoutMS=3000
                        )

    _dbName = "my_db"
    _collectionName = "my_collection"
    
    setEnvVariables(_uri, _dbName, _collectionName)
    
    _db = _client[_dbName]

    collection = _db[_collectionName]
    
    collection.insert_one({"init": True})
    
    return collection, collection_exists(collection, _db)

def collection_exists(collection, db):
    
    return collection.name in db.list_collection_names() 

def setEnvVariables(uri, dbName, collectionName):
    environ["uri"] = uri
    environ["dbName"] = dbName
    environ["collectionName"] = collectionName
    