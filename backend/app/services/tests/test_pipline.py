import mongomock
from ..data_ingestion_pipeline import data_ingestion_pipeline

def test_full_pipeline_with_mongomock(mocker):
    # --- 1. Mock Parser ---
    mock_parser = mocker.Mock()
    mock_parser.parse.return_value = ["doc1", "doc2"]
    mocker.patch("pipeline.create_parser", return_value=mock_parser)

    # --- 2. Mock Chunker ---
    mock_chunker = mocker.Mock()
    mock_chunker.chunk.return_value = ["chunk1", "chunk2"]
    mocker.patch("pipeline.Chunker", return_value=mock_chunker)

    # --- 3. Patch MongoDB with mongomock ---
    mocker.patch("pipeline.MongoClient", new=mongomock.MongoClient)

    # --- 4. Mock the embedding function (optional but recommended) ---
    def fake_embedding(d):
        return [0.1, 0.2]  # fake vector
    
    mocker.patch(
        "embedding_engine.EmbeddingEngine.generate_embedding",
        side_effect=fake_embedding
    )

    # --- 5. Run the pipeline ---
    data_ingestion_pipeline("dummy.pdf", reset=True)

    # --- 6. Validate DB content ---
    # Create a fresh instance of the engine to inspect DB contents
    from embedding_engine import EmbeddingEngine
    engine = EmbeddingEngine()

    stored = list(engine.collection.find({}))

    assert len(stored) == 2
    assert stored[0]["text"] == "chunk1"
    assert stored[1]["text"] == "chunk2"
