from groq import Groq
from rag.retriever import retrievePapers
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY) # setting up client wioth our API key

#Now we are defing the agent (Optimistic agent) with the help of the API key
def optimisticAgent(topic: str) -> str:
    #first we will retrive the papers from the DB using the retrievePapers() function
    papers = retrievePapers(f"strong evidence supporting {topic}", nResults= 7)

    #Now we will format the papers so that its easier for the prompt to work with it.
    evidence = ""
    for p in papers:
        evidence += f"- Title: {p['title']}\n"
        evidence += f"  Link: {p['link']}\n"
        evidence += f"  Content: {p['text'][:300]}\n\n"
    

    #Now final;ly we are going tocall groq and make prompt for this agent to work like.
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are the Optimist agent in a scientific debate panel. "
                    "Your job is to find the strongest evidence SUPPORTING the topic. "
                    "Use facts, statistics, and specific findings from the papers provided. "
                    "Always cite the paper title and link when referencing it. "
                    "Be confident, enthusiastic, and persuasive. "
                    "Keep your argument to 3-4 paragraphs."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Topic: {topic}\n\n"
                    f"Here are your retrieved papers as evidence:\n{evidence}\n"
                    f"Build your strongest supporting argument for this topic."
                )
            }
        ]
    )

    return response.choices[0].message.content