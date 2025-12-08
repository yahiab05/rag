from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from app.db.db_connection import collection, reset_collection
from os import environ

api_key = environ.get("OPENAI_API_KEY")

class EmbeddingEngine:
    def __init__(self):
        self.collection = collection
        self.embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        
    def create_embedding(self, docs, reset):
        if reset:
            reset_collection()
        self.vector_search = MongoDBAtlasVectorSearch(
            docs,
            embedding_function=self.embeddings,
            collection=self.collection,
        )   