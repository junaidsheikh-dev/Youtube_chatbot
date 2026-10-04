from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from backend.rag.splitter import documents

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001")

vector_store = FAISS.from_documents(documents, model)

vector_store.index_to_docstore_id

print("Number of vectors:", vector_store.index.ntotal)
print("Vector dimension:", vector_store.index.d)
