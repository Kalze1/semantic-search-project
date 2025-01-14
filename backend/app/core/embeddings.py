import redis  # For caching embeddings
import pickle  # For serializing and deserializing Python objects
from sentence_transformers import SentenceTransformer  # For generating embeddings
import pandas as pd  # For loading and handling datasets
import numpy as np  # For similarity calculations


class EmbeddingManager:
    """
    Class for managing text embeddings, including dataset loading, caching, and similarity calculations.

    Attributes:
        model (SentenceTransformer): The SentenceTransformer model for generating embeddings.
        cache (redis.Redis): A Redis client for caching embeddings.
    """

    def __init__(self, model_name, redis_host="localhost", redis_port=6379):
        """
        Initializes the EmbeddingManager with the specified model name and Redis connection parameters.

        Args:
            model_name (str): Name of the pre-trained sentence transformer model.
            redis_host (str, optional): Hostname of the Redis server. Defaults to "localhost".
            redis_port (int, optional): Port of the Redis server. Defaults to 6379.
        """
        self.model = SentenceTransformer(model_name)  # Load the embedding model
        self.cache = redis.Redis(host=redis_host, port=redis_port)  # Connect to Redis cache

    def load_data(self, path):
        """
        Loads the dataset from a CSV file.

        Args:
            path (str): Path to the dataset CSV file.

        Returns:
            pd.DataFrame: The loaded dataset as a DataFrame.
        """
        data = pd.read_csv(path)
        return data

    def compute_embeddings(self, texts):
        """
        Computes embeddings for a list of texts.

        Args:
            texts (list[str]): List of text strings.

        Returns:
            np.ndarray: Array of embeddings.
        """
        return self.model.encode(texts)

    def cosine_similarity(self, query_emb, doc_embs):
        """
        Computes cosine similarity between a query embedding and document embeddings.

        Args:
            query_emb (np.ndarray): Query embedding vector (1D array).
            doc_embs (np.ndarray): Array of document embedding vectors (2D array).

        Returns:
            np.ndarray: 1D array of similarity scores for each document.
        """
        query_emb = query_emb.reshape(1, -1)  # Ensure query_emb is 2D
        scores = np.dot(doc_embs, query_emb.T).flatten() / (
            np.linalg.norm(doc_embs, axis=1) * np.linalg.norm(query_emb)
        )
        return scores


    def cache_embedding(self, text_id, text):
        """
        Caches the embedding for a given text in Redis.

        Args:
            text_id (str): Unique identifier for the text.
            text (str): The text to generate and cache the embedding for.
        """
        if not self.cache.get(text_id):  # Check if embedding is already cached
            embedding = self.model.encode(text)  # Generate embedding
            self.cache.set(text_id, pickle.dumps(embedding))  # Cache the embedding

    def get_embedding(self, text_id, text=None):
        """
        Retrieves the embedding for a given text_id from the cache or computes it if not found.

        Args:
            text_id (str): Unique identifier for the text.
            text (str, optional): The text to compute the embedding for if not cached.

        Returns:
            np.ndarray: The embedding vector, or None if not found and no text is provided.
        """
        cached_embedding = self.cache.get(text_id)  # Retrieve from cache
        if cached_embedding:
            return pickle.loads(cached_embedding)  # Load cached embedding

        if text:  # If text is provided and embedding is not in the cache
            embedding = self.model.encode(text)  # Compute embedding
            self.cache.set(text_id, pickle.dumps(embedding))  # Cache it
            return embedding

        return None  # Return None if not found and text is not provided
