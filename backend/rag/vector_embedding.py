import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from backend.rag.splitter import create_documents

load_dotenv()


def get_vector_store(video_id):

    model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")

    path = f"vector_stores/{video_id}"

    if os.path.exists(path):
        vector_store = FAISS.load_local(
            path,
            model,
            allow_dangerous_deserialization=True
        )
    else:
        documents = create_documents(video_id)

        vector_store = FAISS.from_documents(documents, model)

        vector_store.save_local(path)

    return vector_store