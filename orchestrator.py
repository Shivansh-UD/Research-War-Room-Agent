from rag.indexer import indexPapers
from agents.optimistic import optimisticAgent
from agents.skeptic import skepticAgent
from agents.devil import devilAgent
from agents.summarizer import summarizerAgent
from mcp_server.arxivServer import fetchPapers

# Manages the entire debate pipeline from fetching papers to running all agents
def orchestratorAgent(topic: str) -> dict:

    # Step 1 — fetch papers from ArXiv via MCP server
    listOfPapers = fetchPapers(topic)

    # Step 2 — index papers into ChromaDB for agent retrieval
    indexPapers(listOfPapers)

    # Step 3 — run each debate agent in order
    a1 = optimisticAgent(topic)
    a2 = skepticAgent(topic)
    a3 = devilAgent(topic)
    a4 = summarizerAgent(topic, a1, a2, a3)

    # Step 4 — return all results as a clean dictionary for the UI
    return {
        "topic":    topic,
        "optimist": a1,
        "skeptic":  a2,
        "devil":    a3,
        "summary":  a4
    }