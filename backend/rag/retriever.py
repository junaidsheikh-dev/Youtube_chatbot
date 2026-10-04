from backend.rag.vector_embedding import get_vector_store

video_id = "h3M00JI8Iwo"

vector_store = get_vector_store(video_id)

retriever = vector_store.as_retriever(search_type='similarity', search_kwargs = {'k' : 4})