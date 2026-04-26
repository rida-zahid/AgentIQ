# 🤖 AgentIQ — Multi-Agent News Intelligence System

A production-ready multi-agent AI system that analyzes any news topic using LangGraph orchestration, FAISS RAG, and Groq LLM. Unlike simple RAG pipelines, AgentIQ uses a decision-making agent that intelligently routes queries across multiple specialized tools.

## 🎥 Demo
▶ Watch AgentIQ in action — [LinkedIn Demo](#)

## 🧠 How It Works
User Query
│
▼
LangGraph Agent  ──►  decides which tools to use
│
├──► RAG Tool (FAISS + Sentence Transformers)
│         └──► Top-K Relevant Articles
│
├──► Summarizer Tool (Groq LLM)
│         └──► Concise Summary
│
└──► Extractor Tool (Groq LLM)
└──► Entities, Topics, Category
│
▼
FastAPI Response
│
▼
MLflow Tracking

## 🚀 Features
- 🔍 RAG Pipeline (FAISS + Sentence Transformers)
- 🤖 Multi-Agent Orchestration (LangGraph)
- 📝 Summarization Tool (Groq LLM)
- 🔎 Entity & Topic Extraction
- ⚡ FastAPI REST API
- 📊 MLflow Experiment Tracking
- 🎨 Gradio UI
- ✅ Automated Testing Suite

## 🗂️ Project Structure
AgentIQ/
├── data/
│   └── news_2000.csv        # 2000 news articles dataset
├── tools/
│   ├── rag.py               # FAISS retrieval
│   ├── summarizer.py        # Groq summarization
│   └── extractor.py         # Entity extraction
├── agent.py                 # LangGraph agent graph
├── pipeline.py              # Combined tools pipeline
├── api.py                   # FastAPI endpoints
├── app.py                   # Gradio UI
├── test_api.py              # Testing suite
├── mlflow_tracking.py       # MLflow integration
├── requirements.txt
└── README.md

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/rida-zahid/AgentIQ.git
cd AgentIQ
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set your Groq API key**
GROQ_API_KEY=your_key_here

## ▶️ Run

```bash
# Run Gradio UI
python app.py

# Run FastAPI
uvicorn api:app --reload

# Run MLflow
mlflow ui
```

## 📊 MLflow Tracking
![MLflow Runs](mlflow_runs.png)
![MLflow Metrics](mlflow_metrics.png)

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| LLM | Groq — Llama 3.3 70B Versatile |
| Agent Orchestration | LangGraph |
| Vector Search | FAISS |
| Embeddings | Sentence Transformers — all-MiniLM-L6-v2 |
| API | FastAPI |
| UI | Gradio |
| Experiment Tracking | MLflow |
| Language | Python 3.10+ |

## 🔒 Security Note
Never commit API keys. Read GROQ_API_KEY from environment. .env file is git-ignored.

## 🚀 Future Improvements
- Docker containerization
- RAGAS evaluation pipeline
- Fine-tuned TinyLlama integration
- Deploy to Hugging Face Spaces

## 👤 Author
Built by Rida Zahid — learning ML/AI in public.
[LinkedIn](https://www.linkedin.com/in/rida-zahid-382730309/) · Feel free to open issues or PRs!