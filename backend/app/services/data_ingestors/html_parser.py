from bs4 import BeautifulSoup
from langchain_core.documents import Document
import requests
from . import Parse


class HtmlParser(Parse):
    def __init__(self, url):
        super().__init__(url)
        
    def parse(self):
        try:
            page = requests.get(self._path)
            soup = BeautifulSoup(page.content, "html.parser")
            for p in soup.find_all("p"):
                self._docs.append(Document(
                    page_content=p.text,
                    metadata={"source": self._path}
                    ))
            self._docs = self.clean_docs(self._docs)
            return self._docs
        except ConnectionError as e:
            raise ConnectionError(f"Error connecting to {self._url}: {e}")
        except IndexError as e:
            raise IndexError(f"No paragraphs available at {self._url}: {e}")
        
    def get_docs(self):
        return self._docs
