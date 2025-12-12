class Parse:
    def __init__(self, path):
        self._path = path
        self._docs = []
        
    def parse(self):
        raise NotImplementedError
    
    def clean_docs(self, docs):
        clean_docs = [d for d in docs if len(d.page_content.split()) > 50]
        return clean_docs