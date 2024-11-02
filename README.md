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
2. **Install necessary packages**:Ensure that you have Python installed (preferably Python 3.8 or later).
   '''bash
   pip install langchain-community qdrant-client transformers pypdf
