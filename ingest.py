import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
PDF_FOLDER = "./my_pdfs/"  # Make sure this folder exists and has PDFs
DB_PATH = "./chroma_db"    # This is where your database will be saved
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def main():
    # 1. Initialize Embedding Model
    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # 2. Process PDFs
    all_documents = []
    if not os.path.exists(PDF_FOLDER):
        print(f"Error: The folder {PDF_FOLDER} does not exist. Please create it.")
        return

    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith('.pdf'):
            file_path = os.path.join(PDF_FOLDER, filename)
            print(f"Processing: {filename}...")
            try:
                loader = PyPDFLoader(file_path)
                documents = loader.load()
                
                # Split the text into smaller chunks
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000, 
                    chunk_overlap=200
                )
                chunks = text_splitter.split_documents(documents)
                all_documents.extend(chunks)
            except Exception as e:
                print(f"Could not read {filename}: {e}")

    if all_documents:
        # 3. Create and Save Vector Store
        print(f"Creating vector store with {len(all_documents)} chunks...")
        vectorstore = Chroma.from_documents(
            documents=all_documents, 
            embedding=embeddings, 
            persist_directory=DB_PATH
        )
        print(f"✅ Success! Database saved in {DB_PATH}")
    else:
        print("❌ No PDF content found. Check your my_pdfs folder.")

if __name__ == "__main__":
    main()
