import pickle  # Module for serializing and deserializing Python objects
from pathlib import Path  # Module for handling filesystem paths

import pandas as pd  # Library for data manipulation and analysis
import streamlit as st  # Library for creating web apps

def load_file(path: str) -> pd.DataFrame:
    """
    Loads a pickled DataFrame from a specified file path.

    Args:
        path (str): The path to the pickled file.

    Returns:
        pd.DataFrame: The loaded DataFrame from the pickle file.
    """
    with open(path, "rb") as f:  # Open the file in binary read mode
        dataset = pickle.load(f)  # Load the pickled data into a DataFrame
        return dataset  # Return the loaded DataFrame

@st.cache_data  # Cache the function to prevent reloading data on each run
def load_data(folder: str) -> pd.DataFrame:
    """
    Loads all pickled DataFrames from a specified folder, concatenates them into a single DataFrame,
    and caches the result.

    Args:
        folder (str): The folder path containing pickled DataFrame files.

    Returns:
        pd.DataFrame: A concatenated DataFrame containing all loaded data.
    """
    # List comprehension to load all files in the folder and store them in a list of DataFrames
    all_datasets = [load_file(file) for file in Path(folder).iterdir()]

    # Concatenate all DataFrames into a single DataFrame
    df = pd.concat(all_datasets)

    return df  # Return the concatenated DataFrame
