import gradio as gr

from config import DATA_PATH
from processor import (
    extract_zip,
    load_documents,
    chunk_documents
)
from embeddings import create_embeddings
from vector_store import store_chunks
from retriever import retrieve_context
from llm_service import ask_llm


print("Preparing vector database...")

folder = extract_zip(DATA_PATH)

docs = load_documents(folder)

chunks = chunk_documents(docs)

embeddings = create_embeddings(chunks)

store_chunks(chunks, embeddings)

print("Ready.")


def chatbot(question, history):

    context = retrieve_context(question)

    answer = ask_llm(
        question,
        context
    )

    history.append(
        (question, answer)
    )

    return "", history


with gr.Blocks() as demo:

    gr.Markdown(
        "# News Article RAG Chatbot"
    )

    chatbot_ui = gr.Chatbot()

    msg = gr.Textbox(
        placeholder="Ask anything..."
    )

    state = gr.State([])

    msg.submit(
        chatbot,
        inputs=[msg, state],
        outputs=[msg, chatbot_ui]
    )


demo.launch(share=True)