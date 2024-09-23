
# Thoughtful AI Support Chatbot

This is a simple chatbot built with Streamlit to answer basic questions about Thoughtful AI using predefined responses and an LLM fallback for unrecognized queries.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/thoughtful-ai-chatbot.git
   cd thoughtful-ai-chatbot
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key in a `.streamlit/secrets.toml` file:
   ```
   [general]
   OPENAI_API_KEY = "your_openai_api_key"
   ```

4. Run the Streamlit app:
   ```
   streamlit run chatbot.py
   ```

You can now interact with the chatbot through a web interface.
