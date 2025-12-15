from langchain_ollama import OllamaEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from ..db.db_connection import collection, reset_collection

class EmbeddingEngine:
    def __init__(self):
        self.collection = collection
        self.embeddings = OllamaEmbeddings(model="qwen2.5:0.5b")
        
    def create_and_store(self, docs, reset):
        if reset:
            reset_collection()
        self.vector_search = MongoDBAtlasVectorSearch.from_documents(
            docs,
            self.embeddings,
            collection=self.collection,
        )   