from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from backend.rag.retriever import retriever

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-20b")

prompt = PromptTemplate(
    template="""you are a helpful assistant. answer ONLY from the provided transcript. if the context is insufficent just say you don't know \n
    {context} \n
    Question : {question}""",
    input_variables=['context', 'question']
)

question = "summarize all the discussion in video in 5 key points"
retrieved_doc = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_doc)

final_prompt = prompt.invoke({"context" : context_text, "question" : question})

answer = model.invoke(final_prompt)

print(answer.content)