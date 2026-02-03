from ..retriever import Retriever
from langchain_ollama import OllamaEmbeddings
import numpy as np

def test_threshold_filtering():
    retriever = Retriever()
    
    docs = retriever.query_database("invertible matrix")
    
    assert len(docs) > 0 and len(docs) <= 5
    
def test_similarity():
    retriever = Retriever()
    
    query = "invertible matrix"
    
    embedded_query = OllamaEmbeddings(model="qwen2.5:0.5b").embed_query(query)
    
    docs = retriever.query_database(query)
    
    embedding = OllamaEmbeddings(model="qwen2.5:0.5b").embed_documents([d.page_content for d in docs])

    for doc in docs:
        
        similarity = sim_fn(embedded_query, embedding)
        
        assert np.min(similarity) >= 0.3
        
        
def sim_fn(x, y):
    return np.dot(y, x) / (np.linalg.norm(x) * np.linalg.norm(y))
    
    
    
    