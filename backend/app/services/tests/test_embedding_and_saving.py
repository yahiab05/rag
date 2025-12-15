import mongomock
from langchain_core.documents import Document
from backend.app.services.embedding_engine import EmbeddingEngine

def test_embedding_in_memory_db(mocker):
    fake_db = mongomock.MongoClient().db
    fake_collection = fake_db.collection

    mocker.patch(
        "backend.app.services.embedding_engine.collection",
        new=fake_collection
    )

    mocker.patch(
        "backend.app.services.embedding_engine.reset_collection"
    )

    mocker.patch(
        "backend.app.services.embedding_engine.MongoDBAtlasVectorSearch.from_documents",
        return_value=None
    )

    engine = EmbeddingEngine()

    docs = [
        Document(page_content="x"),
        Document(page_content="y")
    ]

    engine.create_and_store(docs, reset=True)

    # Simulate insert (because we mocked from_documents)
    fake_collection.insert_many([
        {"text": "x"},
        {"text": "y"}
    ])

    assert fake_collection.count_documents({}) == 2
