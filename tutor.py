import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_JUSTIFY

# --- Configuration ---
DB_PATH = "./chroma_db"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gemma:2b" 
OUTPUT_FOLDER = "./generated_notes"

if not os.path.exists(OUTPUT_FOLDER): os.makedirs(OUTPUT_FOLDER)

def save_session_to_pdf(history, filename="Tutor_Session.pdf"):
    doc = SimpleDocTemplate(os.path.join(OUTPUT_FOLDER, filename), pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TutorStyle', fontName='Helvetica-Bold', fontSize=12, textColor=colors.darkblue, spaceBefore=10))
    styles.add(ParagraphStyle(name='UserStyle', fontName='Helvetica-Oblique', fontSize=12, textColor=colors.black, spaceBefore=5))
    
    story = []
    story.append(Paragraph("Tutor Session Transcript", styles['Title']))
    
    for entry in history:
        if entry['role'] == 'tutor':
            story.append(Paragraph(f"<b>Tutor:</b> {entry['text']}", styles['TutorStyle']))
        else:
            story.append(Paragraph(f"<i>User:</i> {entry['text']}", styles['UserStyle']))
        story.append(Spacer(1, 6))
    
    doc.build(story)
    print(f"\n✅ Session saved to: {filename}")

def start_tutor_session():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    if not os.path.exists(DB_PATH): return
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    llm = OllamaLLM(model=LLM_MODEL)

    print("\n🎓 WELCOME TO THE AI TUTOR 🎓")
    topics_input = input("Which topics should I scan and teach you? (separated by commas): ")
    topics = [t.strip() for t in topics_input.split(",")]
    
    session_history = []
    
    for topic in topics:
        print(f"\n--- Switching to Topic: {topic} ---")
        docs = vectorstore.similarity_search(topic, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        system_persona = f"You are a Socratic Tutor. Teach {topic} using this context: {context}. Explain one concept, then ask a question. Wait for the answer before moving on."
        
        chat_history = ""
        current_prompt = system_persona + "\n\nStart by introducing the topic."
        
        while True:
            response = llm.invoke(current_prompt + "\n\nHistory:\n" + chat_history)
            print(f"\n👨‍🏫 Tutor: {response}")
            
            session_history.append({'role': 'tutor', 'text': response})
            
            user_input = input("\nYour Answer (or 'next' to move topic, 'exit' to quit): ")
            session_history.append({'role': 'user', 'text': user_input})
            
            if user_input.lower() == 'exit': 
                save_session_to_pdf()
                return
            if user_input.lower() == 'next': 
                break
                
            chat_history += f"\nTutor: {response}\nUser: {user_input}"
            current_prompt = f"{system_persona}\n\nEvaluate the user's answer and move to the next concept if correct."

    save_session_to_pdf()

if __name__ == "__main__":
    start_tutor_session()
