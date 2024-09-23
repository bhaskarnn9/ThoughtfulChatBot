
import streamlit as st
import openai

# Predefined dataset
PREDEFINED_RESPONSES = {
    "What does the eligibility verification agent (EVA) do?": 
    "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "What does the claims processing agent (CAM) do?": 
    "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "How does the payment posting agent (PHIL) work?": 
    "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "Tell me about Thoughtful AI's Agents.": 
    "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "What are the benefits of using Thoughtful AI's agents?": 
    "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

# Function to search predefined responses
def get_predefined_response(query):
    for question, answer in PREDEFINED_RESPONSES.items():
        if query.lower() in question.lower():
            return answer
    return None

# Fallback to OpenAI's LLM
def get_fallback_response(query):
    openai.api_key = st.secrets["OPENAI_API_KEY"]  # API key from Streamlit secrets
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Answer this question: {query}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Thoughtful AI Support Bot")

user_input = st.text_input("Ask a question about Thoughtful AI:")

if user_input:
    predefined_answer = get_predefined_response(user_input)
    
    if predefined_answer:
        st.write(f"**Answer:** {predefined_answer}")
    else:
        st.write("**Fetching response from AI...**")
        ai_answer = get_fallback_response(user_input)
        st.write(f"**AI Answer:** {ai_answer}")
