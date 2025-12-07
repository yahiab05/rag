from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import SentenceTransformersTokenTextSplitter

class Chunker:
    def __init__(self):
        self.sementic_splitter = SentenceTransformersTokenTextSplitter(
            sentence_transformer_model_name="all-MiniLM-L6-v2",
            chunk_size=500,
            chunk_overlap=150
        )
        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, 
            chunk_overlap=150
            )
        
    def chunck(self, docs, sementic = True):
        if sementic:
            return self.chunck_sementic(docs)
        else:
            return self.chunck_simple(docs)
        
    def chunk_sementic(self, docs):
        return self.model.split_documents(docs)
    
    def chunk_simple(self, docs):
        return self.recursive_splitter.split_documents(docs)