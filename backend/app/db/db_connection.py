from pymongo import MongoClient
from pymongo.server_api import ServerApi
from os import environ

password = environ.get("DB_PASSWORD")
username = environ.get("DB_USERNAME")
appName = environ.get("APP_NAME")

_uri = f"mongodb+srv://{username}:{password}@{appName}.lbpiqmb.mongodb.net/?appName={appName}"
_client = MongoClient(_uri, server_api=ServerApi('1'))
_db = _client["my_db"]

collection = _db["my_collection"]

def reset_collection():
    collection.delete_many({})