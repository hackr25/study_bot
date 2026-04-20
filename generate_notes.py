import os
import re
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

# --- Configuration ---
DB_PATH = "./chroma_db"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gemma4:e2b" 
OUTPUT_FOLDER = "./generated_notes"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# --- YOUR EXACT STRUCTURE TEMPLATE ---
STRUCTURE_TEMPLATE = """
You must organize the notes using the following 7 sections EXACTLY. 
Do not skip any section. If the provided context doesn't have enough information for a section, use your general knowledge to fill it, but keep the section header.

1. Introduction
   - Definition of the topic
   - Purpose and core objective
   - Primary conversion/function (e.g., X to Y)

2. Working / Process
   - Step-by-step mechanism
   - Internal representations or methodologies
   - Core operational flow

3. Key Features
   - List of essential tools/capabilities
   - Specific technical components
   - Unique identifiers or analysis capabilities

4. Comparison / Analysis (e.g., Static vs Dynamic, or A vs B)
   - Contrast the primary approach with an alternative
   - Pros and cons of the current method
   - Context of when to use which

5. Advantages
   - Why is this tool/method used?
   - Specific benefits in industry or academia
   - Support and compatibility

6. Limitations
   - What are the weaknesses?
   - Common failure points or difficulties
   - Required expertise level

7. Conclusion
   - Summary of its importance
   - Industry status
   - Final verdict on its utility
"""

class PDFStylist:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        # Main Title
        self.styles.add(ParagraphStyle(name='CustomMainTitle', fontName='Helvetica-Bold', fontSize=22, textColor=colors.darkblue, alignment=TA_CENTER, spaceAfter=20))
        # Section Headers (1. Introduction, etc)
        self.styles.add(ParagraphStyle(name='CustomSectionHeader', fontName='Helvetica-Bold', fontSize=14, textColor=colors.darkred, spaceBefore=15, spaceAfter=10))
        # Body Text
        self.styles.add(ParagraphStyle(name='CustomBodyText', fontName='Helvetica', fontSize=11, textColor=colors.black, alignment=TA_JUSTIFY, leading=14, spaceAfter=10))
        # Meta Data
        self.styles.add(ParagraphStyle(name='CustomMetaData', fontName='Helvetica-Oblique', fontSize=10, textColor=colors.grey, alignment=TA_CENTER, spaceAfter=20))

def format_markdown_to_pdf(text):
    """
    Converts Markdown into ReportLab XML tags.
    **Bold** -> <b>Bold</b>
    """
    # Replace **Bold** with <b>Bold</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    return text

def generate_combined_notes():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    if not os.path.exists(DB_PATH):
        print("Error: Run ingest.py first!")
        return
    
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    llm = OllamaLLM(model=LLM_MODEL)

    print("\n--- 📝 Blueprint Structured Note Builder ---")
    questions_input = input("Enter the topics/questions (separated by commas): ")
    questions = [q.strip() for q in questions_input.split(",")]

    # Single output file for all notes
    output_file = os.path.join(OUTPUT_FOLDER, "Combined_Study_Notes.pdf")
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    stylist = PDFStylist()
    story = []

    for query in questions:
        print(f"\n🚀 Building Blueprint for: {query}...")
        docs = vectorstore.similarity_search(query, k=5)
        context = "\n\n---\n\n".join([doc.page_content for doc in docs])

        # The prompt now includes your exact template as a mandatory requirement
        prompt = f"""
        You are an expert academic writer. Create a highly structured study guide.
        
        MANDATORY FORMATTING:
        You must follow this blueprint EXACTLY. Do not change the headings.
        {STRUCTURE_TEMPLATE}
        
        CONTEXT:
        {context}
        
        TOPIC: {query}
        
        Write the notes now. Use bullet points for lists. 
        IMPORTANT: Use **Bold** for key terms.
        """

        response = llm.invoke(prompt)
        
        # Add Topic Header
        story.append(Paragraph(format_markdown_to_pdf(f"TOPIC: {query}"), stylist.styles['CustomMainTitle']))
        story.append(Spacer(1, 12))

        # Process the response line by line
        lines = response.split("\n")
        for line in lines:
            line = line.strip()
            if not line: continue
            
            formatted_line = format_markdown_to_pdf(line)
            
            # Detect Section Headers (e.g., "1. Introduction")
            if any(line.startswith(f"{i}.") for i in range(1, 8)):
                story.append(Paragraph(formatted_line, stylist.styles['CustomSectionHeader']))
            # Detect Bullet Points
            elif line.startswith("- ") or line.startswith("* "):
                story.append(Paragraph(f"• {formatted_line[2:]}", stylist.styles['CustomBodyText']))
            # Regular Paragraphs
            else:
                story.append(Paragraph(formatted_line, stylist.styles['CustomBodyText']))
        
        story.append(Spacer(1, 30)) # Separator between different topics

    doc.build(story)
    print(f"\n✅ All blueprint notes combined and saved to: {output_file}")

if __name__ == "__main__":
    generate_combined_notes()
