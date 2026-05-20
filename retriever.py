from embeddings import create_embeddings
from vector_store import search


def retrieve_context(question):

    query_embedding = create_embeddings(
        [question]
    )

    docs = search(query_embedding)

    context = "\n".join(docs)

    return context