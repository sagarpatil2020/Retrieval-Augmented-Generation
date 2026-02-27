import os
import dotenv
 # Load environment variables from .env file

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_qdrant import QdrantVectorStore

dotenv.load_dotenv() 

# Specify the path to the PDF file
pdf_path = Path(__file__).parent / "testing-file.pdf"

# Load the PDF document
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# Split the content of the pages into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents=docs)

#vector embedding for the chunks of text
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", api_key=os.getenv("GEMINI_API_KEY"))

# Create a vector store and add the chunks to it
vector_store = QdrantVectorStore.from_documents(
  documents=chunks,
  embedding=embedding_model,
  url="http://localhost:6333",
  collection_name="pdf_chunks"
)

print("Vector store created and chunks added successfully!")