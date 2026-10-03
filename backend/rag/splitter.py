from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.youtube.transcript import get_transcript

transcript = get_transcript("eIho2S0ZahI")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

chunks = splitter.split_text(transcript)

print(chunks)