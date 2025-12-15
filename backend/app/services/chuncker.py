from langchain_text_splitters import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
from langchain_ollama import ChatOllama
import json


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
        self.llm = ChatOllama(
            model="mistral",
            temperature=0
        )
        
        
    def chunk(self, docs, sementic = True):
        tagged_docs = self.add_metadata(docs)
        if sementic:
            return self.chunk_sementic(tagged_docs)
        else:
            return self.chunk_simple(tagged_docs)
        
    def chunk_sementic(self, docs):
        return self.sementic_splitter.split_documents(docs)
    
    def chunk_simple(self, docs):
        return self.recursive_splitter.split_documents(docs)
    
    def add_metadata(self, docs):
        batch = [d.page_content for d in docs]
        metadata_list = self._extract_metadata_batch(batch)
        for doc, meta in zip(docs, metadata_list):
            doc.metadata = meta
        return docs

    def _extract_metadata_batch(self, texts):
        prompt = f"""
        You MUST return a JSON array.
        Each element MUST be an object with:
        - title (string)
        - keywords (array of strings)
        - description (string)

        Return ONLY a JSON array.

        Texts:
        {json.dumps(texts)}
        """


        response = self.llm.invoke(prompt).content
        print(type(response))
        printer = True
        if printer:
            print(response)
            printer = False
        return json.loads(response)