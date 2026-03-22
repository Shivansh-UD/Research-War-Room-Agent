from mcp_server.arxivServer import fetchPapers
from rag.indexer import indexPapers
from rag.retriever import retrievePapers


#TESTING MCP SERVER
papers = fetchPapers("artificial intelligence impact society", maxResults = 15)

for p in papers:
    print(p["title"])
    print(p["link"])
    print("---")
    print()


#TESTING THE RAG SYSTEM ALONG WITH THE MCP TO SEE IF THEY WORK CORRECTLY TOGETHER

#firstly we index the papers from the collection in the DB (Vector DB mei papers ko insert karna)
indexPapers(papers)

#Now we search accoring to how a agent would serach
'''
THE STRING WE ARE PASSING THROUGH THE FUNCTION TO REPLICATE HOW AN AGENT WOULD SEARCH WORKS THE FORLLOWING WAY:
1. CONVERT THE STRING TO VECTORS(NUMBERS)
2. GOES THROUGH THE COLLECTION TO SEE AND SEARCH FOR THE VECTORS THAT ARE ENCODED SIMILALRY AND RETURNS THEM AS REQUIRED BY EACH DIFFERENT AGENT.
'''
print("=== OPTIMIST SEARCH ===")
for p in retrievePapers("strong evidence AI has positive benefits for society"):
    print(p["title"])

print("\n=== SKEPTIC SEARCH ===")
for p in retrievePapers("failures risks and dangers of AI for society"):
    print(p["title"])
