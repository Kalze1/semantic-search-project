from nltk.corpus import wordnet  # Import WordNet corpus for synonym and related word lookup

class QueryExpansion:
    """
    Class for expanding user queries using synonyms and related words.

    Methods:
        @staticmethod
        expand_query(query):
            Expands the given query by finding synonyms and related words using WordNet.

    """

    @staticmethod
    def expand_query(query):
        """
        Expands the given query by finding synonyms and related words using WordNet.

        Args:
            query (str): The user's search query.

        Returns:
            list: A list of expanded query terms, including the original words and their synonyms/related words.
        """
        words = query.split()  # Split the query into individual words
        expanded = set(words)  # Create a set to store unique expanded terms

        for word in words:
            for syn in wordnet.synsets(word):  # Get synsets (sets of synonyms) for each word
                for lemma in syn.lemmas():  # Get lemmas (word forms) from each synset
                    expanded.add(lemma.name().replace("_", " "))  # Add lemma names (synonyms/related words) to the set, replacing underscores with spaces

        return list(expanded)  # Convert the set of expanded terms back to a list