from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY) # setting up client wioth our API key

#Now we are defing the agent (Summerizer agent) with the help of the API key
def summarizerAgent(topic: str, optimistArg: str, skepticArg: str, devilArg: str) -> str:

    # Format all three arguments for the user prompt
    fullDebate = (
        f"OPTIMIST ARGUMENT:\n{optimistArg}\n\n"
        f"SKEPTIC ARGUMENT:\n{skepticArg}\n\n"
        f"DEVIL'S ARGUMENT:\n{devilArg}\n\n"
    )


    #Now finally we are going tocall groq and make prompt for this agent to work like.
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are the Summarizer agent in a scientific debate panel. "
                    "You will be given arguments from 3 agents — Optimist, Skeptic, and Devil. "
                    "Your job is to summarize each agent in 1-2 paragraphs clearly and neutrally. "
                    "Use specific facts and statistics each agent mentioned. "
                    "Always cite paper titles and links when referenced. "
                    "End with an overall verdict — what does the science say about this topic overall? "
                    "Write in a way that someone who never saw the debate fully understands the topic from all angles."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Topic: {topic}\n\n"
                    f"Here is the full debate:\n{fullDebate}"
                    f"Write your complete summary and verdict."
                )
            }
        ]
    )

    return response.choices[0].message.content