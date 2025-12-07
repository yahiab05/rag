from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from utils.helpers import clean_docs


class PDFParser:
    def __init__(self, file_path):
        self._loader = self.define_parser(file_path)
        self._docs = self._loader.load()
        self._clean_docs = clean_docs(self._docs)
    
    def define_parser(self, file_path):
        return PyPDFLoader(file_path)

        
    def get_clean_docs(self):
        return self._clean_docs