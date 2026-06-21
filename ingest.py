from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  # fixed import path
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings            # updated to prevent the next crash

loader = TextLoader("data/knowledge_base.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="vector_store"
)

vector_db.persist()
print("Vector database created successfully!")