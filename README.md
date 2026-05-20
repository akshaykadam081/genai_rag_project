******************************* GenAI RAG Chatbot ********************

I built this project to understand how a real-world Retrieval-Augmented Generation (RAG) system works end-to-end — from raw data to an interactive chatbot UI.
It combines document processing, vector search, and LLM-based answering using Groq. The main entry point of the project is app.py, and I have separated the logic into different files to keep things simple and organized while I was learning.
For example, cleaner.py handles data cleaning and preprocessing, llm_service.py is responsible for calling the Groq LLM APIs, and vector_store.py manages storing and retrieving embeddings using the vector database. Each file has a small and clear responsibility, which helped me understand how a full RAG pipeline is built step by step.

**** What this project does ***
- Cleans and prepares raw text data for processing
- Splits documents into meaningful chunks for better retrieval
- Generates embeddings using SentenceTransformers
- Stores and searches vectors using ChromaDB
- Finds the most relevant context using similarity search
- Uses Groq Llama3 to generate intelligent responses
- Provides a simple chatbot UI using Gradio

*** Project Flow (File-wise Execution) ***
1. app.py → Starts Gradio UI, takes user input, and connects frontend to backend chatbot flow  
2. chatbot() (app.py) → Receives query and coordinates retrieval + LLM response generation  
3. llm_service.py → Builds prompt, adds context, and calls Groq Llama3 API for response generation  
4. retriever.py / vectorstore.py → Performs similarity search on stored embeddings to fetch relevant chunks  
5. SentenceTransformer (embeddings module) → Converts text (documents + queries) into vector embeddings  
6. ChromaDB → Stores embeddings and returns most similar document chunks based on query  
7. data preprocessing / chunking file → Cleans raw text and splits it into smaller chunks for embedding  
8. config.py → Stores API keys and configuration settings like Groq API key  

*** How to run this project ***
1. Clone the repository:
   !git clone https://github.com/your-username/genai_rag_project.git
   %cd genai_rag_project
2. Install dependencies:
   !pip install -r requirements.txt
3. Add your Groq API key:
   - edit config.py
    GROQ_API_KEY = "your_api_key_here"
4. Run the app:
  !python app.py
