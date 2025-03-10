import ollama

def chat_with_openai(prompt):
    """
    Envia um prompt para o modelo LLaMA 3 rodando localmente via Ollama.
    """
    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual da A.C.E. Consultoria."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"❌ Erro na comunicação com LLaMA 3: {str(e)}"

# Teste opcional ao rodar o arquivo diretamente
if __name__ == "__main__":
    pergunta_teste = "O que é a A.C.E. Consultoria?"
    print(f"Pergunta: {pergunta_teste}")
    print("Resposta do LLaMA 3:", chat_with_openai(pergunta_teste))
