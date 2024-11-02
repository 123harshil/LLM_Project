# LLM_Project

This project utilizes LangChain and Qdrant to create a simple document ingestion and querying pipeline for a language model-based system. The pipeline is designed to process and index PDF documents, enabling semantic search through embeddings from a Hugging Face model.

Table of Contents
Overview
Setup and Installation
Files
Usage
Dependencies
Overview
The project consists of two main scripts:

ingest.py: Responsible for loading a PDF document, splitting its content into manageable chunks, generating embeddings for each chunk, and storing these embeddings in a Qdrant database.
app.py: A querying interface that retrieves relevant chunks of the document based on a given input query, using semantic similarity search on the Qdrant database.
Setup and Installation
To get started, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/LLM-Project.git
cd LLM-Project
Install the necessary Python packages: Ensure that you have Python installed (preferably Python 3.8 or later).

bash
Copy code
pip install langchain-community qdrant-client transformers pypdf
Set up Qdrant: Qdrant is used as the vector database. You can run Qdrant locally using Docker or download and install it directly.

To start Qdrant with Docker:

bash
Copy code
docker run -p 6333:6333 qdrant/qdrant
Note: Make sure Qdrant is running on http://127.0.0.1:6333 or update the url parameter in both ingest.py and app.py to reflect your Qdrant server's address.

Download the Document: Place the PDF document (DL.pdf) in the directory collections inside your project folder.

Files
1. ingest.py
This script is responsible for processing the PDF document and storing its embeddings in the Qdrant vector database.

Workflow
Load the PDF Document: The document is loaded using the PyPDFLoader from LangChain.
Text Splitting: The document content is split into chunks (default: 1000 characters with 50 characters overlap) using RecursiveCharacterTextSplitter.
Generate Embeddings: Each text chunk is transformed into embeddings using the Hugging Face model (BAAI/bge-large-en).
Store in Qdrant: The embeddings are stored in a Qdrant collection (gpt_db).
Usage
To run the ingestion script:

bash
Copy code
python ingest.py
2. app.py
This script provides an interface to query the database and retrieve the most relevant document chunks based on semantic similarity.

Workflow
Load Embeddings: Initializes the Hugging Face embeddings model, which will be used for query embedding.
Connect to Qdrant: Establishes a connection with the Qdrant database.
Search Query: Executes a similarity search based on the input query (example: "What is saliency maps?") and retrieves the top 5 most relevant chunks.
Display Results: Prints each retrieved document chunk along with its similarity score and metadata.
Usage
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
Install all dependencies with:

bash
Copy code
pip install -r requirements.txt
Example Output
Ingest Script (ingest.py)
lua
Copy code
Embeddings model loaded successfully................
Qdrant collection created successfully................
Query Script (app.py)
bash
Copy code
####################################
<qdrant_client.client instance details>
####################################
<db instance details>
###############################
{'score': <similarity_score>, 'content': <retrieved_text_chunk>, 'metadata': <metadata>}
License
This project is open source and available under the MIT License.
