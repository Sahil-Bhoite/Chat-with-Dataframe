# Dataset Chat Application 🦙💬

This Streamlit application allows users to interact with a dataset using natural language queries. It combines the power of Streamlit for the user interface, PandasAI for intelligent dataframe operations, and OpenAI's language model to interpret and execute user queries.

## Features

- Load and preview datasets
- Chat interface for querying the dataset
- Support for various types of responses (dataframes, plots, text)
- Real-time code execution display

## Prerequisites

Before running this application, make sure you have the following:

- Python 3.7+
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Sahil-Bhoite/Chat-with-Dataframe/git
   cd dataset-chat-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

1. Place your dataset files in the `./data` directory. The application supports pickled dataframes.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

4. Use the chat interface to query your dataset using natural language.

## Project Structure

- `app.py`: Main application file containing the Streamlit UI and query processing logic.
- `dataset.py`: Utility functions for loading and processing data.
- `./data/`: Directory to store your dataset files.

## How It Works

1. The application loads datasets from the `./data` directory using the `load_data` function in `dataset.py`.
2. Users can preview the loaded dataframe and enter natural language queries in the text area.
3. Queries are processed using PandasAI's SmartDataframe, which utilizes OpenAI's language model to interpret and execute the queries.
4. Results are displayed in the Streamlit UI, supporting various output types including dataframes, plots, and text.

## Customization

You can customize the application by modifying the following:

- Adjust the OpenAI model or parameters in the `app.py` file.
- Modify the `StreamlitCallback` and `StreamlitResponse` classes to change how results are displayed.
- Update the data loading logic in `dataset.py` if you need to support different file formats.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[[Insert your chosen license here](https://github.com/Sahil-Bhoite/Chat-with-Dataframe/blob/main/LICENSE)]

## About the Developer

LinkedIn: [Sahil Bhoite](https://www.linkedin.com/in/sahil-bhoite/)
Portfolio: [Sahil Bhoite's Portfolio](https://sahil-bhoite.github.io/Portfolio/)
