# 🎓 Gemma Study Suite
### Local AI Academic Ecosystem — Powered by Gemma 4 + Ollama

> A fully offline, privacy-first academic toolkit that transforms raw PDFs — textbooks, question papers, and lecture notes — into professional study guides and interactive tutoring sessions using a local RAG pipeline.

---

## ✨ Overview

Gemma Study Suite is a **modular, local-first AI study companion** that runs entirely on your machine. No cloud. No data leaks. Just intelligent, structured learning powered by **Gemma 4 (via Ollama)**, **ChromaDB**, and **LangChain**.

```
Your PDFs  →  Vector Indexing  →  RAG Pipeline  →  Gemma 4  →  Notes / Tutor
```

---

## 🌟 Features

### 📄 1. Professional Note Architect — `generate_notes.py`

Generates exam-ready, structured notes in a strict **7-section academic format**:

| Section | Purpose |
|---|---|
| **Introduction** | What & Why |
| **Working** | How it operates |
| **Key Features** | Core characteristics |
| **Analysis** | Deep technical breakdown |
| **Advantages** | Strengths & benefits |
| **Limitations** | Trade-offs & drawbacks |
| **Conclusion** | Summary & takeaways |

**Additional highlights:**
- 🎨 HTML/CSS-based rendering with textbook-quality layout
- 🏷️ Color-coded headers and professional typography
- 📦 Batch processing — generate notes for multiple topics in one run
- ⚖️ Weightage-aware depth adjustment for **2-mark**, **5-mark**, and **10-mark** questions

---

### 👨‍🏫 2. Socratic AI Tutor — `tutor.py`

An interactive, adaptive tutor that guides you through concepts using the Socratic method:

```
Select Topic
    ↓
Learn Concept (in small modules)
    ↓
Answer Check-for-Understanding Questions
    ↓
Adaptive Feedback (Re-explain or Progress)
    ↓
Master Topic ✅
```

- ❌ Avoids giving direct answers — builds genuine understanding
- 🔄 Re-explains on incorrect responses
- ✅ Advances when mastery is demonstrated

---

### 🏗️ 3. Local Knowledge Base — `ingest.py`

Builds a fully local, searchable semantic index from your PDFs:

- 🔒 **100% offline** — no data ever leaves your machine
- 🧠 **HuggingFace `all-MiniLM-L6-v2`** embeddings for semantic understanding
- 💾 **ChromaDB** as the persistent vector store
- ⚡ Fast similarity search at query time

---

## 🛠️ Installation & Setup

### Prerequisites

1. **Install Ollama** — [Download from ollama.com](https://ollama.com)

2. **Pull the Gemma model:**
   ```bash
   ollama pull gemma3:4b
   ```

### Python Environment

```bash
# Create and activate a virtual environment
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
.\venv\Scripts\activate
```

### Install Dependencies

```bash
pip install langchain langchain-community langchain-huggingface \
    langchain-text-splitters pypdf chromadb \
    sentence-transformers xhtml2pdf
```

---

## 📂 Project Structure

```
gemma-study-suite/
│
├── my_pdfs/              # 📚 INPUT: Place your source PDFs here
├── chroma_db/            # 💾 Auto-generated vector knowledge base
├── generated_notes/      # 📄 Output: Styled PDF notes
│
├── ingest.py             # ⚙️  Step 1 — Index PDFs into ChromaDB
├── generate_notes.py     # 🚀  Step 2 — Generate structured notes
├── tutor.py              # 🎓  Step 3 — Launch interactive tutor
│
└── README.md
```

---

## 🚀 Usage Guide

### Step 1 — Index Your Material

Place your PDFs inside `my_pdfs/`, then run:

```bash
python ingest.py
```

This builds the **ChromaDB vector database** from your documents.

---

### Step 2 — Generate Structured Notes

```bash
python generate_notes.py
```

**Example input:**
```
IDA Pro, Web Attacks, RSA Encryption
```

**Output:** Professionally formatted PDFs saved to `generated_notes/`

---

### Step 3 — Interactive Tutoring Session

```bash
python tutor.py
```

Follow the on-screen prompts to select a topic and begin a guided learning session.

---

## 📐 Technical Architecture

| Component | Technology | Role |
|---|---|---|
| **LLM** | Gemma 4 via Ollama | Reasoning, generation & tutoring |
| **Vector Store** | ChromaDB | Stores and retrieves embeddings |
| **Embeddings** | `all-MiniLM-L6-v2` | Converts text to semantic vectors |
| **PDF Engine** | xhtml2pdf + CSS | Renders styled PDF output |
| **RAG Pipeline** | LangChain | Orchestrates retrieval & prompts |

### System Flow

```
User Query
   │
   ▼
Similarity Search (ChromaDB)
   │
   ▼
Context Injection into Prompt
   │
   ▼
Gemma 4 — Structured / Socratic Prompt
   │
   ▼
HTML/CSS Template Rendering
   │
   ▼
Final PDF Output  ✅
```

---

## 🔐 Privacy & Design Philosophy

| Principle | Implementation |
|---|---|
| ✅ Fully offline | Gemma runs locally via Ollama |
| ✅ No cloud uploads | ChromaDB stores data on-disk |
| ✅ No API keys needed | Zero external service dependency |
| ✅ Modular design | Each script works independently |
| ✅ Scalable | Add more PDFs anytime and re-index |

---

## 📌 Use Cases

- 📚 **Exam preparation** — Structured notes for any syllabus
- 🧠 **Concept mastery** — Socratic dialogue builds real understanding
- 📄 **Automated note generation** — Batch-convert textbook chapters
- 🎓 **Self-paced learning** — Study at your own pace, offline, privately

---

## 📜 License

This project is open-source. Refer to the `LICENSE` file for details.

---

<div align="center">

**Built for students who take their privacy seriously.**  
*No subscriptions. No tracking. Just learning.*

</div>
