import os
import streamlit as st
from dotenv import load_dotenv

# Import the research function from agents
from agents import run_research

# Load environment variables from a .env file if it exists
load_dotenv()

st.set_page_config(page_title="Deep Researcher Agent")

st.title("Deep Researcher Agent")

# Sidebar inputs for API keys
with st.sidebar:
    st.header("API Keys")
    nebius_key = st.text_input("Nebius API Key", type="password")
    scrape_key = st.text_input("ScrapeGraph API Key", type="password")
    st.markdown("---")

# Input for the research topic
topic = st.text_input("Enter a research topic")

if st.button("Run Research"):
    if not topic:
        st.error("Please enter a topic.")
    elif not nebius_key or not scrape_key:
        st.error("Please provide both API keys.")
    else:
        # Set environment variables for the agent
        os.environ["NEBIUS_API_KEY"] = nebius_key
        os.environ["SGAI_API_KEY"] = scrape_key

        with st.status("Running research...", expanded=True):
            report = run_research(topic)

        # Display the final report
        st.markdown(report)
