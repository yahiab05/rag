from langchain_ollama import OllamaEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from ..db.db_connection import collection

class AtlasVectorSearch:
    def __init__(self):
        self.collection = collection
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text")
        self.vector_store = MongoDBAtlasVectorSearch(
            collection=self.collection,
            embedding=self.embeddings,
            index_name="my_index",
            relevance_score_fn="cosine|",
        )