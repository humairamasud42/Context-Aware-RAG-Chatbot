# 🤖 Context-Aware RAG Chatbot (LangChain + Streamlit)

A **Retrieval-Augmented Generation chatbot** that uses LangChain, vector databases, LLMs to answer questions based on custom documents and maintains conversational memory.

---

## 🚀 Project Overview

This project demonstrates how to build a **smart AI chatbot** that:

- Retrieves relevant information from a custom knowledge base
- Maintains conversation context (memory)
- Uses vector embeddings for semantic search
- Generates intelligent responses using an LLM
- Runs as a web app using Streamlit

---

## 🎯 Features

- 📄 Document-based question answering (RAG)
- 🧠 Conversational memory support
- 🔍 Semantic search using vector embeddings
- ⚡ Fast retrieval with ChromaDB
- 🤖 LLM-powered responses (OpenAI / compatible models)
- 🌐 Interactive Streamlit UI

---

## 🧠 Tech Stack

- Python
- LangChain
- ChromaDB (Vector Database)
- Sentence Transformers
- Streamlit
- OpenAI API / LLMs
- Python-dotenv

---

## 📁 Project Structure

```text
rag-chatbot/
│
├── data/
│   └── knowledge_base.txt     # Custom dataset / documents
│
├── vector_store/              # Stored embeddings (ChromaDB)
│
├── ingest.py                  # Creates embeddings & vector DB
├── app.py                     # Streamlit chatbot app
├── requirements.txt           # Project dependencies
├── .env                       # API keys
└── README.md
```

## 💬 How It Works
User adds documents (knowledge base)
Text is split into chunks
Embeddings are created using Sentence Transformers
Stored in ChromaDB vector database
User query is embedded and matched with relevant chunks
LLM generates final response using retrieved context

## 🧪 Example Questions
What is AI?
Explain Machine Learning.
What did we discuss earlier?
How does deep learning work?
The chatbot can:

✅ Remember conversation

✅ Retrieve documents

✅ Use vector search

✅ Generate contextual responses

## Expected Output
User:
What is AI?

Bot:
Artificial Intelligence is the simulation of human intelligence by machines.

User:
What is machine learning?

Bot:
Machine Learning is a subset of Artificial Intelligence that enables systems to learn from data.

---

## 📌 Key Concepts Learned
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- Conversational AI
- LangChain framework
- Streamlit deployment

## 🔮 Future Improvements
- Upload PDF files directly
- Multi-document chat support
- Voice-enabled chatbot
- Chat history export
- Advanced memory systems
- Hybrid search (keyword + vector)
