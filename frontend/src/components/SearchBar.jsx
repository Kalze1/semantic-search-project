import React, { useState } from "react"; // Import React and useState hook

const SearchBar = ({ onSearch }) => {
  /**
   * State variable:
   * - query: Stores the current search query entered by the user.
   */
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    /**
     * Handles form submission:
     * - Prevents default form submission behavior.
     * - Ignores empty queries to avoid unnecessary API calls.
     * - Calls the onSearch prop (passed from parent component) with the current query.
     */
    e.preventDefault();
    if (query.trim() === "") return;
    onSearch(query);
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        marginTop: "20px",
      }}
    >
      <input
        type="text"
        placeholder="Enter your search query..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{
          padding: "10px",
          width: "50%",
          fontSize: "16px",
          borderRadius: "5px",
          border: "1px solid #ccc",
          marginBottom: "10px",
        }}
      />
      <button
        type="submit"
        style={{
          padding: "10px 20px",
          backgroundColor: "#007bff",
          color: "white",
          fontSize: "16px",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Search
      </button>
    </form>
  );
};

export default SearchBar;