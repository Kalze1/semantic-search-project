import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders search bar", () => {
  render(<App />);
  const inputElement = screen.getByPlaceholderText(/enter your search query/i);
  expect(inputElement).toBeInTheDocument();
});
