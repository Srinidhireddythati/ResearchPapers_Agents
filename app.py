import streamlit as st
from research.pipeline import Pipeline

# Set up the Streamlit app
st.title("Chat with Research Papers(Agents) 🔎🤖")
st.caption("This app allows you to chat with arXiv research papers using GPT-4.")

# Input field for the OpenAI API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Get the search query from the user
query = st.text_input("Enter the Search Query")

if api_key and query:
    # Initialize pipeline
    pipeline = Pipeline(api_key)

    # Execute pipeline with the search query
    results = pipeline.execute(query)

    for paper in results['papers']:
        st.write(f"### {paper['title']}")
        st.write(paper['summary'])
        st.write(f"[Read more]({paper['url']})")

    if 'insights' in results and results['insights']:
        st.write("**AI Generated Insights:**")
        st.write(results['insights'])
