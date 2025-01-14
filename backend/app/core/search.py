from app.core.embeddings import EmbeddingManager
from app.core.config import Config

class SearchEngine:
    def __init__(self):
        self.embed_manager = EmbeddingManager(Config.EMBEDDINGS_MODEL)
        self.data = self.embed_manager.load_data(Config.DATA_PATH)  # Load dataset
        self.embeddings = self.embed_manager.compute_embeddings(
            self.data["Combined_Text"].tolist()
        )  # Compute embeddings for documents

    def search(self, query):
        """
        Performs a semantic search using the query.

        Args:
            query (str): The user's search query.

        Returns:
            list[dict]: A list of top search results with scores.
        """
        query_embedding = self.embed_manager.compute_embeddings([query])
        scores = self.embed_manager.cosine_similarity(query_embedding, self.embeddings)

        # Get top 5 results
        results = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:5]
        return [
            {
                "item": self.data.iloc[idx].to_dict(),
                "score": float(score),  # Convert numpy.float32 to Python float
            }
            for idx, score in results
        ]

