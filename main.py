
from dotenv import load_dotenv

from search import search_web
from processor import process_results
from generator import generate_report

load_dotenv()


def main():
    question = input("Enter your research question: ")

    print("\nSearching the web...")
    results = search_web(question)
    print(f"Results found: {len(results)}")

    cleaned_results = process_results(results)
    print(f"Results after cleaning: {len(cleaned_results)}")

    if not cleaned_results:
        print("\nNo useful search results found. Try another question.")
        return

    print("\nGenerating research report...")

    report = generate_report(question, cleaned_results)

    print("\n--- Research Report ---\n")
    print(report)


if __name__ == "__main__":
    main()
