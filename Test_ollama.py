import ollama

response = ollama.chat(
    model="mistral",
    messages=[{"role": "user", "content": "O que é a A.C.E. Consultoria?"}]
)

print(response["message"]["content"])
