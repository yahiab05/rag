from langchain_text_splitters import RecursiveCharacterTextSplitter
import json


class Chunker:
    def __init__(self):
        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800, 
            chunk_overlap=100
            )
    
    def chunk(self, docs):
        return self.recursive_splitter.split_documents(docs)