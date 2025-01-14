import React from "react"; // Import React library

const ResultsList = ({ results, expandedQueries, relatedItems }) => {
  /**
   * Handles rendering the list of search results.
   * - If there are no results (empty array), it returns null to avoid rendering an empty list.
   * - Otherwise, it iterates through the results array and renders each result as a list item.
   */

  return (
    <div style={{ marginTop: "20px" }}>
      

      {/* Related Items Section */}
      {relatedItems && relatedItems.length > 0 && (
        <div style={{ marginTop: "20px", textAlign: "left" }}>
          <h3>Related Items:</h3>
          <ul style={{ listStyleType: "square", paddingLeft: "20px" }}>
            {relatedItems.map((item, idx) => (
              <li key={idx}>
                <h4>{item.title}</h4> {/* Related item title */}
                <p>{item.description}</p> {/* Related item description */}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ResultsList;
