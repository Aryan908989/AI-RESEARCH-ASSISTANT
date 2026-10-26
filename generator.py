
import os
from groq import Groq


def generate_report(question, results):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not set")

    client = Groq(api_key=api_key)

    context = ""

    for i, item in enumerate(results, start=1):
        context += (
            f"\nSource {i}\n"
            f"Title: {item['title']}\n"
            f"URL: {item['url']}\n"
            f"Content: {item['content']}\n"
        )

    prompt = f"""
You are a research assistant.

Answer the user's question using the provided search results.
Organize the answer with clear headings and bullet points.
Do not invent facts or claim the sources say things they do not.
If the sources do not contain enough information, say so.
Include a Sources section with the source titles and URLs.

Research question:
{question}

Search results:
{context}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
