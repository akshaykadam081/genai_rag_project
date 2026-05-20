******************************* GenAI RAG Chatbot ********************

I built this project to understand how a real-world Retrieval-Augmented Generation (RAG) system works end-to-end — from raw data to an interactive chatbot UI.
It combines document processing, vector search, and LLM-based answering using Groq.

* What this project does
Cleans and prepares raw text data for processing
Splits documents into meaningful chunks for better retrieval
Generates embeddings using SentenceTransformers
Stores and searches vectors using ChromaDB
Finds the most relevant context using similarity search
Uses Groq Llama3 to generate intelligent responses
Provides a simple chatbot UI using Gradio

* Key Concepts Learned
While building this, I worked through:
- Data preprocessing pipelines
- Text chunking strategies for RAG
- Vector embeddings and semantic search
- Building and querying vector databases
- Connecting retrieval systems with LLMs
- Deploying a chatbot-style interface

* How to run this project
1. Clone the repository:
   !git clone https://github.com/your-username/genai_rag_project.git
   %cd genai_rag_project
2. Install dependencies:
   !pip install -r requirements.txt
3. Add your Groq API key:
   # config.py
  GROQ_API_KEY = "your_api_key_here"
4. Run the app:
  !python app.py
