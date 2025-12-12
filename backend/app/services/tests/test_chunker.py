from ..chuncker import Chunker

def test_chunker_splits_docs():
    docs = ["this is a long document that should be chunked."]
    chunker = Chunker()

    chunks = chunker.chunk(docs)
    assert isinstance(chunks, list)
    assert len(chunks) > 0  # depending on your logic

def test_chunk_size():
    chunker = Chunker()
    assert chunker.sementic_splitter.chunk_size == 500