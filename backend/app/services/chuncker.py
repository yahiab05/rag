from sentence_transformers import SentenceTransformer, util
import nltk
from langchain_core.documents import Document

class Chunker:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        nltk.download('punkt')
        
    def chunck_split(self, docs, threshold = 0.6):
        text, metadata = self.extract_text(docs)
        
        sentences = nltk.sent_tokenize(text)
        
        embeddings = self.model.encode(sentences, convert_to_tensor=True)
        
        chunks = []
        current_chunks = [sentences[0]]
        
        for i in range(1, len(sentences)):
            similarity = util.cos_sim(embeddings[i], embeddings[i - 1]) 
            if similarity > threshold:
                current_chunks.append(sentences[i])
            else:
                chunks.append(current_chunks)
                current_chunks = [sentences[i]]
        
        if current_chunks:
            chunks.append(current_chunks)
        
        chunks = self.restore_docs(chunks, metadata)
        return chunks
    
    def extract_text(self, doc: list):
        for d in doc:
            text += " " + d.page_content
            
        return text, doc[0].metadata
    
    def restore_docs(self, chunks:list, metadata):
        docs = []
        for chunk in chunks:
            docs.append(Document(
                page_content=chunk, 
                metadata=metadata))
        return docs