# Deep Researcher Agent

## Overview

Deep Researcher Agent is a multi‑stage AI research pipeline that automatically finds, analyses and synthesises information into a coherent report.  It leverages the [Agno](https://www.agno.com/) framework with Nebius LLM models and [ScrapeGraph](https://github.com/dmm-com/scrapegraph) tools to perform web searches, extract content, analyse sources and write a final report.  A Streamlit interface lets you run powerful research sessions directly from the browser.

## Features

- **Multi‑stage research workflow** – orchestrates search, analysis and report writing as separate steps.
- **Web scraping with ScrapeGraph** – extracts structured information from relevant web pages.
- **AI‑powered analysis** – uses Nebius Llama‑3 models to summarise and analyse source content.
- **Streamlit UI & CLI** – run the agent interactively via a web app or from the command line.
- **Secure API keys** – environment variables keep your Nebius and ScrapeGraph API keys safe.

## Tech stack

- Python 3.10+
- Agno
- Nebius Llama‑three models (via `NEBIUS_API_KEY`)
- ScrapeGraph
- Streamlit

## Prerequisites

To run this project you need:

- Python 3.10 or later.
- A Nebius AI API key.  Sign up at [Nebius AI Studio](https://ai.nebius.ai/) and create a token.
- A ScrapeGraph AI API key.

Set these in a `.env` file or as environment variables:

```env
NEBIUS_API_KEY=your_nebius_api_key
SGAI_API_KEY=your_scrapegraph_api_key
```

## Installation

```bash
# clone the repository
git clone https://github.com/AbdullahRasheed45/ai-projects-deep-researcher-agent.git
cd ai-projects-deep-researcher-agent

# create and activate a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate   # on Windows use venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# copy .env.example and add your API keys
cp .env.example .env
```

## Usage

### Streamlit interface

Launch the Streamlit app to use an interactive UI:

```bash
streamlit run app.py
```

Provide your Nebius and ScrapeGraph API keys in the sidebar, enter a research topic and click **Run Research**.  The app will display live status updates and stream the final report when it’s ready.

### Command‑line

You can also run the research workflow directly from the command line by importing the `run_research` function:

```bash
python -c "from agents import run_research; print(run_research('Artificial Intelligence'))"
```

## Deployment

This project includes a Streamlit app that can be deployed to platforms such as Hugging Face Spaces, Streamlit Community Cloud or your own server.  Ensure that your environment defines `NEBIUS_API_KEY` and `SGAI_API_KEY` so the agent can authenticate with Nebius and ScrapeGraph.

## License

This project is adapted from the [awesome‑ai‑apps](https://github.com/Arindam200/awesome-ai-apps) repository under the MIT license.  See the original project for more details.
