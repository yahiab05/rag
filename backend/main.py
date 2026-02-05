from .app.services.answer_generation import AnswerGenerator
from .app.services.data_ingestion_pipeline import data_ingestion_pipeline
from pathlib import Path


def saving_docs(file_path):
    data_ingestion_pipeline(file_path)
    
def answer_question(question):
    answer = AnswerGenerator()
    return answer.answer(question)
