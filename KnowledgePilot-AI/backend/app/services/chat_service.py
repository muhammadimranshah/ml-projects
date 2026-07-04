import time

from app.services.vector_service import search_chunks
from app.core.llm import generate_response


def ask_question(question: str):

    total_start = time.time()

    # ==========================
    # Vector Search
    # ==========================

    start = time.time()

    results = search_chunks(question)

    print(f"\nVector Search Time: {time.time() - start:.2f} sec")

    # ==========================
    # Context
    # ==========================

    docs = results.get("documents", [[]])[0]

    context = "\n\n".join(docs)

    # ==========================
    # Prompt
    # ==========================

    prompt = f"""
You are a helpful AI assistant.

If the answer exists in the context below,
answer ONLY from the context.

If the context does not contain the answer,
answer normally using your own knowledge.

Context:
{context}

Question:
{question}
"""

    # ==========================
    # LLM
    # ==========================

    start = time.time()

    answer = generate_response(prompt)

    print(f"LLM Time: {time.time() - start:.2f} sec")

    print(f"Total Time: {time.time() - total_start:.2f} sec\n")

    return answer