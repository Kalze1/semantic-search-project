from neo4j import GraphDatabase
import pandas as pd

class Neo4jImporter:
    """
    A class to handle importing a dataset into a Neo4j database.
    """

    def __init__(self, uri, user, password):
        """
        Initializes the Neo4j connection.

        Args:
            uri (str): The URI of the Neo4j database (e.g., bolt://localhost:7687).
            user (str): The Neo4j username.
            password (str): The Neo4j password.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """
        Closes the Neo4j database connection.
        """
        self.driver.close()

    def import_data_in_batches(self, dataset_path, batch_size=1000):
        """
        Imports data from a CSV file into the Neo4j database in batches.

        Args:
            dataset_path (str): Path to the dataset CSV file.
            batch_size (int, optional): The number of rows to import in each batch. Defaults to 1000.
        """
        df = pd.read_csv(dataset_path)
        df = df.dropna(subset=["Title", "Combined_Text"])

        for i in range(0, len(df), batch_size):
            batch_df = df.iloc[i:i+batch_size]
            with self.driver.session() as session:
                for _, row in batch_df.iterrows():
                    session.run(
                        """
                        MERGE (item:Cloth {title: $title})
                        SET item.review = $review,
                            item.cons_rating = $cons_rating,
                            item.cloth_class = $cloth_class,
                            item.materials = $materials,
                            item.construction = $construction,
                            item.color = $color,
                            item.finishing = $finishing,
                            item.durability = $durability,
                            item.combined_text = $combined_text
                        """,
                        title=row["Title"],
                        review=row["Review"],
                        cons_rating=row["Cons_rating"],
                        cloth_class=row["Cloth_class"],
                        materials=row["Materials"],
                        construction=row["Construction"],
                        color=row["Color"],
                        finishing=row["Finishing"],
                        durability=row["Durability"],
                        combined_text=row["Combined_Text"],
                    )

                # Create relationships between items within the batch
                session.run(
                    """
                    MATCH (a:Cloth), (b:Cloth)
                    WHERE a.cloth_class = b.cloth_class AND a <> b
                    MERGE (a)-[:RELATED_TO]->(b)
                    """,
                )

if __name__ == "__main__":
    # Neo4j connection details
    NEO4J_URI = "bolt://localhost:7687"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "12345678"

    # Path to the dataset
    DATASET_PATH = "./backend/data/cleaned_dataset.csv" 

    # Import data into Neo4j
    importer = Neo4jImporter(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
    try:
        importer.import_data_in_batches(DATASET_PATH)
        print("Data import completed successfully.")
    finally:
        importer.close()