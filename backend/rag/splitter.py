from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.youtube.transcript import get_transcript

def create_documents(video_id):

    transcript = get_transcript(video_id)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

    return splitter.create_documents([transcript])

