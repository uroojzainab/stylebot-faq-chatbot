import json
import difflib

def load_faq_data(filepath):
    """Loads the structured dataset."""
    with open(filepath, 'r') as file:
        return json.load(file)

def get_chatbot_response(user_query, faq_data):
    """Finds the most relevant answer using basic string matching."""
    known_questions = list(faq_data.keys())
    
    # Matches user input to the closest question in our dataset
    matches = difflib.get_close_matches(user_query, known_questions, n=1, cutoff=0.6)
    
    if matches:
        best_match = matches[0]
        return faq_data[best_match]
    else:
        return "I'm sorry, I don't have an answer for that. Could you try rephrasing, or ask about shipping, returns, or sizing?"