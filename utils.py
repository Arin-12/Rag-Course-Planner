from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load data
def load_docs(urls):
    loader = WebBaseLoader(urls)
    return loader.load()

# Split
def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(docs)

# Embeddings
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

# Vector store
def create_db(chunks, embeddings):
    return FAISS.from_documents(chunks, embeddings)

# Retriever
def get_retriever(db):
    return db.as_retriever(search_kwargs={"k": 5})