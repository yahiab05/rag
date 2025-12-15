from ..chuncker import Chunker
from langchain_core.documents import Document

docs = [
    Document(page_content="In a quiet city that never truly slept, people moved through their routines with a mix of intention and habit, rarely stopping to notice how many small decisions shaped their days. Conversations floated through cafés, offices, and buses, blending plans for the future with reflections on the past, while screens glowed softly in hands and pockets. Somewhere between work deadlines and personal dreams, moments of curiosity appeared, brief but meaningful, pushing individuals to learn, create, or question what they already knew. Technology accelerated these moments, connecting distant ideas and people in seconds, yet it also reminded everyone of the importance of slowing down and thinking clearly. Progress did not arrive all at once; it emerged from repeated effort, quiet persistence, and the willingness to improve something just a little each time. In that steady rhythm, growth became less about sudden breakthroughs and more about consistency, patience, and understanding the value of each step forward.")
    ]

chunker = Chunker()

def test_chunker_splits_docs():
    chunks = chunker.chunk(docs)
    assert isinstance(chunks, list), show_result(f"Expected type: list, Result: {type(chunks)}")
    assert len(chunks) > 0 and len(chunks) < 3, show_result(f"Expected Range: (1, 2), Result: {len(chunks)}")

def test_chunk_size():
    chunks = chunker.chunk(docs)
    assert len(chunks[0].page_content) > 0 and len(chunks[0].page_content) < 800, show_result(f"Expected Range: (1, 800), Result: {len(chunks[0].page_content)}")
    
def test_chunk_type():
    chunks = chunker.chunk(docs)    
    assert isinstance(chunks[0], Document), show_result(f"Expected type: Document, Result: {type(chunks[0])}") 

def show_result(expected, result):
    return (f"""Expected: {expected} \n
    Result: {result}""")

