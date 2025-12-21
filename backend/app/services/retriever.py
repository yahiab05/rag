from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_ollama import OllamaEmbeddings
from os import environ

class Retriever:
    def __init__(self):
        _uri = environ["uri"]
        _dbName = environ["dbName"]
        _collectionName = environ["collectionName"]
        
        self.vectoreStore = MongoDBAtlasVectorSearch.from_connection_string(
            _uri, _dbName + "." + _collectionName,
            OllamaEmbeddings(model="qwen2.5:0.5b"),
            index = "my_index" 
        )
        
    def query_database(self, query):
        result =  self.vectoreStore.similarity_search(
            search_type="similarity",
            search_kwargs={
                "k": 5,
                "score_threshold": 0.01
            },
        )
        
        return result
        