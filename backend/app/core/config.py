import os  # Import the 'os' module for environment variable access

class Config:
    """
    Configuration class for application settings.

    Attributes:
        EMBEDDINGS_MODEL (str): The name of the pre-trained embeddings model.
            Defaults to "sentence-transformers/all-MiniLM-L6-v2" if not specified in the environment.
        DATA_PATH (str): The path to the dataset file.
            Defaults to "data/dataset.csv" if not specified in the environment.
    """
    EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2") 
    DATA_PATH = os.getenv("DATA_PATH", "data/cleaned_dataset.csv")