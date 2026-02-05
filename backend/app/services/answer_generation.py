from langchain_core.prompts import PromptTemplate
from .vector_search import AtlasVectorSearch
from .retriever import Retriever
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama


class AnswerGenerator:
    def __init__(self):
        self.retriever = Retriever()
        self.vector_search = AtlasVectorSearch()
        self.template_inputs = ["context", "question"]
        self.template = """
            Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Do not answer the question if there is no given context.
    Do not answer the question if it is not related to the context.
    Do not give recommendations to anything other than what is given in the context.
    If the question isn't about the context, just write that you don't know without giving any explanation.
    Context:
    {context}
    Question: {question}
        """
        
        
    def answer(self, question):
        self.question = question
        try:
            retrieve = {
                "context": self.retriever.getRetriever() | (lambda docs: "/n/n".join([d.page_content for d in docs])),
                "question": RunnablePassthrough()
            }
        except ValueError as e:
            return "I don't know the answer to that question."
            
        llm = ChatOllama(model="qwen2.5:0.5b", temperature=0.5)
        
        prompt = PromptTemplate(input_variables=self.template_inputs, template=self.template)
        
        outputer = StrOutputParser()
        
        pipeline = (
            retrieve
            | prompt
            | llm
            | outputer
        )
        
        try:
            answer = pipeline.invoke(question)
        except ValueError as e:
            return "I don't know the answer to that question."
        return answer
