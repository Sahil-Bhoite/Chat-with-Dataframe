import os  # Module for interacting with the operating system, e.g., environment variables

import streamlit as st  # Library for creating interactive web applications
from pandasai import SmartDataframe  # Class for querying DataFrames using AI
from pandasai.callbacks import BaseCallback  # Base class for handling callback events
from pandasai.llm import OpenAI  # Class for interfacing with OpenAI's LLMs
from pandasai.responses.response_parser import ResponseParser  # Class for formatting responses

from dataset import load_data  # Import the function to load data from the dataset module

class StreamlitCallback(BaseCallback):
    def __init__(self, container) -> None:
        """
        Initialize the callback handler to handle and display responses.

        Args:
            container: The Streamlit container to display the code responses.
        """
        self.container = container

    def on_code(self, response: str):
        """
        Display the code response in the Streamlit container.

        Args:
            response (str): The code response to display.
        """
        self.container.code(response)

class StreamlitResponse(ResponseParser):
    def __init__(self, context) -> None:
        """
        Initialize the response parser for formatting responses.

        Args:
            context: The context for the response parser.
        """
        super().__init__(context)

    def format_dataframe(self, result):
        """
        Format and display a DataFrame result in Streamlit.

        Args:
            result: The result containing the DataFrame to display.
        """
        st.dataframe(result["value"])  # Display the DataFrame in the Streamlit app
        return

    def format_plot(self, result):
        """
        Format and display an image plot result in Streamlit.

        Args:
            result: The result containing the image plot to display.
        """
        st.image(result["value"])  # Display the plot image in the Streamlit app
        return

    def format_other(self, result):
        """
        Format and display other types of results in Streamlit.

        Args:
            result: The result containing text or other data to display.
        """
        st.write(result["value"])  # Display text or other data in the Streamlit app
        return

# Streamlit app setup
st.write("# Chat with Dataset 🦙")  # Title of the Streamlit app

# Load the dataset from the specified path
df = load_data("./data")  # Ensure the path to the dataset is correct

# Display a preview of the DataFrame in an expandable section
with st.expander("🔎 Dataframe Preview"):
    st.write(df.tail(3))  # Show the last 3 rows of the DataFrame

# Input area for user queries
query = st.text_area("🗣️ Chat with Dataframe")  # Text area for user input
container = st.container()  # Container to hold the response output

if query:
    # Initialize the OpenAI LLM with the API token from environment variables
    llm = OpenAI(api_token=os.environ["OPENAI_API_KEY"])

    # Configure SmartDataframe with the LLM, response parser, and callback handler
    query_engine = SmartDataframe(
        df,
        config={
            "llm": llm,  # Set the LLM for querying
            "response_parser": StreamlitResponse,  # Set the response parser for formatting
            "callback": StreamlitCallback(container),  # Set the callback for displaying code responses
        },
    )

    # Query the data and get the answer
    answer = query_engine.chat(query)  # Use the chat method to get the response from the LLM
