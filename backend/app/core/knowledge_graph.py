from neo4j import GraphDatabase  # Import library for interacting with Neo4j graph database

class KnowledgeGraph:
    """
    Class for interacting with a Neo4j knowledge graph.

    Attributes:
        driver (neo4j.Driver): A Neo4j driver object used for creating sessions and running Cypher queries.

    Methods:
        __init__(self, uri, user, password):
            Initializes the KnowledgeGraph with the connection details for the Neo4j server.

        close(self):
            Closes the connection to the Neo4j server.

        query(self, cypher_query):
            Executes a Cypher query on the Neo4j graph and returns the results.

        get_related_items(self, cloth_class):
            Retrieves related items for a given cloth class from the knowledge graph.

    """

    def __init__(self, uri, user, password):
        """
        Initializes the KnowledgeGraph with the connection details for the Neo4j server.

        Args:
            uri (str): The URI of the Neo4j server.
            user (str): The username for accessing the Neo4j server.
            password (str): The password for accessing the Neo4j server.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))  # Create a Neo4j driver

    def close(self):
        """
        Closes the connection to the Neo4j server.

        This method should be called when you're finished using the KnowledgeGraph object
        to release resources and avoid connection leaks.
        """
        self.driver.close()
    
    def run_query(self, query, parameters=None):
        """
        Runs a Cypher query with optional parameters and returns the results.

        Args:
            query (str): The Cypher query to execute.
            parameters (dict, optional): Query parameters. Defaults to None.

        Returns:
            list: List of query results.
        """
        with self.driver.session() as session:
            return list(session.run(query, parameters))


    def query(self, cypher_query):
        """
        Executes a Cypher query on the Neo4j graph and returns the results.

        Args:
            cypher_query (str): The Cypher query to be executed on the Neo4j graph.

        Returns:
            list: A list of dictionaries, where each dictionary represents a record returned by the query.
        """
        with self.driver.session() as session:  # Create a Neo4j session
            result = session.run(cypher_query)  # Run the Cypher query
            return [record for record in result]  # Convert the result to a list of dictionaries

    def get_related_items(self, cloth_class):
        """
        Fetches related items based on a given cloth class.

        Args:
            cloth_class (str): The class of the clothing item (e.g., "Dresses").

        Returns:
            list[dict]: A list of related items with their titles and descriptions.
        """
        query = f"""
        MATCH (c:Cloth {{cloth_class: $cloth_class}})-[:RELATED_TO]->(related:Cloth)
        RETURN related.title AS title, related.review AS review
        """
        results = self.run_query(query, parameters={"cloth_class": cloth_class})
        return [{"title": record["title"], "review": record["review"]} for record in results]
