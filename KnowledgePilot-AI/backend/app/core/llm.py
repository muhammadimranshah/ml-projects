import ollama

# MODEL_NAME = "llama3.2:latest"   # or mistral, codellama, etc.
MODEL_NAME = "qwen2.5:1.5b"
def generate_response(prompt: str):
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]