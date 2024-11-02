from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient

#load the embeddings model

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