
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

    _db = _client["my_db"]

    collection = _db["my_collection"]
    
    collection.insert_one({"init": True})
    
    return collection, collection_exists(collection, _db)

def collection_exists(collection, db):
    
    return collection.name in db.list_collection_names() 