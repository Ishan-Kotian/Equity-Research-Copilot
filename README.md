
# Equity Research Copilot (Streamlit + Azure OpenAI)

This Streamlit app implements your **one-agent** Equity Research Copilot with **file-first (RAG-style)** behavior and **GPT fallback**.
Upload files like `AAPL_company_profile.txt`, `AAPL_news.txt`, `AAPL_inputs.json` or just type a ticker and rely on GPT fallback.

## Local Run

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

# Set env vars (or use Streamlit Secrets when deploying)
export AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com"
export AZURE_OPENAI_KEY="<your-key>"
export AZURE_OPENAI_DEPLOYMENT="<your-deployment-name>"

streamlit run app.py
```

## Streamlit Community Cloud

1. Push these files to a GitHub repo (app.py, requirements.txt).
2. Create a new app in Streamlit Cloud and point to `app.py`.
3. In **Secrets**, add:
```
AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com"
AZURE_OPENAI_KEY="<your-key>"
AZURE_OPENAI_DEPLOYMENT="<your-deployment-name>"
```
4. Deploy.

## Notes

- If you upload files matching the ticker (e.g., AAPL_*), the app uses the files.
- If no files match, the app clearly states it used **GPT fallback**.
- Valuation only uses numeric inputs from files or GPT fallback if it can confidently infer numbers.
