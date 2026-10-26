# 🔎 AI Research Assistant

An AI-powered research tool that searches the web, processes results, and generates structured research reports with source links.

## ✨ Features

- **Web Search:** Retrieves relevant web results using the Tavily API.
- **Result Processing:** Removes duplicate URLs and incomplete results.
- **AI-Generated Reports:** Uses Groq to generate structured answers and summaries.
- **Source Links:** Displays links to the webpages used for research.
- **Interactive Interface:** Built with Streamlit.
- **Caching:** Reuses search results for repeated questions.
- **Error Handling:** Displays helpful messages when something goes wrong.

## 🛠️ Tech Stack

- Python
- Streamlit
- Tavily Search API
- Groq API
- `requests`
- `python-dotenv`
- `uv`

## 📁 Project Structure

```text
ai-research-assistant/
├── app.py
├── main.py
├── search.py
├── processor.py
├── generator.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-research-assistant
```

### 2. Install dependencies

Install [uv](https://docs.astral.sh/uv/) if it isn't already installed, then run:

```bash
uv sync
```

### 3. Configure API keys

Create a `.env` file in the project root:

```text
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the example values with your actual API keys.

Never upload `.env` or publish your API keys.

### 4. Run the application

```bash
uv run streamlit run app.py
```

Open the local URL displayed in your terminal.

## 🚀 How It Works

1. The user enters a research question.
2. Tavily searches the web for relevant information.
3. The processor removes duplicate or incomplete results.
4. Groq generates a structured report using the retrieved content.
5. The application displays the report and source links.

## 🔮 Future Improvements

- More specific API error messages
- Improved caching
- Research quality evaluation
- Downloadable research reports
- Better source relevance and filtering

## 🔐 Security

API keys are loaded from environment variables using `python-dotenv`. Keep `.env` out of version control and use `.gitignore` to protect secrets.

## 📄 License

Choose a license before distributing this project publicly.
