from sentence_transformers import SentenceTransformer
from rag.indexer import getCollection


#Setting up the model we will be using
model = SentenceTransformer('all-MiniLM-L6-v2')


def retrievePapers(query: str, nResults:int = 30) -> list[dict]:
    """
    This function searches ChromaDB for papers relevant to the query.
    Returns the top n_results most semantically similar papers.
    """
    collectionOfPapers = getCollection() # calling the function that gets all the papers from the DB

    #convertin the search quesry into a Vector

    queryVector = model.encode(query).tolist()

    # TTHE BELOW LINE IS VERY IMPORTANT BECAUSE IT ACTUALLY SEARCHED THE DB AND GETS THE MOST RELEVANT RESULTS USING THE VECTOR ENCODING
    results = collectionOfPapers.query(
        query_embeddings = [queryVector],
        n_results = nResults
    )

    #Now we put all the results we found in a LIST cleanly and return that list
    papers = []
    for i in range(len(results["ids"][0])):
        papers.append({
            "title": results["metadatas"][0][i]["title"],
            "link":  results["metadatas"][0][i]["link"],
            "text":  results["documents"][0][i]
        })

    return papers