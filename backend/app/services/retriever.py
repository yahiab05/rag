from .vector_search import AtlasVectorSearch
from ..db.db_connection import reset_collection

class Retriever(AtlasVectorSearch):
    def __init__(self):
        super().__init__()
        
    def getRetriever(self):
        retriever = self.vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 5,
                "score_threshold": 0.2,
                },
        )
        
        return retriever
