import chromadb
from sentence_transformers import SentenceTransformer



#Loading the model up which we want to impliment in the ChromaDB
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create a local ChromaDB client — stores data on your machine
client = chromadb.PersistentClient(path="./chroma_db")
'''
ChromaDB is an open-source, lightweight vector database designed to store and search through 
AI-generated data embeddings (like text, images, or audio). It acts as a "memory" for AI applications, 
allowing developers to quickly find similar information or provide context to Large Language Models
'''

def getCollection():
    return client.get_or_create_collection(name="papers")

def indexPapers(papers: list[dict]):
    """
    Takes a list of paper dicts from fetch_papers()
    and stores them in ChromaDB as vectors.
    """
    collection = getCollection()

    # Clear old papers so we start fresh for each new topic
    collection.delete(where={"source": "arxiv"})

    #Creating columns for our ChromaDB and we will append to each column accordingly
    ids = []
    embeddings = []
    documents   = []
    metadatas   = []

    """
    We build 4 lists in parallel — one entry per paper.
    ChromaDB needs all 4 to store a paper properly.

    ids        → unique name for each row e.g. "0", "1", "2"
                must be a string, not a number

    embeddings → the vector (384 numbers) representing the
                MEANING of the paper. this is what ChromaDB
                searches through when an agent queries it

    documents  → the raw text we embedded (title + abstract)
                stored so we can read it back after a search
                not just get numbers

    metadatas  → bonus info per paper (title, link, source)
                does NOT affect search, but agents need
                title + link to cite their sources properly

    at the end we call collection.add() ONCE with all 4 lists
    instead of inserting one paper at a time — more efficient
    """
    for i, paper in enumerate(papers):

        # Combine title + abstract for richer embedding
        fulltext = paper["title"] + " " + paper["abstract"]

        # Convert text to vector using sentence-transformers
        vector = model.encode(fulltext).tolist() #THIS IS THE MAIN LINE OF CODE HERE IS WHERE THE SENTENCES ARE GETTING TRANSFORMED INTO VECTORS

        ids.append(str(i))
        embeddings.append(vector)
        documents.append(fulltext)
        metadatas.append({
            "title":  paper["title"],
            "link":   paper["link"],
            "source": "arxiv"
        })

    collection.add(
        ids        = ids,
        embeddings = embeddings,
        documents  = documents,
        metadatas  = metadatas
    )

    print(f"Indexed {len(papers)} papers into ChromaDB")
