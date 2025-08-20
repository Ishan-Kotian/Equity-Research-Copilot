import os
import json
import streamlit as st
from openai import AzureOpenAI

# --- Azure OpenAI setup ---
# Make sure these env vars are set in your terminal before running:
# export AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE-NAME.openai.azure.com/"
# export AZURE_OPENAI_KEY="YOUR-KEY"
# export AZURE_OPENAI_DEPLOYMENT="gpt-4o-mini"

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")

if not endpoint or not api_key:
    st.error("⚠️ Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY as environment variables.")
else:
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version="2024-05-01-preview"
    )

# --- Helper to load company files ---
def load_company_files(ticker: str):
    profile_file = f"{ticker}_company_profile.txt"
    news_file = f"{ticker}_news.txt"
    inputs_file = f"{ticker}_inputs.json"

    profile, news, inputs = "", "", ""

    if os.path.exists(profile_file):
        profile = open(profile_file, "r").read()

    if os.path.exists(news_file):
        news = open(news_file, "r").read()

    if os.path.exists(inputs_file):
        try:
            data = json.load(open(inputs_file, "r"))
            inputs = json.dumps(data, indent=2)
        except:
            inputs = open(inputs_file, "r").read()

    return profile, news, inputs

# --- Streamlit UI ---
st.title("📊 Equity Research Copilot")

ticker = st.text_input("Enter Ticker (e.g., AAPL):")

if st.button("Generate Report") and ticker:
    profile, news, inputs = load_company_files(ticker)

    context = f"""
You are an equity research analyst. Generate a professional research note for {ticker}.
If the provided files are empty, fall back to your own knowledge.

Company Profile:
{profile if profile else 'No profile file provided.'}

Recent News:
{news if news else 'No news file provided.'}

Valuation Inputs:
{inputs if inputs else 'No valuation inputs provided.'}
"""

    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": "You are a financial analyst generating stock research notes."},
                {"role": "user", "content": context}
            ],
            temperature=0.3,
            max_tokens=1200
        )

        report = response.choices[0].message.content
        st.subheader(f"Equity Research Note: {ticker}")
        st.write(report)

    except Exception as e:
        st.error(f"Error: {e}")