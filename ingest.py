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

#load the embeddings model
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
