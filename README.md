```markdown
# 🤖 Agentic AI & Autonomous Systems Hands-On Tutorial

Welcome to the **Agentic AI Tutorial** repository! This repository contains a structured, progressive collection of hands-on projects and core concept implementations in Agentic AI, Multimodal Systems, RAG, and Vector Databases.

---
## 🌟 Key Project: AI Shopping Assistant

An end-to-end intelligent e-commerce assistant built with **Streamlit** and **LLM Agent Tooling**. 

### Key Features:
* 🖼️ **Shop by Image (Multimodal)**: Upload a product photo to automatically analyze visual features and retrieve matching items from the catalog[cite: 4].
* 💬 **Natural Language Filtering**: Query products by complex constraints (e.g., *"Show me only with ratings 4+"* or *"I want to buy an oil under $20"*)[cite: 2, 9].
* 🎯 **Structured Catalog Search**: Dynamically returns matching products with pricing, ratings, organic tags, and unique item IDs[cite: 2, 4, 9].
* 📦 **Automated Order Confirmation**: Select items via conversation to instantly place an order with estimated delivery details[cite: 2, 6].

---
## 📂 Repository Structure & Modules

Based on the core projects in this repository:

* **`health_analysis/`** 🩺
  * Health analysis workflows and diagnostic reasoning pipelines (e.g., blood work report analysis and medical insights).
* **`multimodel_agents/`** 👁️🤖
  * Implementation of multimodal AI agents capable of processing multi-modal inputs (image, vision, and text).
* **`project_shopping_agent/`** 🛒
  * End-to-end autonomous Shopping Agent leveraging tool-calling patterns, product lookups, dynamic reasoning, and decision-making loops.
* **`rag_basics/`** 📚
  * Fundamental Retrieval-Augmented Generation (RAG) hands-on pipelines—covering document chunking, overlap parameter tuning, and context retrieval.
* **`simple_llm_calling/`** ⚡
  * Base LLM API integrations, prompt execution, and foundational model interactions.
* **`single_agent/`** 🧠
  * Single AI agent setup featuring in-memory state management, tool execution, and conversational memory.
* **`vector_db/`** 🗄️
  * Direct hands-on with Vector Databases (embeddings generation, vector search queries, and similarity indexing).

---

## 🛠 Project Management & Tech Stack

This project is configured using modern Python package management with **uv** and standard configuration files:

* **Package Manager**: [`uv`](https://github.com/astral-sh/uv) (configured via `pyproject.toml` and `uv.lock`)
* **Language / Environment**: Python (`.python-version`)
* **Key Frameworks**: LangChain / LlamaIndex / OpenAI / ChromaDB / Streamlit

---

## 🚀 Quick Start & Setup

### 1. Prerequisites

Make sure you have **Python 3.10+** and **`uv`** installed on your system.

```bash
# Install uv if you haven't already
pip install uv

```

### 2. Clone the Repository

```bash
git clone [https://github.com/UdathuManasa/tutorial-agentic-ai.git](https://github.com/UdathuManasa/tutorial-agentic-ai.git)
cd tutorial-agentic-ai

```

### 3. Create & Sync Environment

Using `uv`, you can set up the virtual environment and sync dependencies instantly:

```bash
# Create virtual environment and install dependencies from uv.lock
uv sync

```

Activate the virtual environment:

```bash
# On macOS/Linux:
source .venv/bin/activate

# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env

```

Set up your required API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

```

---

## 🧪 Module Run Examples

* **Shopping Agent**:
```bash
streamlit run project_shopping_agent/app.py

```


* **Multimodal Agents**:
```bash
python -m multimodel_agents.main

```


* **Health Analysis App (Streamlit)**:
```bash
streamlit run health_analysis/app.py

```
