import zipfile
import os

from cleaner import clean_text
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)


def extract_zip(zip_path):

    extract_folder = "data/extracted"

    if not os.path.exists(extract_folder):
        os.makedirs(extract_folder)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    return extract_folder


def load_documents(folder):

    docs = []

    for root, dirs, files in os.walk(folder):

        for file in files:

            if file.endswith(".txt"):

                path = os.path.join(root, file)

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    text = f.read()

                    cleaned = clean_text(text)

                    docs.append(cleaned)

    return docs


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for doc in documents:
        pieces = splitter.split_text(doc)
        chunks.extend(pieces)

    return chunks