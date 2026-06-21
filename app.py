import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory        
from langchain_classic.chains import ConversationalRetrievalChain    
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.memory import ConversationBufferMemory

load_dotenv()

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖"
)

st.title("Context-Aware RAG Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="vector_store",
    embedding_function=embeddings
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatOpenAI(
    temperature=0
)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

user_question = st.text_input(
    "Ask a question:"
)

if user_question:
    result = qa_chain.invoke(
        {"question": user_question}
    )
    answer = result["answer"]

    st.session_state.chat_history.append(
        ("You", user_question)
    )
    st.session_state.chat_history.append(
        ("Bot", answer)
    )

for sender, msg in st.session_state.chat_history:
    st.write(f"**{sender}:** {msg}")