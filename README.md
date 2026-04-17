🎓 Gemma Study Suite
Local AI Academic Ecosystem

A privacy-focused academic toolkit that transforms raw PDFs (textbooks, question papers, lecture notes) into professional study guides and interactive tutoring sessions.

Powered by Gemma 4 (via Ollama) and a local RAG (Retrieval-Augmented Generation) pipeline.

🌟 Key Features
1. 📄 Professional Note Architect (generate_notes.py)
🔹 Structured Academic Format

Every generated note follows a strict 7-section format:

Introduction → Working → Key Features → Analysis → Advantages → Limitations → Conclusion
🔹 Premium PDF Styling
HTML/CSS-based rendering
Textbook-quality layout
Color-coded headers
Professional typography
Meta-information boxes
🔹 Batch Processing
Generate notes for multiple topics/questions in one run
🔹 Weightage-Aware Content
Adjusts depth automatically for:
2 marks
5 marks
10 marks
2. 👨‍🏫 Socratic AI Tutor (tutor.py)
🔹 Interactive Learning Model
Teaches concepts in small modules
Avoids direct answers
🔹 Knowledge Validation
After each explanation → asks Check-for-Understanding questions
🔹 Adaptive Feedback
Evaluates your response
Re-explains if incorrect
Progresses if correct
3. 🏗️ Local Knowledge Base (ingest.py)
🔹 Privacy First
Fully offline system
No cloud uploads
🔹 Vector Indexing
Uses:
ChromaDB
HuggingFace embeddings
Builds a searchable semantic map of PDFs
🛠️ Installation & Setup
1. System Requirements
Install Ollama

Download and install from official source.

Pull Gemma Model
ollama pull gemma:2b
2. Python Environment Setup
# Create virtual environment
python -m venv venv

# Activate environment
# Linux/macOS
source venv/bin/activate  

# Windows
.\venv\Scripts\activate
Install Dependencies
pip install langchain langchain-community langchain-huggingface \
langchain-text-splitters pypdf chromadb sentence-transformers xhtml2pdf
📂 Project Structure
gemma-study-suite/
├── my_pdfs/              # 📚 INPUT: Source PDFs
├── chroma_db/           # 💾 Knowledge base (generated)
├── generated_notes/     # 📄 Output PDFs
├── ingest.py            # ⚙️ Step 1: Index PDFs
├── generate_notes.py    # 🚀 Step 2: Generate notes
├── tutor.py             # 🎓 Step 3: Interactive tutor
└── README.md
🚀 Workflow Guide
🔹 Phase 1: Indexing Your Material
Place PDFs inside:
my_pdfs/
Run:
python ingest.py

👉 This builds the ChromaDB vector database

🔹 Phase 2: Generating Structured Notes

Run:

python generate_notes.py
Input Example:
IDA Pro, Web Attacks, RSA Encryption
Output:
Professionally formatted PDFs in:
generated_notes/
🔹 Phase 3: Interactive Learning

Run:

python tutor.py
Flow:
Select Topic → Learn Concept → Answer Questions → Get Feedback → Master Topic
📐 Technical Architecture
Component	Technology	Purpose
LLM	Gemma 4 (Ollama)	Reasoning & tutoring
Vector Store	ChromaDB	Store embeddings
Embeddings	all-MiniLM-L6-v2	Text → vector conversion
PDF Engine	xhtml2pdf + CSS	Styled PDF generation
RAG Pipeline	LangChain	Retrieval + prompt flow
🔁 System Flow
User Query 
   → Similarity Search (ChromaDB)
   → Context Injection
   → Gemma 4 (Structured/Socratic Prompt)
   → HTML/CSS Template
   → Final PDF Output
🔐 Key Advantages
100% offline & private
Structured exam-ready notes
Interactive learning system
Modular & scalable architecture
No dependency on external APIs
📌 Use Cases
📚 Exam preparation
🧠 Concept mastery
📄 Automated note generation
🎓 Self-paced learning