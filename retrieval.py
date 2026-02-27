import os
import dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

dotenv.load_dotenv()

openai_client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"),
                       base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", api_key=os.getenv("GEMINI_API_KEY"))


vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="pdf_chunks",
    embedding=embedding_model,
)

# take user query and convert it to vector embedding
user_query = input("Enter your query: ")


# perform similarity search in the vector database to retrieve relevant chunks of text
search_result = vector_db.similarity_search(query=user_query, k=3)

context = "\n\n\n".join(
    [f"Chunk {i+1}:\nFile location: {result.metadata['source']}\nContent: {result.page_content}" for i, result in enumerate(search_result)])


SYSTEM_PROMPT = """You are a helpful assistant that provides answers based on the retrieved chunks of text from the PDF document. 
Use the following retrieved chunks to answer the user's query. If the information is not available in the chunks
context:{context}"""

response = openai_client.chat.completions.create(
    model="models/gemini-2.0-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ],
    temperature=0.5,
)

print("Answer:", response.choices[0].message.content)