from data_ingestors import create_parser
from chuncker import Chunker
from embedding_engine import EmbeddingEngine


def data_ingestion_pipeline(file_path: str, reset: bool):
    parser = create_parser(file_path)
    docs = parser.parse()
    
    chunker = Chunker()
    docs = chunker.chunk(docs)
    
    embedding_engine = EmbeddingEngine()
    embedding_engine.create_embedding(docs, reset)
