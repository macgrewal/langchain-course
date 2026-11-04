# LangChain Course

A small LangChain agent project that performs a web search and answers a question using OpenAI and Tavily.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) installed
- API keys for:
  - OpenAI
  - Tavily

## Project setup

1. Clone the repository and move into the project directory:

   ```bash
   cd /path/to/langchain-course
   ```

2. Install the project dependencies:

   ```bash
   uv sync
   ```

3. Create a `.env` file in the project root with your API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## Run the app

You can run the project either with Python module syntax or the installed script:

```bash
uv run python -m langchain_course
```

or

```bash
uv run langchain-course
```

The app currently asks: "What's the weather like in Wolverhampton?" and prints the agent response from the search tool.

## Project structure

```text
langchain-course/
├── src/
│   └── langchain_course/
│       ├── __init__.py
│       ├── __main__.py
├── .env
├── pyproject.toml
├── README.md
└── uv.lock
```

## Notes

- The project uses `uv` for dependency management.
- The executable entry point is defined in `pyproject.toml`.
- `load_dotenv()` reads environment variables from `.env` automatically.
