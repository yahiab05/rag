from .vector_search import AtlasVectorSearch
from ..db.db_connection import reset_collection

class Retriever(AtlasVectorSearch):
    def __init__(self):
        super().__init__()
        
    def query_database(self, query):
        retriever = self.vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 5,
                "score_threshold": 0.3,
                },
        )
        
        result = retriever.invoke(query)
        
        if len(result) == 0:
            raise ValueError("No results found")
        return result
