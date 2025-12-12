from ..chuncker import Chunker
from langchain_core.documents import Document

def test_chunker_splits_docs():
    docs = [
        Document(page_content="this is a long document that should be chunked.")
        ]
    chunker = Chunker()

    chunks = chunker.chunk(docs)
    assert isinstance(chunks, list)
    assert len(chunks) > 0  # depending on your logic

def test_chunk_size():
    chunker = Chunker()
    assert chunker.sementic_splitter._chunk_size == 500