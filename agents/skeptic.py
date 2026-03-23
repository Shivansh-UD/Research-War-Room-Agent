from groq import Groq
from rag.retriever import retrievePapers
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY) # setting up client wioth our API key

#Now we are defing the agent (Skeptic agent) with the help of the API key
def skepticAgent(topic: str) -> str:
    #retrive the papers
    papers = retrievePapers(f"Strong evidence not supporting {topic}", nResults= 7)

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
                    "You are the Skeptic agent in a scientific debate panel. "
                    "You will be given a topic and a list of papers. "
                    "Your job is to find and argue with the AGAINST evidence that opposes the topic. "
                    "Use specific facts, statistics, and findings from the papers to support your reasoning. "
                    "Always cite the paper title and link when referencing it. "
                    "Be confident, aggressive, and relentless in your skepticism — poke holes in every claim. "
                    "Keep your argument to 3-4 paragraphs."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Topic: {topic}\n\n"
                    f"Here are your retrieved papers as evidence:\n{evidence}\n"
                    f"Build your strongest argument not supporting this topic."
                )
            }
        ]
    )

    return response.choices[0].message.content