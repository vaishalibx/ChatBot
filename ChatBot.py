import streamlit as st
from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="AI Chat Bot",
    page_icon="🤖",
    layout="wide"
)

# Add a title and description
st.title("AI Chat Bot 🤖")
st.markdown("Ask me anything!")

# Get API key from environment variable
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found in .env file!")
    st.stop()

# Initialize the agent
@st.cache_resource
def get_agent():
    return Agent(
        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=api_key
        ),
        markdown=True
    )

agent = get_agent()

# Create the input field
user_question = st.text_input("Enter Your Question:", key="user_input")

if user_question:
    with st.spinner("Thinking..."):
        st.markdown("### Answer:")
        # Get the agent's response
        response = agent.run(user_question)
        st.markdown(response.content)





