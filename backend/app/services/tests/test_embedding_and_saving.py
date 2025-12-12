import mongomock
from ..embedding_engine import EmbeddingEngine

def test_embedding_in_memory_db(mocker):
    mocker.patch("backend.app.db.db_connection._client", new=mongomock.MongoClient)

    engine = EmbeddingEngine()

    docs = ["x", "y"]
    engine.create_embedding(docs, reset=True)

    # Read back
    assert engine.collection.count_documents({}) == 2
