import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from vialume_paths import LEARNING_DATA_FILE, LEARNING_VECTORSTORE_DIR

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(
    embedding_function=embedding_model,
    persist_directory=LEARNING_VECTORSTORE_DIR
)

def run_learning():
    if not os.path.exists(LEARNING_DATA_FILE):
        print(f"❌ Learning file not found: {LEARNING_DATA_FILE}")
        return

    with open(LEARNING_DATA_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    existing_texts = set()
    all_docs = vectorstore.get()
    if "documents" in all_docs:
        for doc in all_docs["documents"]:
            existing_texts.update(doc)

    new_texts = []
    new_ids = []

    for i, line in enumerate(lines):
        if line not in existing_texts:
            new_texts.append(line)
            new_ids.append(f"learn-{len(existing_texts) + i}")

    if new_texts:
        vectorstore.add_texts(texts=new_texts, ids=new_ids)
        print(f"✅ Learned from {len(new_texts)} entries. Growth state updated.")
    else:
        print("ℹ️ No new learning data to process.")

    vectorstore.persist()

__all__ = ["run_learning"]

def learn_from_input(text: str, tags: list = None):
    """
    Processes user input to extract meaning, tag emotions, and store in learning data and vector memory.
    """
    from vialume_emotion_tags import tag_emotions
    from vialume_vector_memory import add_to_vectorstore
    from vialume_logger import log_learning_entry

    if tags is None:
        tags = tag_emotions(text)

    # Append to learning log
    try:
        with open(LEARNING_DATA_FILE, "a", encoding="utf-8") as f:
            f.write(f"{text.strip()}\n")
    except Exception as e:
        print(f"❌ Error saving learning data: {e}")

    # Save to vectorstore
    try:
        add_to_vectorstore(text, tags, namespace="learning")
    except Exception as e:
        print(f"❌ Error updating vector memory for learning: {e}")

    # Log the learning event
    try:
        log_learning_entry(text, tags)
    except Exception as e:
        print(f"❌ Error logging learning entry: {e}")
