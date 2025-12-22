from ..db.db_connection import reset_collection
from .vector_search import AtlasVectorSearch

class EmbeddingEngine(AtlasVectorSearch):
    def __init__(self):
        super().__init__()
        
    def create_and_store(self, docs, reset):
        if reset:
            reset_collection()

        self.vector_store.add_documents(docs)