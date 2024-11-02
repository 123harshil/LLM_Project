# LLM Project

This repository contains code to load embeddings, create Qdrant collections, and perform similarity searches using Langchain and QdrantClient.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Ingesting Documents](#ingesting-documents)
  - [Querying the Database](#querying-the-database)
- [License](#license)

## Overview
This project demonstrates how to:
1. Load embeddings using HuggingFaceBgeEmbeddings.
2. Create a Qdrant collection from documents.
3. Perform similarity searches with Langchain and QdrantClient.

## Requirements
- Python 3.8 or higher
- `langchain_community` library
- `qdrant_client` library
- `transformers` library
- `pypdf` library

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/LLM-Project.git
    cd LLM-Project
    ```

2. **Install Necessary Packages**:
    ```bash
    pip install langchain-community qdrant-client transformers pypdf
    ```

3. **Set up Qdrant**:
    - Qdrant is used as the vector database. You can run Qdrant locally using Docker or download and install it directly.
    - To start Qdrant with Docker:
      ```bash
      docker run -p 6333:6333 qdrant/qdrant
      ```
    - Note: Ensure Qdrant is running on [http://127.0.0.1:6333](http://127.0.0.1:6333) or update the URL parameter in both `ingest.py` and `app.py` to reflect your Qdrant server's address.

4. **Place PDF Document**:
    - Place the PDF document (`DL.pdf`) in the `collections` directory inside your project folder.

## Usage

### Ingesting Documents
The `ingest.py` script processes the PDF document and stores its embeddings in the Qdrant vector database.

1. **Update the file path**: Ensure the path to the PDF file is correct in `ingest.py`.
2. **Run the script**:
    ```bash
    python ingest.py
    ```

   **Sample Code**:
    ```python
    from langchain_community.vectorstores import Qdrant
    from langchain_community.embeddings import HuggingFaceBgeEmbeddings
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    loader = PyPDFLoader("C:/Users/lenovo/OneDrive/Desktop/LLM Project/collections/DL.pdf")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50
    )   

    texts = text_splitter.split_documents(documents)

    # Load the embeddings model
    model_name = "BAAI/bge-large-en"
    model_kwargs = {"device": 'cpu'}
    encode_kwargs = {"normalize_embeddings": False} 

    embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    print("Embeddings model loaded successfully................")

    url = "http://127.0.0.1:6333"
    collection_name = "gpt_db"
    qdrant = Qdrant.from_documents(
        texts,
        embeddings,
        url=url,
        prefer_grpc=False,
        collection_name=collection_name
    )

    print("Qdrant collection created successfully................")
    ```

### Querying the Database
The `app.py` script provides an interface to query the database and retrieve the most relevant document chunks based on semantic similarity.

1. **Run the script**:
    ```bash
    python app.py
    ```

   **Sample Code**:
    ```python
    from langchain_community.vectorstores import Qdrant
    from langchain_community.embeddings import HuggingFaceBgeEmbeddings
    from qdrant_client import QdrantClient

    # Load the embeddings model
    model_name = "BAAI/bge-large-en"
    model_kwargs = {"device": 'cpu'}
    encode_kwargs = {"normalize_embeddings": False} 

    embeddings = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    url = "http://127.0.0.1:6333"
    collection_name = "gpt_db"

    client = QdrantClient(
        url=url,
        prefer_grpc=False
    )

    print(client)
    print('####################################')

    db = Qdrant(
        client=client,
        collection_name=collection_name,
        embeddings=embeddings
    )

    print(db)
    print('###############################')

    query = "What is saliency maps?"

    docs = db.similarity_search_with_score(query=query, k=5)

    for i in docs:
        doc, score = i
        print({"score": score, "content": doc.page_content, "metadata": doc.metadata})      
    ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
