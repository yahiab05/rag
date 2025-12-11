from langchain_text_splitters import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
from langchain_community.document_transformers.openai_functions import create_metadata_tagger
from langchain_openai import ChatOpenAI
from os import environ

api_key = environ.get("OPENAI_API_KEY")

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
        self.llm = ChatOpenAI(openai_api_key=api_key, 
                                temperature=0,
                                model_name="gpt-3.5-turbo",
                            )
        self.transformer, self.schema = self.create_schema_and_transformers()
        
        
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
        return self.transformer.transform_documents(docs)
    
    def create_schema_and_transformers(self): 
        schema = {
            "properties":{
                "title": {"type": "string"},
                "keywords": {"type": "array", "items": {"type": "string"}},
                "description": {"type": "string"},
            },
            "required": ["title", "keywords", "description"]
        }
        
        transformer = create_metadata_tagger(metadata_schema=schema, llm=self.llm)
        
        return transformer, schema