import chromadb

# ✅ Persistent storage (VERY IMPORTANT)
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# ✅ Single consistent collection
collection = client.get_or_create_collection(
    name="documents"
)