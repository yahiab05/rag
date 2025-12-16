from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

password = "rtkMqFbfPUwIclvL"
username = "yahiaboukharrata092_db_user"
appName = "rag"

_uri = f"mongodb+srv://{username}:{password}@{appName}.lbpiqmb.mongodb.net/?retryWrites=true&w=majority"
_client = MongoClient(_uri, 
                    server_api=ServerApi('1'), 
                    tls=True,
                    serverSelectionTimeoutMS=3000,  # 3 seconds
                    connectTimeoutMS=3000,
                    socketTimeoutMS=3000
                    )
try:
    _client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)