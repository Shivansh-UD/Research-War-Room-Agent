from mcp.server.fastmcp import FastMCP
import arxiv

#Firstly we are creating the MCP server here
mcp = FastMCP("research-war-room")


#now we will create a funtion (tool) to get the data from the MCP server
# its just a function where where we give it a topic and a max value of 25  as parameters and it fetches the papers

@mcp.tool() # This is similar to how we do this in the Spring Framework in JAVA (@RestController)
def fetchPapers(topic: str, maxResults = 45) -> list[dict]:
    """
    Fetches research papers from ArXiv based on a topic.
    Returns a list of papers with title, abstract, and link.
    """

    client = arxiv.Client() # here we are making a client or like initializing arxiv

    search = arxiv.Search(query= topic, max_results= maxResults, sort_by=arxiv.SortCriterion.Relevance) #this is the line that searches for it

    papers = []
    for result in client.results(search):  # call results on client, not search
        papers.append({
            "title":    result.title,
            "abstract": result.summary,
            "link":     result.entry_id
        })

    return papers

if __name__ == "__main__":
    mcp.run()