import streamlit as st
from src.logic import load_faq_data, get_chatbot_response

# Load the clothing dataset
faq_data = load_faq_data("data/faq_data.json")

# Configure the page appearance
st.set_page_config(page_title="StyleBot | FAQ", page_icon="🛍️")

# Store Branding
st.title("StyleBot 🛍️")
st.markdown("**Your 24/7 Fashion Store Assistant**")
st.write("Welcome! I can help you with your orders, shipping details, sizing, and returns.")

# Expandable category cheat sheet
with st.expander("💡 See what you can ask me"):
    st.markdown("""
    **📦 Shipping & Orders:**
    - How long does shipping take?
    - How can I track my order?
    - Can I cancel my order?
    
    **👗 Sizing & Fit:**
    - How do I know my size?
    - Do your clothes run true to size?
    
    **↩️ Returns & Exchanges:**
    - What is your return policy?
    - How do I exchange an item?
    """)

# Quick Action Buttons tailored to e-commerce
st.write("### Quick Questions:")
col1, col2, col3 = st.columns(3)

button_question = None
with col1:
    if st.button("Track Order"):
        button_question = "How can I track my order?"
with col2:
    if st.button("Return Policy"):
        button_question = "What is your return policy?"
with col3:
    if st.button("Find my Size"):
        button_question = "How do I know my size?"

st.divider()

# Manual input box
text_input = st.text_input("Or type your own question here:")

# Chatbot Response Logic
if st.button("Ask") or button_question:
    final_query = button_question if button_question else text_input
    
    if final_query:
        response = get_chatbot_response(final_query, faq_data)
        st.info("**You asked:** " + final_query)
        st.success("**StyleBot:** " + response)
    else:
        st.warning("Please type a question or click a quick link first.")