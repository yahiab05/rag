# RAG - Retrieval-Augmented Generation

A FastAPI-based Retrieval-Augmented Generation (RAG) application that combines file upload and question-answering capabilities with a full-stack architecture.

## Features

- **File Upload**: Upload documents to ingest and process data
- **Question Answering**: Ask questions about your uploaded documents and get intelligent answers
- **FastAPI Backend**: High-performance async API
- **Modern Frontend**: Interactive user interface
- **MongoDB Integration**: Persistent data storage

## Project Structure

```
rag/
├── app.py                 # Main FastAPI application
├── frontend/              # Frontend application
│   ├── static/           # Static assets
│   └── templates/        # HTML templates
├── backend/              # Backend logic
│   └── main.py          # Core RAG pipeline and QA functions
└── .gitignore           # Git ignore rules
```

## Getting Started

### Prerequisites

- Docker installed and working

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yahiab05/rag.git
cd rag
```

2. Build image:
```bash
docker build -t rag .
```
4. Set up environment variables (if needed for MongoDB connection)
```bash
docker run rag
```
The application will be available at `http://localhost:8000`

## API Endpoints

- **GET `/`** - Serves the main HTML interface
- **POST `/upload`** - Upload a file for data ingestion
  - Request: Form data with `filepath`
  - Response: JSON with success message
- **POST `/query`** - Ask a question about uploaded documents
  - Request: JSON with `query` field
  - Response: JSON with `answer` field

## Architecture

### Frontend
- Located in `frontend/` directory
- Contains HTML templates and static files
- Served by FastAPI's StaticFiles and Jinja2Templates

### Backend
- Located in `backend/` directory
- Implements:
  - `data_ingestion_pipeline()` - Processes and ingests document data
  - `answer_question()` - Generates answers to user queries

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **MongoDB** - NoSQL database
- **Jinja2** - Template engine
- **Python** - Programming language

## Error Handling

The application includes error handling for:
- MongoDB connection failures
- Network connectivity issues
- Configuration errors

## License

This project is open source and available on GitHub.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
