import openai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Obtém a chave da API
api_key = os.getenv("OPENAI_API_KEY")

# Verifica se a chave foi carregada corretamente
if not api_key:
    raise ValueError("ERRO: A chave OPENAI_API_KEY não foi encontrada. Verifique o arquivo .env!")

# Inicializa o cliente OpenAI
client = openai.OpenAI(api_key=api_key)

def chat_with_openai(prompt):
    """
    Envia um prompt para a API da OpenAI e retorna a resposta.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Alterado para o modelo disponível na sua conta
            messages=[
                {"role": "system", "content": "Você é um assistente virtual de uma empresa."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na comunicação com a OpenAI: {str(e)}"

def chat_with_openai(prompt):
    """
    Simula uma resposta caso a API não esteja disponível.
    """
    if not api_key:
        return "Modo offline: resposta simulada."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual de uma empresa."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except openai.OpenAIError:
        return "Erro: Sem créditos. Modo offline ativado."
