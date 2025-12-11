from langchain_community.document_loaders import PyPDFLoader
from . import Parse

class PDFParser(Parse):
    def __init__(self, file_path):
        super().__init__(file_path)
        
    def parse(self):
        self._loader = PyPDFLoader(file_path=self._path)
        self._docs = self._loader.load()
        self._docs = self.clean_docs(self._docs)
        
        return self._docs
        
    def get_clean_docs(self):
        return self._docs