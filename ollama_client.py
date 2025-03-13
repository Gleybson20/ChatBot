import ollama

def chat_with_ollama(prompt):
    """
    Envia um prompt para o modelo da Ollama rodando localmente.
    """
    try:
        response = ollama.chat(
            model="mistral",  # Ou outro modelo que você escolher
            messages=[
                {"role": "system", "content": "Você é um assistente virtual da A.C.E. Consultoria."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Essa pergunta será respondida ao longo do trainee."
