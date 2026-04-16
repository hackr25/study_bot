import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

# --- Configuration ---
DB_PATH = "./chroma_db"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gemma4:e2b" 

def start_tutor_session():
    # 1. Initialize RAG Components
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    if not os.path.exists(DB_PATH):
        print("Error: Database not found. Please run ingest.py first!")
        return
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    llm = Ollama(model=LLM_MODEL)

    print("\n" + "="*50)
    print("🎓 WELCOME TO YOUR AI PERSONAL TUTOR 🎓")
    print("I will teach you based on your PDFs using the Socratic Method.")
    print("I'll explain a concept, then ask you a question to test your knowledge.")
    print("Type 'exit' to end the session.")
    print("="*50)

    topic = input("\nWhat topic would you like to learn today? ")
    
    # Initial retrieval of the whole topic context
    docs = vectorstore.similarity_search(topic, k=5)
    full_context = "\n\n---\n\n".join([doc.page_content for doc in docs])

    # System Prompt to define the "Tutor Persona"
    system_persona = f"""
    You are a patient and brilliant Socratic Tutor. Your goal is to teach the user the following topic: {topic}.
    
    RULES FOR TEACHING:
    1. DO NOT dump all the information at once. 
    2. Break the topic into small, digestible "Learning Modules".
    3. Explain ONE concept clearly using the provided context.
    4. After the explanation, ask the user a targeted "Check-for-Understanding" question.
    5. Wait for the user's answer. 
    6. If the user is correct, praise them and move to the next concept.
    7. If the user is wrong, gently correct them and re-explain the concept in a different way.
    8. Always stay strictly based on the provided context.

    CONTEXT FOR TEACHING:
    {full_context}
    """

    # Initial state
    current_prompt = system_persona + "\n\nStart the session by introducing the topic briefly and explaining the first core concept. Then ask me the first question."
    
    chat_history = "" # To keep track of the conversation

    while True:
        # Get response from Gemma 4
        response = llm.invoke(current_prompt + "\n\nChat History:\n" + chat_history)
        
        print("\n\n--- 👨‍🏫 TUTOR ---")
        print(response)
        print("\n" + "-"*20)
        
        user_input = input("\nYour Answer: ")
        
        if user_input.lower() == 'exit':
            print("\nGreat job today! Keep studying. Goodbye! 👋")
            break
        
        # Update chat history and create the next prompt
        chat_history += f"\nTutor: {response}\nUser: {user_input}"
        
        # The prompt for the next turn focuses on evaluating the user's answer
        current_prompt = f"""
        {system_persona}
        
        The user has just answered your question. 
        1. Evaluate if their answer is correct based on the context.
        2. Provide feedback (Correct/Incorrect).
        3. If correct, move to the next sub-topic or concept.
        4. If incorrect, re-explain and ask the question again.
        
        Remember: keep explanations short and always end with a question.
        """

if __name__ == "__main__":
    start_tutor_session()
