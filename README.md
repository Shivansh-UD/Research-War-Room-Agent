
<div align="center">

```
██████╗ ███████╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██████╔╝█████╗  ███████╗█████╗  ███████║██████╔╝██║     ███████║
██╔══██╗██╔══╝  ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██║  ██║███████╗███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

██╗    ██╗ █████╗ ██████╗      ██████╗  ██████╗  ██████╗ ███╗   ███╗
██║    ██║██╔══██╗██╔══██╗     ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
██║ █╗ ██║███████║██████╔╝     ██████╔╝██║   ██║██║   ██║██╔████╔██║
██║███╗██║██╔══██║██╔══██╗     ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
╚███╔███╔╝██║  ██║██║  ██║     ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
```

### ⚔️ Four AI Agents. Real Papers. One Brutal Debate. ⚔️

*An Agentic AI system where multiple specialized agents debate each other*
*using live scientific papers as evidence — zero hallucinations.*

---

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=for-the-badge&logo=groq&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B35?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![ArXiv](https://img.shields.io/badge/ArXiv-2M+_Papers-B31B1B?style=for-the-badge)
![License](https://img.shields.io/badge/Cost-$0-00FF88?style=for-the-badge)

</div>

---

## 🧠 What Is This?

Most AI systems give you **one answer from one perspective.**

**Research War Room** gives you **four AI agents debating each other** using real scientific papers as weapons. Every argument is grounded in actual research fetched live from ArXiv. No hallucinations. No guessing. Just science vs science.

> You type a topic. The agents go to war.

---

## ⚔️ Meet The Agents

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   🟢  OPTIMIST    →   Finds the strongest SUPPORTING evidence   │
│                                                                 │
│   🔴  SKEPTIC     →   Finds the strongest OPPOSING evidence     │
│                                                                 │
│   😈  DEVIL       →   Finds the most UNEXPECTED findings        │
│                                                                 │
│   📊  SUMMARIZER  →   Reads all 3 and writes a FINAL VERDICT    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Each agent has its own personality, its own retrieval strategy, and its own system prompt. They're not just answering — they're **arguing.**

---

## 🏗️ Architecture

```
                        USER ENTERS TOPIC
                               │
                               ▼
                    ┌─────────────────────┐
                    │    orchestrator.py   │
                    │  (debate director)   │
                    └──────────┬──────────┘
                               │
               ┌───────────────┼───────────────┐
               ▼               ▼               ▼
    ┌─────────────────┐              ┌─────────────────┐
    │   MCP SERVER    │              │   RAG PIPELINE  │
    │  arxivServer.py │──────────►  │  indexer.py     │
    │                 │  25 papers   │  retriever.py   │
    │  Hits ArXiv API │              │  ChromaDB local │
    └─────────────────┘              └────────┬────────┘
                                              │
                          ┌───────────────────┼───────────────────┐
                          │                   │                   │
                          ▼                   ▼                   ▼
               ┌──────────────────┐  ┌───────────────┐  ┌──────────────┐
               │  🟢 optimist.py  │  │ 🔴 skeptic.py │  │ 😈 devil.py  │
               │                  │  │               │  │              │
               │ Searches for:    │  │ Searches for: │  │ Searches for:│
               │ "supporting      │  │ "limitations  │  │ "surprising  │
               │  evidence"       │  │  and failures"│  │  findings"   │
               │                  │  │               │  │              │
               │ → Groq API call  │  │ → Groq API    │  │ → Groq API   │
               └────────┬─────────┘  └───────┬───────┘  └──────┬───────┘
                        │                    │                  │
                        └────────────────────┼──────────────────┘
                                             │
                                             ▼
                                  ┌─────────────────────┐
                                  │  📊 summarizer.py   │
                                  │                     │
                                  │  Reads all 3 args   │
                                  │  Writes verdict     │
                                  │  Cites sources      │
                                  └──────────┬──────────┘
                                             │
                                             ▼
                                  ┌─────────────────────┐
                                  │    Streamlit UI      │
                                  │  3-page dark theme   │
                                  │  Chat-style debate   │
                                  │  Download report     │
                                  └─────────────────────┘
```

---

## 🔬 How RAG Works Here

```
TRADITIONAL AI                    RESEARCH WAR ROOM
──────────────                    ─────────────────

User asks question                User asks question
        │                                 │
        ▼                                 ▼
  AI uses memory              MCP fetches 25 real papers
  (can be wrong,                         │
   outdated,                             ▼
   hallucinated)              Papers embedded as vectors
        │                        stored in ChromaDB
        ▼                                 │
  One answer,                            ▼
  one perspective            Each agent searches with
                             their own biased query
                                         │
                                         ▼
                             Groq generates argument
                             grounded ONLY in real papers
                                         │
                                         ▼
                             Cited, verifiable, honest
```

---

## 📁 Project Structure

```
Research-War-Room-Agent/
│
├── 📂 mcp_server/
│   └── arxivServer.py        # Connects to ArXiv API, fetches papers
│
├── 📂 rag/
│   ├── indexer.py            # Embeds papers → stores in ChromaDB
│   └── retriever.py          # Semantic search by meaning, not keywords
│
├── 📂 agents/
│   ├── optimistic.py         # Finds supporting evidence → argues FOR
│   ├── skeptic.py            # Finds opposing evidence → argues AGAINST
│   ├── devil.py              # Finds unexpected findings → disrupts both
│   └── summarizer.py         # Reads full debate → writes verdict
│
├── 📂 pages/
│   ├── 1_Debate.py           # Chat-style debate UI page
│   └── 2_Verdict.py          # Verdict + download report page
│
├── orchestrator.py           # Wires everything together end-to-end
├── ui.py                     # Streamlit landing page
├── config.py                 # Loads API keys from .env
├── .env                      # 🔒 NOT pushed — your secrets live here
├── .gitignore                # Keeps .env and chroma_db out of git
└── requirements.txt          # All dependencies
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12
- A free [Groq API key](https://groq.com) (takes 2 minutes)
- That's it — everything else is local and free

### Installation

**1. Clone the repo**
```bash
git clone https://github.com/Shivansh-UD/Research-War-Room-Agent.git
cd Research-War-Room-Agent
```

**2. Create and activate a conda environment**
```bash
conda create -n warroom python=3.12 -y
conda activate warroom
```

**3. Install PyTorch (do this first to avoid conflicts)**
```bash
conda install -c conda-forge pytorch -y
conda install -c conda-forge sentence-transformers -y
```

**4. Install remaining dependencies**
```bash
pip install -r requirements.txt
```

**5. Set up your environment file**
```bash
# Create a .env file in the root folder
echo GROQ_API_KEY=your_key_here > .env
```

**6. Run the app**
```bash
streamlit run ui.py
```

Open your browser at `http://localhost:8501` and enter the war room. ⚔️

---

## 🧪 How To Use It

```
Step 1 ──► Open the app at localhost:8501

Step 2 ──► Type any research topic into the input box
           e.g. "Can AI replace doctors?"
                "Does social media harm teenagers?"
                "Is intermittent fasting effective?"

Step 3 ──► Click ENTER THE WAR ROOM
           (Takes ~15-30 seconds — fetching real papers!)

Step 4 ──► Go to the Debate page
           Read the 3 agents arguing in chat format

Step 5 ──► Click GET THE VERDICT
           Read the Summarizer's balanced analysis

Step 6 ──► Download the full report as a .txt file
           or click NEW TOPIC to start again
```

---

## 🛠️ Tech Stack

| Tool | Purpose | Cost |
|------|---------|------|
| **Groq** (LLaMA 3.3 70B) | Powers all 4 agents | Free tier |
| **ArXiv API** | Source of 2M+ scientific papers | Free |
| **ChromaDB** | Local vector database | Free |
| **Sentence Transformers** | Converts text to vectors for semantic search | Free |
| **MCP SDK** | Standardized tool protocol for AI agents | Free |
| **LangChain** | AI framework glue | Free |
| **Streamlit** | Web UI — pure Python, no HTML needed | Free |

**Total cost to run: $0** 🎉

---

## 💡 Key Concepts

### What is RAG?
**Retrieval Augmented Generation** — instead of letting the AI answer from memory (which can be wrong), we force it to retrieve real documents first and answer ONLY based on what it found. Like an open-book exam vs a closed-book exam.

### What is MCP?
**Model Context Protocol** — a standardized way to give AI agents access to external tools. Our MCP server wraps the ArXiv API so all agents can fetch papers through one clean interface.

### What is a Vector Database?
ChromaDB stores papers as lists of numbers (vectors) that represent their **meaning**. When an agent searches, it converts its query to a vector and finds papers with similar meaning — not just matching keywords. "Negative consequences of caffeine" finds papers about "side effects of coffee."

### What is Multi-Agent Orchestration?
Instead of one AI doing everything, multiple specialized agents each do one job. The orchestrator controls the flow — who runs when, in what order, passing results between them.

---

## 🔮 Future Upgrades

- [ ] **Streaming responses** — words appear token by token like ChatGPT
- [ ] **Agents respond to each other** — Skeptic directly challenges Optimist's specific claims
- [ ] **Semantic Scholar + PubMed** — more paper sources beyond ArXiv
- [ ] **GPT-4o / Claude** — upgrade LLM for deeper reasoning
- [ ] **Pinecone** — cloud vector DB to scale to millions of papers
- [ ] **Voice mode** — listen to agents debate via text-to-speech
- [ ] **User joins debate** — argue against the agents in real time

---

## 🧱 Built With

This project was built entirely from scratch as a learning exercise in:
- Agentic AI systems
- RAG pipelines
- MCP server design
- Multi-agent orchestration
- Prompt engineering
- Vector databases

Every module was built with a focus on understanding the fundamentals — not just copying boilerplate.

---

<div align="center">

**Built by [Shivansh](https://github.com/Shivansh-UD)**

*If this project helped you or inspired you — drop a ⭐ on the repo!*

```
⚔️  May your research always be cited  ⚔️
```

</div>
