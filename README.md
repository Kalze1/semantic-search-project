# **Semantic Search System for Clothing Dataset**

This project implements a Semantic Search System, allowing users to search for items or information based on natural language queries. The system is designed to demonstrate the concept and implementation of semantic search, leveraging FastAPI for the backend, React for the frontend, and integrating with Neo4j for a knowledge graph to enhance search relevance and accuracy.

---

## **Features**

- **Semantic Search**: Find clothing items using natural language queries.
- **Query Expansion**: Automatically suggests synonyms or related terms for better search results.
- **Knowledge Graph Integration**: Displays related clothing items using relationships from the dataset.
- **Top Results**: Returns the top 5 most relevant results and related items for each query.

---

## **Technologies Used**

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend**: [React](https://reactjs.org/)
- **Database**: [Neo4j](https://neo4j.com/)
- **Embedding Model**: [SentenceTransformers](https://www.sbert.net/)

---

## **Setup Instructions**

### **Backend**

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

### **Frontend**

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

### **Neo4j**

1. Install Neo4j and start the database.
2. Load the dataset into Neo4j using the provided script:
   ```bash
   python backend/data/import_to_neo4j.py
   ```

---

## **How to Use**

1. Start the backend, frontend, and Neo4j database.
2. Open the frontend at [http://localhost:5173](http://localhost:5173).
3. Enter a query in the search bar (e.g., "Comfortable dresses").
4. View the top results and related items.

---

## **Folder Structure**

- **backend/**: Backend API for semantic search and knowledge graph integration.
- **frontend/**: React app for user interaction.
- **data/**: Dataset and scripts for Neo4j data import.

---
