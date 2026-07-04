from app.database.chroma import collection
from app.utils.embeddings import create_embeddings


def store_chunks(document_id, chunks):
    """
    Store document chunks + embeddings into ChromaDB
    """

    print("\n========== VECTOR STORE DEBUG ==========")
    print("Document ID:", document_id)
    print("Chunks received:", len(chunks))

    # ❌ Safety check: empty chunks
    if not chunks:
        print("❌ No chunks to store. Exiting store_chunks.")
        return

    # Create embeddings
    embeddings = create_embeddings(chunks)

    print("Embeddings generated:", len(embeddings))

    # ❌ Safety check: mismatch
    if len(embeddings) != len(chunks):
        print("❌ ERROR: Embeddings and chunks mismatch!")
        return

    # Store in ChromaDB
    for i, chunk in enumerate(chunks):

        try:
            collection.add(
                ids=[f"{document_id}_{i}"],
                embeddings=[embeddings[i].tolist()],
                documents=[chunk],
                metadatas=[{"document_id": document_id}]
            )

            print(f"✅ Stored chunk {i}")

        except Exception as e:
            print(f"❌ Error storing chunk {i}: {str(e)}")

    print("========================================\n")

def search_chunks(question):
    embedding = create_embeddings([question])[0]

    results = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=5
    )

    docs = results.get("documents", [[]])[0]
    distances = results.get("distances", [[]])[0]

    # Combine & sort by relevance (LOW distance = better match)
    paired = list(zip(docs, distances))
    paired.sort(key=lambda x: x[1])

    # Take top 3 best chunks only
    top_chunks = [doc for doc, _ in paired[:3]]

    return {
        "documents": [top_chunks]
    }
def delete_document_vectors(document_id):

    ids = collection.get()["ids"]

    delete_ids = []

    for vector_id in ids:

        if vector_id.startswith(f"{document_id}_"):

            delete_ids.append(vector_id)

    if delete_ids:

        collection.delete(ids=delete_ids)