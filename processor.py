
def process_results(results):
    cleaned_results = []
    seen_urls = set()

    for item in results:
        title = item.get("title", "").strip()
        url = item.get("url", "").strip()
        content = item.get("content", "").strip()

        if not url or not content:
            continue

        if url in seen_urls:
            continue

        seen_urls.add(url)

        cleaned_item = {
            "title": title or "Untitled",
            "url": url,
            "content": content
        }

        cleaned_results.append(cleaned_item)

    return cleaned_results
