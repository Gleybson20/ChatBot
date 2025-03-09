import openai
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Obter a chave da API
api_key = os.getenv("OPENAI_API_KEY")

# Criar o cliente
client = openai.OpenAI(api_key=api_key)

# Listar modelos disponíveis
models = client.models.list()
for model in models.data:
    print(model.id)