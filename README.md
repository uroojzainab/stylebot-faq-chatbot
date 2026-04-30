# StyleBot: E-Commerce FAQ Chatbot 🛍️

A lightweight, modular FAQ chatbot built with Python and Streamlit, designed to assist customers with common e-commerce queries like shipping, sizing, and returns.

## Structure
```text
project/
  ├── data/                # Contains the structured FAQ dataset (JSON)
  ├── src/                 # Contains the core matching logic
  ├── main.py              # The Streamlit web interface
  ├── requirements.txt     # Project dependencies
  └── README.md            # Project documentation
``` 
## Approach
This project avoids the overhead of large machine learning models by utilizing a deterministic string-matching approach. 

1. **Data Storage:** Knowledge is decoupled from the code and stored in a structured `faq_data.json` file.
2. **Retrieval Engine:** The system uses Python's built-in `difflib` library to calculate similarity ratios between the user's input and known questions.
3. **User Interface:** A web-based GUI built with Streamlit provides a clean, responsive chat environment, complete with quick-action buttons to solve the "blank canvas" user experience problem.

## Example Inputs & Outputs

**Input:** "Where is my package?"
**Output:** "Once your order ships, you will receive an email with a tracking link. You can also track it in your account under 'Order History'."

**Input:** "Can I get my money back?"
**Output:** "We accept returns within 30 days of delivery. Items must be unworn, unwashed, and have the original tags attached."

**Input:** "Do you sell shoes?" (Out of scope)
**Output:** "I'm sorry, I don't have an answer for that. Could you try rephrasing, or ask about shipping, returns, or sizing?"

## Limitations
* **Exact Keyword Reliance:** The current `difflib` matching algorithm relies heavily on lexical similarity. If a user uses completely different vocabulary (e.g., "apparel" instead of "clothes"), the confidence score may drop below the required threshold.
* **No Conversational Memory:** The chatbot treats every query independently and does not remember previous interactions within the session.

## Future Improvements
* **Semantic Search:** Replace the `difflib` keyword matcher with a lightweight NLP model (like sentence-transformers) to understand intent rather than just matching words.
* **Security & Validation:** Implement strict input sanitization to prevent potential injection attempts and add rate-limiting to protect the retrieval engine from automated abuse.
* **Database Integration:** Migrate the static JSON dataset to an SQLite or PostgreSQL database for easier updating and scaling.

## How to Run Locally
*Clone this repository.
*Install the required dependencies:
*pip install -r requirements.txt
*Launch the Streamlit application:
*streamlit run main.py
