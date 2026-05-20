from groq import Groq

from config import (
    GROQ_API_KEY,
    MODEL_NAME
)

client = Groq(
    api_key=GROQ_API_KEY
)


def ask_llm(question, context):

    prompt = f"""
Answer only from the context below.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content