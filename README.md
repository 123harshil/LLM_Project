# LLM Project with LangChain and Qdrant

This project utilizes [LangChain](https://www.langchain.com/) and [Qdrant](https://qdrant.tech/) to create a document ingestion and querying pipeline for language model-based systems. The pipeline processes and indexes PDF documents, enabling semantic search with embeddings from a Hugging Face model. 

## Table of Contents
1. [Overview](#overview)
2. [Setup and Installation](#setup-and-installation)
3. [Files](#files)
4. [Usage](#usage)
5. [Dependencies](#dependencies)

## Overview
The project contains two main scripts:
1. `ingest.py`: Loads a PDF document, splits its content, generates embeddings, and stores these embeddings in a Qdrant database.
2. `app.py`: Provides an interface to query the database and retrieve relevant chunks of the document based on a given query using semantic similarity search.

## Setup and Installation

To get started, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/LLM-Project.git
   cd LLM-Project
2. Install Necessary Packages
Ensure that you have Python installed (preferably Python 3.8 or later).

bash
Copy code
pip install langchain-community qdrant-client transformers pypdf
3. Set up Qdrant
Qdrant is used as the vector database. You can run Qdrant locally using Docker or download and install it directly.

To start Qdrant with Docker:

bash
Copy code
docker run -p 6333:6333 qdrant/qdrant
Note: Ensure Qdrant is running on http://127.0.0.1:6333 or update the url parameter in both ingest.py and app.py to reflect your Qdrant server's address.

4. Place PDF Document
Place the PDF document (DL.pdf) in the collections directory inside your project folder.

Files
1. ingest.py
This script processes the PDF document and stores its embeddings in the Qdrant vector database.

Workflow
Load the PDF Document: Loaded using PyPDFLoader from LangChain.
Text Splitting: The document content is split into chunks (default: 1000 characters with 50 characters overlap) using RecursiveCharacterTextSplitter.
Generate Embeddings: Each text chunk is transformed into embeddings using the Hugging Face model (BAAI/bge-large-en).
Store in Qdrant: The embeddings are stored in a Qdrant collection (gpt_db).
2. app.py
This script provides an interface to query the database and retrieve the most relevant document chunks based on semantic similarity.

Workflow
Load Embeddings: Initializes the Hugging Face embeddings model.
Connect to Qdrant: Establishes a connection with the Qdrant database.
Search Query: Executes a similarity search based on the input query (example: "What is saliency maps?") and retrieves the top 5 most relevant chunks.
Display Results: Prints each retrieved document chunk along with its similarity score and metadata.
Usage
Running the Ingestion Script
To run the ingestion script:

bash
Copy code
python ingest.py
Running the Query Script
To run the query script:

bash
Copy code
python app.py
Modify the query variable in app.py to customize the query string as desired.

Dependencies
Python (>=3.8)
LangChain-Community: Library for document loaders, text splitters, and Qdrant integrations.
Qdrant-Client: Python client for interacting with the Qdrant database.
HuggingFace Transformers: Embeddings model from Hugging Face to generate vector representations of text.
PyPDF: A Python library to load PDF documents.
