# Equity Research Copilot

> Generative‑AI assistant that automates core equity research tasks — from sourcing disclosures and news to synthesizing insights and drafting analyst‑ready output.

---

## 🚀 Why this matters

* **Accelerate time‑to‑insight:** Target **\~75% reduction** in initial research and report drafting time.
* **Scale analyst coverage:** Enable **up to 3×** more companies per analyst through workflow automation.
* **Improve decision consistency:** Standardized analysis and templated outputs reduce variance and rework.

---

## ✨ What it does

* **Ingest**: Retrieve company disclosures (10‑K/Q), earnings transcripts, news, and pricing/ratio context.
* **Summarize**: Distill key sections (business overview, risks, segments) with reliable citations.
* **Sentiment**: Score narrative signals across filings and news to detect trend/inflection.
* **Valuation aides**: Surface ratio snapshots (P/E, P/S, EV/EBITDA) and DCF inputs for review.
* **Draft**: Generate an editable investment brief (talking points, risks, watch‑items) for analysts.

> **Example prompt**: `Analyze AAPL and prepare a 1‑pager with overview, recent drivers, valuation context, and top 5 risks, citing important passages.`

---

## 🧱 Architecture overview

* **Orchestration / UI**: CLI + optional Streamlit/Flask front‑end
* **GenAI runtime**: **Azure AI Foundry** (model deployments, safety, monitoring)
* **Retrieval**: Vector store (Azure AI Search or pgvector) for Retrieval‑Augmented Generation (RAG)
* **Pipelines**: ETL jobs to fetch and chunk source docs; metadata & citation tracking
* **Guardrails**: Content filters, source‑attribution, confidence flags, human‑in‑the‑loop review
* **Tests**: Unit tests for agents, E2E smoke tests on a small ticker set

```
app/
  ├─ ui/                # Streamlit / Flask app (optional)
  ├─ agents/            # retrieval, synthesis, drafting
  ├─ pipelines/         # ingestion, chunking, indexing
  ├─ services/          # Azure, vector DB, storage
  ├─ eval/              # prompt evals, regression tests
  └─ tests/             # unit + E2E
configs/
  ├─ app.toml           # feature flags
  └─ connections.toml   # endpoints, collections, index names
data/
  ├─ raw/               # downloaded source docs (gitignored)
  └─ index/             # vector artifacts (gitignored)
```

---

## 🛠️ Tech stack

* **Azure AI Foundry** (model deployments & safety)
* **Python** (pandas, requests, pydantic, fastapi/streamlit)
* **Vector DB**: Azure AI Search **or** PostgreSQL + **pgvector**
* **Scheduling**: cron / GitHub Actions for ingestion refresh
* **Testing**: pytest + data‑driven prompt checks


---

## 🔍 Key features

* **Cited answers**: Every claim links back to a paragraph in source docs.
* **Configurable templates**: 1‑pager, 3‑pager, or deck outline.
* **Valuation helpers**: Ratio snapshots and scaffolds for DCF inputs (manual review encouraged).
* **Sentiment tracks**: News vs. filings sentiment deltas to spot narrative shifts.
* **Analyst controls**: Redline edits, risk tagging, and watch‑list export (CSV/Markdown).

---

## 📈 Example outputs

* **Company overview**: business model, segments, geography
* **Recent drivers**: product launches, guidance shifts, regulatory updates
* **Valuation context**: P/E, P/S, EV/EBITDA time‑series snapshot
* **Top risks**: sourced from Item 1A and recent transcripts


---

## 🔒 Safety, accuracy & governance

* Retrieval‑only answers for factual claims; no free‑form “knowledge” without a source
* Guardrails for sensitive content; explicit **confidence flags** on low‑evidence sections
* **Human‑in‑the‑loop**: Analysts approve draft output before publication
* Test set of tickers ensures prompt/output regressions are caught early

---

## 🗺️ Roadmap

* [ ] Broker transcript and Q\&A slot extraction
* [ ] KPI extraction by sector (e.g., DAUs/MAUs for internet, RPO for SaaS)
* [ ] Valuation table auto‑refresh via scheduled data pulls
* [ ] Redteam evaluations and bias checks
* [ ] Multi‑company comp‑table generation

---


## 🙌 Acknowledgments

Built as part of an MSBA project exploring how GenAI can **automate and standardize equity research** while keeping analysts **in control** of judgment and sign‑off.
