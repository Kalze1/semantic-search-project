from fastapi import APIRouter, HTTPException, Query  # Import FastAPI dependencies
import math

# Import custom modules from the app package
from app.core.search import SearchEngine
from app.core.knowledge_graph import KnowledgeGraph
from app.core.query_expansion import QueryExpansion

# Create an APIRouter instance for defining API endpoints
router = APIRouter()

# Initialize search engine, knowledge graph, and query expansion objects
engine = SearchEngine()  # For semantic search
graph = KnowledgeGraph("bolt://localhost:7687", "neo4j", "12345678")  # Connect to Neo4j knowledge graph

def sanitize_response(data):
    """
    Recursively replace NaN and Infinity values in a response with None.
    """
    if isinstance(data, dict):
        return {k: sanitize_response(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_response(v) for v in data]
    elif isinstance(data, float) and (math.isnan(data) or math.isinf(data)):
        return None
    return data

# Define a GET route for search requests
@router.get("/search/")
async def search(query: str, expand: bool = True):
    """
    Searches for relevant items based on a user query.

    Args:
        query (str): The user's search query.
        expand (bool, optional): Flag indicating whether to perform query expansion (default: True).

    Returns:
        dict: A dictionary containing the search results, including:
            - query (str): The original user query.
            - expanded_queries (list[str]): The list of expanded queries (if enabled).
            - results (list[dict]): The top 5 search results from the semantic search engine.
            - related_items (list[dict]): The top 5 related items retrieved from the knowledge graph.
    """
    try:
        # Perform query expansion if enabled
        expanded_queries = QueryExpansion.expand_query(query) if expand else [query]

        # Search for items using the expanded queries
        results = []
        for q in expanded_queries:
            results.extend(engine.search(q))

        # Limit results to the top 5
        results = sorted(results, key=lambda x: x.get("score", 0), reverse=True)[:5]

        # Integrate knowledge graph for related items
        related_items = []
        for result in results:
            cloth_class = result["item"].get("Cloth_class")
            if cloth_class:
                related_items.extend(graph.get_related_items(cloth_class))

        # Limit related items to the top 5
        related_items = related_items[:5]

        # Return the combined search response
        response = {
            "query": query,
            "expanded_queries": expanded_queries,
            "results": results,
            "related_items": related_items,
        }
        return sanitize_response(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
