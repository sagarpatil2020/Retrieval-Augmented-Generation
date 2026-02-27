RAG-Project

This project demonstrates a Retrieval-Augmented Generation (RAG) system using Google Gemini for embeddings and Qdrant for vector storage. The system retrieves relevant chunks of text from a PDF document based on user queries and generates answers using the retrieved information.

STEP 1: Set Up Environment
1. Clone the repository and navigate to the project directory.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

STEP 2: Configure API Key
1. Create a `.env` file in the project root directory and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key
   ```
STEP 3: Run the Retrieval System
1. Run the `retrieval.py` script:
   ```bash
   python retrieval.py
   ```
2. Enter your query when prompted. The system will retrieve relevant chunks from the PDF document and generate an answer using the retrieved information.
Note: Ensure that you have the necessary permissions and access to the Google Gemini API and Qdrant vector store for the system to function correctly.

STEP 4: Test the System
1. Test the system by entering different queries related to the content of the PDF document.
2. Observe the system's ability to retrieve relevant chunks and generate accurate answers based on the retrieved information.


# RAG-PIPELINE 
INDEXING - 
1. The PDF document is split into smaller chunks of text.
2. Each chunk is converted into a vector representation using the Google Gemini embedding model.
3. The vectors are stored in a Qdrant vector store for efficient retrieval.
RETRIEVAL -
1. When a user query is received, it is also converted into a vector using the same embedding model.
2. The vector store is queried to retrieve the most relevant chunks of text based on cosine similarity.
ANSWER GENERATION -
1. The retrieved chunks of text are used as context to generate an answer to the user's query.
