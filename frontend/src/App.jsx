import React, { useState } from "react"; // Import React and useState hook
import SearchBar from "./components/SearchBar.jsx"; // Import SearchBar component
import ResultsList from "./components/ResultsList.jsx"; // Import ResultsList component

const App = () => {
  /**
   * State variables:
   * - results: Stores the main search results received from the backend.
   * - expandedQueries: Stores the list of expanded queries if query expansion is enabled.
   * - relatedItems: Stores the related items retrieved from the knowledge graph.
   * - error: Stores any error messages encountered during the search process.
   */
  const [results, setResults] = useState([]);
  const [expandedQueries, setExpandedQueries] = useState([]);
  const [relatedItems, setRelatedItems] = useState([]);
  const [error, setError] = useState("");

  const handleSearch = async (query) => {
    /**
     * Handles the search query:
     * 1. Clears previous errors and results.
     * 2. Makes a GET request to the backend API with the query.
     * 3. Updates the state with the received results, expanded queries, and related items.
     * 4. Handles potential errors (e.g., network issues, backend errors).
     */
    setError("");
    setResults([]);
    setExpandedQueries([]);
    setRelatedItems([]);

    try {
      const response = await fetch(`http://localhost:8000/search/?query=${query}&expand=true`);
      if (!response.ok) {
        throw new Error("Backend could not process the request");
      }
      const data = await response.json();
      console.log(data)
      setResults(data.results || []);
      setExpandedQueries(data.expanded_queries || []);
      setRelatedItems(data.related_items || []);
    } catch (err) {
      if (err.message === "Failed to fetch") {
        setError("Connection problem: Unable to reach the backend.");
      } else {
        setError(err.message || "An unknown error occurred.");
      }
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <SearchBar onSearch={handleSearch} /> {/* Render the SearchBar component */}
      {error && <div style={{ color: "red", marginTop: "20px" }}>{error}</div>} {/* Display error messages */}
      <ResultsList
        results={results}
        expandedQueries={expandedQueries}
        relatedItems={relatedItems}
      /> {/* Render ResultsList with additional props Expanded queries and RelatedItems */}
    </div>
  );
};

export default App;
