import mongomock
from ..embedding_engine import EmbeddingEngine

def test_embedding_in_memory_db(mocker):
    mocker.patch("embedding_engine.MongoClient", new=mongomock.MongoClient)

    engine = EmbeddingEngine()

    docs = ["x", "y"]
    engine.create_embedding(docs, reset=True)

    # Read back
    assert engine.collection.count_documents({}) == 2
