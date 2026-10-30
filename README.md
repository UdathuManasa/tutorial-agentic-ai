# 🤖 Agentic AI & LLM Engineering — Hands-on Projects

A hands-on engineering repository exploring **Generative AI, LLM applications, Retrieval-Augmented Generation (RAG), autonomous agents, multimodal AI, and AI-powered applications** using Python.

This repository documents my journey from understanding foundational LLM concepts to building practical AI applications that combine language models, external tools, vector databases, structured data, and interactive interfaces.

Rather than focusing only on theory, the implementations explore how LLM-powered systems can retrieve information, interact with external tools, process multimodal inputs, and execute multi-step workflows.

**Repository:** [tutorial-agentic-ai](https://github.com/UdathuManasa/tutorial-agentic-ai)

---

## 🌟 Featured Projects

### 1. 🛒 AI Shopping Assistant

An interactive e-commerce assistant that uses LLM-powered tool calling to help users discover products and interact with a product catalog through natural language.

**Key capabilities:**
- **Shop by Image:** Upload a product image and use multimodal AI to identify relevant product characteristics.
- **Natural Language Search:** Search and filter products using conversational queries.
- **Structured Product Retrieval:** Retrieve product information such as pricing, ratings, categories, and product attributes.
- **Tool Calling:** Allow the LLM to invoke application tools to retrieve and filter catalog information.
- **Order Workflow:** Support conversational product selection and order confirmation.

**Technologies:** Python, Streamlit, LLM APIs, Tool Calling.

### 2. 🩺 Health Analysis

An exploratory AI application focused on extracting information from health-related reports and using language models to generate contextual explanations.

**Areas explored:**
- Processing health report information.
- Retrieving relevant information using RAG concepts.
- Providing natural-language explanations of extracted data.
- Combining document context with LLM-based responses.

*This is an educational exploration, not a clinically validated diagnostic system or a substitute for professional medical advice.*

### 3. 👁️ Multimodal AI Agents

Exploring vision-language models that accept both textual and image inputs.

**Areas explored:**
- Image and text-based prompting.
- Vision-language model integrations.
- Multimodal input processing.
- Using models from different providers, including Gemini, Groq, and Qwen where supported by individual experiments.

---

## 📚 Repository Modules

The repository is organized into focused modules covering different aspects of LLM and Agentic AI engineering.

| Module | Focus |
|---|---|
| `simple_llm_calling/` | LLM API integration, prompting, model parameters and response generation |
| `rag_basics/` | Document processing, chunking, embeddings and semantic retrieval |
| `vector_db/` | Vector storage, indexing, collections and similarity search using ChromaDB |
| `single_agent/` | Single-agent workflows, tool execution, conversational state and ReAct concepts |
| `multimodel_agents/` | Multimodal and vision-language model experiments |
| `project_shopping_agent/` | Interactive AI-powered shopping assistant |
| `health_analysis/` | Health report analysis and contextual information retrieval |

Each module is intended to explore a specific concept or implementation pattern, progressing towards more integrated AI applications.

---

## 🧠 Concepts & Engineering Topics

### 1. Large Language Models (LLMs)
- Transformer architecture fundamentals.
- Next-token prediction and attention mechanisms.
- Prompt engineering and context management.
- Temperature, Top-K and Top-P sampling.
- Model API integrations.

### 2. Retrieval-Augmented Generation (RAG)
- Document ingestion and preprocessing.
- Fixed-size text chunking and chunk overlap.
- Embedding generation.
- Semantic similarity search.
- Vector indexing and retrieval using ChromaDB.
- Grounding LLM responses with retrieved context.

### 3. Agentic AI & Tool Calling
- Single-agent architectures.
- ReAct (Reasoning and Acting) workflow.
- Defining tools and exposing application functionality to LLMs.
- Tool invocation and result handling.
- Conversational state and memory.
- Structured outputs and Pydantic validation.
- Multi-step execution workflows.

### 4. Multimodal AI
- Vision-language model integrations.
- Image and text inputs.
- Multimodal prompting.
- Applying visual understanding to practical applications.

### 5. Evaluation & Observability
- Understanding response quality and retrieval relevance.
- Exploring guardrails and validation.
- Tracing and debugging LLM workflows.
- Exploring LangSmith for LLM observability and evaluation.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Package Management | uv |
| LLM Frameworks | LangChain, LangGraph |
| Model Providers | Google Gemini, Groq, Hugging Face (across individual experiments) |
| Embeddings | Hugging Face Sentence Transformers |
| Vector Database | ChromaDB |
| Application UI | Streamlit |
| Data Validation | Pydantic |
| Observability | LangSmith |

*Individual modules may use different libraries and model providers depending on the experiment.*

---

## 🚀 Getting Started

### Prerequisites

- Python (use the version specified in `.python-version`, if available).
- [uv](https://docs.astral.sh/uv/) Python package manager.
- API credentials for the model providers required by the individual projects.

### 1. Clone the repository

```bash
git clone https://github.com/UdathuManasa/tutorial-agentic-ai.git

cd tutorial-agentic-ai
```

### 2. Set up the Python environment

Install `uv` if it is not already available:

```bash
pip install uv
```

Synchronize the project dependencies:

```bash
uv sync
```

This creates the virtual environment and installs dependencies defined in the project configuration.

### 3. Configure environment variables

Create a `.env` file in the project root or the location expected by the individual module.

For example:

```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

Configure only the credentials required by the project you intend to run.

**Important:** Never commit API keys, credentials, or other secrets to GitHub.

### 4. Run the applications

**AI Shopping Assistant**

```bash
uv run streamlit run project_shopping_agent/app.py
```

**Health Analysis**

```bash
uv run streamlit run health_analysis/app.py
```

**Jupyter Notebooks**

```bash
uv run jupyter notebook
```

Individual experiments may have their own execution instructions and dependency requirements.

---

## 🗺️ Learning Roadmap

The repository follows a progression from foundational LLM concepts towards more sophisticated AI applications.

```text
LLM Fundamentals
       |
       v
LLM API Integration
       |
       v
Prompt Engineering
       |
       v
Embeddings & Vector Databases
       |
       v
Retrieval-Augmented Generation
       |
       v
Single-Agent Systems
       |
       v
Tool Calling & ReAct Workflows
       |
       v
Multimodal AI
       |
       v
End-to-End AI Applications
```

---

## 🎯 Goals of This Repository

The primary objective is to develop a practical understanding of how LLM-powered applications are designed and implemented.

Areas of continued exploration include:

- Designing reliable multi-step agent workflows.
- Improving retrieval quality and reducing hallucinations.
- Implementing robust tool execution and failure handling.
- Evaluating LLM responses and agent behavior.
- Building scalable AI-enabled backend services.
- Integrating AI capabilities into real-world applications.

---

## 📌 About

This repository is a continuously evolving collection of hands-on implementations, experiments, and projects in Generative AI and Agentic AI.

It reflects my interest in combining **backend engineering, distributed systems, automation, and emerging AI technologies** to build practical software systems.

**Author:** [Udathu Manasa](https://github.com/UdathuManasa)

- GitHub: [UdathuManasa](https://github.com/UdathuManasa)

---

⭐ If you find this repository useful, feel free to explore the implementations and share your feedback.
