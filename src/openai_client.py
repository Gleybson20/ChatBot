import openai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Obtém a chave da API
api_key = os.getenv("OPENAI_API_KEY")

# Verifica se a chave foi carregada corretamente
if not api_key:
    raise ValueError("❌ ERRO: A chave OPENAI_API_KEY não foi encontrada. Verifique o arquivo .env!")

# Inicializa o cliente OpenAI
client = openai.OpenAI(api_key=api_key)

def chat_with_openai(prompt):
    """
    Envia um prompt para a API da OpenAI e retorna a resposta.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual da A.C.E. Consultoria."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except openai.OpenAIError as e:
        return f"❌ Erro na comunicação com a OpenAI: {str(e)}"

# Teste opcional ao rodar o arquivo diretamente
if __name__ == "__main__":
    pergunta_teste = "O que é a A.C.E. Consultoria?"
    print(f"Pergunta: {pergunta_teste}")
    print("Resposta da OpenAI:", chat_with_openai(pergunta_teste))
