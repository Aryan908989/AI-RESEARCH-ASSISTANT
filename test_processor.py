
from processor import process_results

sample_results = [
    {
        "title": "AI Research",
        "url": "https://example.com/ai",
        "content": "AI is used in research."
    },
    {
        "title": "AI Research Duplicate",
        "url": "https://example.com/ai",
        "content": "This is a duplicate."
    },
    {
        "title": "Empty Content",
        "url": "https://example.com/empty",
        "content": "   "
    },
    {
        "title": "Cybersecurity",
        "url": "https://example.com/security",
        "content": "AI can help detect threats."
    }
]

cleaned = process_results(sample_results)

print("Before:", len(sample_results))
print("After:", len(cleaned))

for item in cleaned:
    print(item["title"], "-", item["url"])
