from .html_parser import HtmlParser
from .pdf_parser import PDFParser

def create_parser(file_path):
    if file_path.endswith(".pdf"):
        return PDFParser(file_path)
    elif file_path.startswith("http://") or file_path.startswith("https://"):
        return HtmlParser(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or HTML file.")