def clean_docs(docs):
    clean_docs = [d for d in docs if len(d.page_content.split()) > 50]
    return clean_docs