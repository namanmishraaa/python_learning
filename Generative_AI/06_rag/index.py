"""
This is indexing pipeline to create chunks, setup is done on both ollama and openai api, can uncomment 
"""


from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
load_dotenv()

pdf_path = Path(__file__).parent/"fluent_python.pdf"

# Load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()
# print(docs[12])

#split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(documents=docs)

# Create vector embeddings
# openai_embeddings = OpenAIEmbeddings(
#     model='text-embedding-3-small',
# )


ollama_embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
    base_url="http://localhost:11434/"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=ollama_embeddings,
    url="http://localhost:6333",
    collection_name="learning_rag_ollama"
)

print("Indexing of the document done ....")