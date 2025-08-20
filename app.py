import streamlit as st
import requests
import os
import json

# 🔑 Azure OpenAI setup
AZURE_OPENAI_KEY = os.getenv(
    "AZURE_OPENAI_KEY",
    "1bkEyLVLHp38A1NYYznJiYhzYXFTgFx5VOGWq0rmiUBZZzJGDuniJQQJ99BGACHYHv6XJ3w3AAABACOGZQ1P"
)
AZURE_OPENAI_ENDPOINT = "https://cognitiveservice-patad004.openai.azure.com"
DEPLOYMENT_NAME = "gpt-4o-mini"  # Your deployment name

headers = {
    "Content-Type": "application/json",
    "api-key": AZURE_OPENAI_KEY
}

# --- Streamlit UI ---
st.title("📈 Equity Research Copilot")
st.markdown("""
This tool retrieves company insights including:
•⁠  ⁠*Business overview*
•⁠  ⁠*Recent news*
•⁠  ⁠*Valuation metrics*
•⁠  ⁠*Final recommendation*
""")

ticker = st.text_input("Enter a company ticker (e.g., AAPL):")

if ticker:
    st.write(f"🔎 Fetching insights for *{ticker}*...")

    # --- Step 1: Try to read local files ---
    local_summary, local_news, local_inputs = "", "", ""

    try:
        with open(f"{ticker.upper()}_company_profile.txt", "r") as f:
            local_summary = f.read()
    except:
        pass

    try:
        with open(f"{ticker.upper()}_news.txt", "r") as f:
            local_news = f.read()
    except:
        pass

    try:
        with open(f"{ticker.upper()}_inputs.json", "r") as f:
            local_inputs = json.load(f)
    except:
        pass

    # --- Step 2: Build prompt ---
    if local_summary or local_news or local_inputs:
        user_prompt = f"""
        You are an equity research analyst. Generate a structured research note for {ticker}.

        ### Company Overview:
        {local_summary if local_summary else "No local profile available."}

        ### Recent News:
        {local_news if local_news else "No local news available."}

        ### Valuation Inputs:
        {json.dumps(local_inputs, indent=2) if local_inputs else "No local valuation inputs available."}

        Please combine this into a structured note with:
        1. *Company Overview*
        2. *Recent News*
        3. *Valuation Metrics* (use inputs if provided, otherwise estimate)
        4. *Recommendation* (Buy/Hold/Sell with rationale)
        """
    else:
        # --- Step 3: Fallback to GPT Knowledge ---
        user_prompt = f"""
        No local files found for {ticker}.
        Use your internal knowledge to generate:
        1. *Company Overview*
        2. *Recent News*
        3. *Valuation Metrics*
        4. *Recommendation*
        """

    payload = {
        "messages": [
            {"role": "system", "content": "You are a financial analyst assistant providing concise equity research reports."},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1500
    }

    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-08-01-preview"
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        try:
            content = result["choices"][0]["message"]["content"]
        except:
            content = result["choices"][0]["messages"]["content"]
        
        st.success(content)
    else:
        st.error(f"Error {response.status_code}: {response.text}")