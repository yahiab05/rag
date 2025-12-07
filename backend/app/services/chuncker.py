from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import SentenceTransformersTokenTextSplitter
from .data_ingestors.html_parser import HtmlParser
from .data_ingestors.pdf_parser import PDFParser

class Chunker:
    def __init__(self):
        self.sementic_splitter = SentenceTransformersTokenTextSplitter(
            chunk_size=500,
            chunk_overlap=150
        )
        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, 
            chunk_overlap=150
            )
        
    def chunck(self, docs, sementic = True):
        if sementic:
            return self.chunk_sementic(docs)
        else:
            return self.chunk_simple(docs)
        
    def chunk_sementic(self, docs):
        return self.sementic_splitter.split_documents(docs)
    
    def chunk_simple(self, docs):
        return self.recursive_splitter.split_documents(docs)