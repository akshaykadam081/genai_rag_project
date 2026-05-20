import chromadb

from config import CHROMA_PATH

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    name="news_articles"
)


def store_chunks(chunks, embeddings):

    ids = []

    for i in range(len(chunks)):
        ids.append(str(i))

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )


def search(query_embedding, k=3):

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=k
    )

    return results["documents"][0]