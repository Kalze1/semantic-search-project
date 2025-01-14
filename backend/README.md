# Backend - Semantic Search API

This folder contains the backend implementation for the semantic search project. It is built using **FastAPI** to handle search queries and provide a REST API.

## Features

- Processes user queries and computes semantic similarity using Sentence-BERT.
- Provides an endpoint to fetch search results based on relevance.
- Scalable and modular code structure.

## Folder Structure

backend/
├── app/ # Main application logic
│ ├── api/ # API endpoints
│ ├── core/ # Core logic (embeddings, search)
│ ├── models/ # Data models
├── requirements.txt # Backend dependencies
├── README.md # Backend-specific README

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Steps

1. **Install Dependencies**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run the Server**:

   ```bash
   uvicorn app.main:app --reload
   ```

3. **Test the API**:
   - Open `http://localhost:8000/docs` to view the interactive API documentation.
   - Use the `/search/` endpoint to perform queries.

## API Endpoints

- `GET /search/`: Accepts a query string and returns top search results.

## Example Usage

Example request to the `/search/` endpoint:

```bash
curl -X GET "http://localhost:8000/search/?query=example" -H "accept: application/json"
```
