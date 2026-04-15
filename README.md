This `README.md` file is designed to be comprehensive, guiding anyone (including your future self) through setting up, indexing, and using your Local RAG system.

You should save this content as `README.md` in the root directory of your project folder (`gemma_notes_rag/`).

***

# 🧠 Local RAG Study Note Generator (Gemma 4 Powered)

This project is a fully local, self-contained Retrieval-Augmented Generation (RAG) system designed to create personalized, high-quality study notes from a collection of personal documents (PDFs). It leverages the power of the **Gemma 4** Large Language Model running locally via **Ollama**.

## ✨ Overview

The system is split into two main phases:

1.  **Ingestion (Indexing):** Processes your raw PDF files, converts their content into searchable data, and builds a local knowledge base (Vector Database).
2.  **Generation (RAG):** Allows you to ask specific questions about your material, retrieves the most relevant context from your PDFs, and uses Gemma 4 to synthesize those notes into organized summaries.

## 🛠️ Prerequisites

Before starting, ensure you have the following installed:

*   **Ollama:** Installed and running on your system.
*   **Python 3.x:** Installed on your system.
*   **Required Python Libraries:**
    ```bash
    pip install pypdf sentence-transformers chromadb langchain
    ```

## 📂 Project Structure

The project is structured to keep your data separate from your code and your index.

```
gemma_notes_rag/
├── my_pdfs/                  <-- 📚 INPUT: Place all your source PDFs here (e.g., Q-papers, notes).
├── chroma_db/                <-- 💾 OUTPUT: The Vector Database created by the ingestion script.
├── ingest.py                 <-- ⚙️ SCRIPT 1: Builds the knowledge base.
├── generate_notes.py         <-- 🚀 SCRIPT 2: Runs the RAG process to generate notes.
└── README.md                 <-- This file!
```

## ⚙️ Phase 1: Building the Knowledge Base (Ingestion)

**Goal:** To process all PDFs in the `my_pdfs/` folder and create a searchable index in `chroma_db/`.

### Step 1: Prepare Your Data
1.  Create the `my_pdfs/` folder in your project root.
2.  Place all your source PDF files inside this folder.

### Step 2: Run the Ingestion Script
Execute the ingestion script from your terminal. This process will read your PDFs and create the knowledge base.

```bash
python ingest.py
```

**⚠️ Important Note:** The first run will take time as it reads and processes all your documents. Once complete, a folder named `chroma_db/` will be created, containing your indexed data.

---

## 🚀 Phase 2: Generating Notes (RAG Engine)

**Goal:** To ask a question and generate customized study notes using the indexed data.

### Step 1: Run the Generator Script
Execute the generation script. You will be prompted to enter your question.

```bash
python generate_notes.py
```

### Step 2: Interact with the System
The script will prompt you for an input question (e.g., "Summarize the key definitions from the provided material regarding quantum mechanics.")

The system will then automatically:
1.  **Retrieve:** Search the `chroma_db/` for the most relevant text.
2.  **Prompt:** Combine the retrieved text with your question into a highly specific instruction for **Gemma 4**.
3.  **Generate:** Send the instruction to the local Gemma 4 model to produce your custom study notes.

---

## 📚 System Architecture (How It Works)

| Component | Role | Technology |
| :--- | :--- | :--- |
| **PDFs** | Raw Knowledge Source | Your uploaded files |
| **Ingestion Script** | Knowledge Builder | `pypdf`, `sentence-transformers`, `ChromaDB` |
| **`chroma_db/`** | The Knowledge Base | Vector Store (Search Index) |
| **`generate_notes.py`** | RAG Engine | LangChain, ChromaDB |
| **Gemma 4 (via Ollama)** | The Brain | Local LLM |

**The Flow:**
$$\text{Question} \rightarrow \text{Retrieval (ChromaDB)} \rightarrow \text{Context} \rightarrow \text{Prompt Construction} \rightarrow \text{Gemma 4 (LLM)} \rightarrow \text{Personalized Notes}$$# study_bot
