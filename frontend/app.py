import streamlit as st
from urllib.parse import urlparse, parse_qs
from backend.main import get_answer


st.title("YouTube Chatbot")

video_url = st.text_input("Enter YouTube URL")

question = st.text_input("Ask a question about the video")

def get_video_id(url):
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query).get("v", [None])[0]


if st.button("Ask"):
    video_id = get_video_id(video_url)

    answer = get_answer(question, video_id)

    # st.write("Vector store loaded successfully!")

    st.write(answer)
    

