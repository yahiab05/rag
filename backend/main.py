from app.services.data_ingestion_pipeline import data_ingestion_pipeline
from pathlib import Path

path = Path(__file__).parent.absolute()
data_ingestion_pipeline(file_path=str(path) + "/vectors.pdf", reset=True)

print("Done")
