🎓 Gemma-Study-Suite: Local AI Academic Ecosystem
A comprehensive, privacy-focused academic toolkit that transforms raw PDFs (textbooks, question papers, lecture notes) into professional study guides and interactive tutoring sessions. Powered by Gemma 4 via Ollama and a local RAG (Retrieval-Augmented Generation) pipeline.

🌟 Key Features
1. 📄 Professional Note Architect (generate_notes.py)
Strict 7-Section Formatting: Every note is generated using a standardized academic skeleton:
Introduction $\rightarrow$ Working $\rightarrow$ Key Features $\rightarrow$ Analysis $\rightarrow$ Advantages $\rightarrow$ Limitations $\rightarrow$ Conclusion.
Premium PDF Styling: Uses HTML/CSS templates to generate textbook-quality PDFs with color-coded headers, meta-boxes, and professional typography.
Batch Processing: Generate notes for multiple topics/questions in one single run.
Weightage-Aware: Adjusts the depth of the content based on the marks assigned to the question (2, 5, or 10 marks).
2. 👨‍🏫 Socratic AI Tutor (tutor.py)
Interactive Learning: Instead of giving answers, the AI teaches concepts in small "modules."
Knowledge Validation: After every explanation, the tutor asks a "Check-for-Understanding" question.
Adaptive Feedback: The AI evaluates your answer and either moves forward or re-explains the concept if you are incorrect.
3. 🏗️ Local Knowledge Base (ingest.py)
Private & Secure: All data stays on your machine. No cloud uploads.
Vector Indexing: Uses ChromaDB and HuggingFace embeddings to create a searchable mathematical map of your PDFs.
🛠️ Installation & Setup
1. System Requirements
Ollama: Download & Install
Model: Pull the Gemma 4 model:
ollama pull gemma:2b
2. Python Environment
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate    # Windows

# Install required dependencies
pip install langchain langchain-community langchain-huggingface langchain-text-splitters pypdf chromadb sentence-transformers xhtml2pdf
📂 Project Structure
gemma-study-suite/
├── my_pdfs/             # 📚 INPUT: Place your source PDFs here
├── chroma_db/            # 💾 KNOWLEDGE BASE: Created by ingest.py
├── generated_notes/      # 📄 OUTPUT: Professionally styled PDFs
├── ingest.py            # ⚙️ Step 1: Index your PDFs
├── generate_notes.py     # 🚀 Step 2: Generate structured PDFs
├── tutor.py              # 🎓 Step 3: Start an interactive teaching session
└── README.md
🚀 Workflow Guide
Phase 1: Indexing Your Material
Place your PDFs in the my_pdfs/ folder and run:

python ingest.py
This reads your documents and builds the searchable chroma_db.

Phase 2: Creating Structured Notes
Run the generator script:

python generate_notes.py
Input: Enter topics separated by commas (e.g., "IDA Pro, Web Attacks, RSA Encryption").
Result: A series of professional PDFs in generated_notes/ following the 7-section academic format.
Phase 3: Interactive Learning
Start a tutoring session:

python tutor.py
Process: Pick a topic $\rightarrow$ Read a concept $\rightarrow$ Answer the AI's question $\rightarrow$ Master the topic.
📐 Technical Architecture
Component	Technology	Purpose
LLM	Gemma 4 (via Ollama)	Reasoning, Synthesis, and Tutoring
Vector Store	ChromaDB	Local storage of document embeddings
Embeddings	all-MiniLM-L6-v2	Converting text to numerical vectors
PDF Engine	xhtml2pdf + CSS	Converting AI output to premium PDF layouts
RAG Logic	LangChain	Orchestrating retrieval and prompt flow
Flow: User Query $\rightarrow$ Similarity Search (ChromaDB) $\rightarrow$ Context Injection $\rightarrow$ Gemma 4 (Socratic/Structured Prompt) $\rightarrow$ HTML/CSS Template $\rightarrow$ Final PDF