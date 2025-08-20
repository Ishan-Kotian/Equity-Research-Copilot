import streamlit as st
import requests
import os

# Load API details
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "1bkEyLVLHp38A1NYYznJiYhzYXFTgFx5VOGWq0rmiUBZZzJGDuniJQQJ99BGACHYHv6XJ3w3AAABACOGZQ1P")
AZURE_OPENAI_ENDPOINT = "https://cognitiveservice-patad004.openai.azure.com"
DEPLOYMENT_NAME = "gpt-4o-mini"  # your deployment name

headers = {
    "Content-Type": "application/json",
    "api-key": AZURE_OPENAI_KEY
}

st.title("⚖️ Equity Research Copilot")
st.markdown("""
This tool retrieves company insights including:
•⁠  ⁠*Business overview*
•⁠  ⁠*Recent news*
•⁠  ⁠*Valuation metrics*
""")

# User input
ticker = st.text_input("Enter a company ticker (e.g., AAPL):")

if ticker:
    st.write(f"Fetching insights for *{ticker}*...")

    # Example query
    data = {
        "messages": [
            {"role": "system", "content": "You are an equity research assistant. Summarize and analyze company details."},
            {"role": "user", "content": f"Give me a summary and valuation for {ticker}."}
        ],
        "temperature": 0.5,
        "max_tokens": 1200
    }

    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-08-01-preview"
    
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(result["choices"][0]["message"]["content"])
    else:
        st.error(f"Error: {response.status_code} - {response.text}")