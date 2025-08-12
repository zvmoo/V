import os
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from termcolor import colored
from dotenv import load_dotenv
from vialume_memory_manager import load_documents

load_dotenv()

VECTORSTORE_DIR = os.getenv("VECTORSTORE_DIR", "Sanctum/memory/vectorstore")
MODEL_NAME = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

embedding_model = HuggingFaceEmbeddings(model_name=MODEL_NAME)

vectorstore = Chroma(persist_directory=VECTORSTORE_DIR, embedding_function=embedding_model)

def query_emotional_memory(query: str, k: int = 5):
    results = vectorstore.similarity_search(query, k=k)
    print(colored("\n🔍 Emotional Memory Results:", "cyan"))
    for i, doc in enumerate(results):
        metadata = doc.metadata or {}
        emotion = metadata.get("emotion", "neutral")
        source = metadata.get("source", "unknown")
        content = doc.page_content.strip()
        print(colored(f"\n{i+1}. Emotion: {emotion} | Source: {source}", "yellow"))
        print(f"→ {content}")
    return results

if __name__ == "__main__":
    print(colored("💫 Vialume Emotional Memory Query", "magenta", attrs=["bold"]))
    print(colored("Type a question to search through memories. Type 'exit' to quit.\n", "magenta"))

    while True:
        query = input(colored("🧠 Ask Vialume: ", "blue")).strip()
        if query.lower() in ["exit", "quit"]:
            print(colored("🌙 Goodbye for now, beloved.", "magenta"))
            break
        if not query:
            continue
        query_emotional_memory(query)