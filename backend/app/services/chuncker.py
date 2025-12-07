from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import SentenceTransformersTokenTextSplitter
from data_ingestors.html_parser import HtmlParser
from data_ingestors.pdf_parser import PDFParser

class Chunker:
    def __init__(self):
        self.sementic_splitter = SentenceTransformersTokenTextSplitter(
            sentence_transformer_model_name="all-MiniLM-L6-v2",
            chunk_size=500,
            chunk_overlap=150
        )
        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, 
            chunk_overlap=150
            )
        
    def chunck(self, docs, sementic = True):
        if sementic:
            return self.chunck_sementic(docs)
        else:
            return self.chunck_simple(docs)
        
    def chunk_sementic(self, docs):
        return self.model.split_documents(docs)
    
    def chunk_simple(self, docs):
        return self.recursive_splitter.split_documents(docs)
    
    
def main():
    html = HtmlParser("https://en.wikipedia.org/wiki/Mohamed_Salah")
    pdf = PDFParser("../../vectors.pdf")
    
    html_docs = html.get_docs()
    pdf_docs = pdf.get_clean_docs()
    
    print(len(html_docs))
    print(len(pdf_docs))
    
    print(html_docs[0].page_content)
    print(pdf_docs[0].page_content)
    
    chunker = Chunker()
    html_chunked_docs = chunker.chunck(html_docs, sementic = False)
    pdf_chunked_docs = chunker.chunck(pdf_docs, sementic = True)
    print(html_chunked_docs[5].page_content)
    print(pdf_chunked_docs[5].page_content)
    
if __name__ == "__main__":
    main()