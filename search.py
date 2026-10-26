    
import os
import requests
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def search_web(query, max_results=5):
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY is not set")

    url = "https://api.tavily.com/search"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": query,
        "max_results": max_results,
        "search_depth": "basic"
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    results = []

    for item in data.get("results", []):
        result = {
            "title": item.get("title", "No title"),
            "url": item.get("url", ""),
            "content": item.get("content", "")
        }

        results.append(result)

    return results


if __name__ == "__main__":
    query = input("Enter your research question: ")

    results = search_web(query)

    print("Data type:", type(results))
    print("Number of results:", len(results))

    if results:
        print("First title:", results[0]["title"])
        print("First URL:", results[0]["url"])
