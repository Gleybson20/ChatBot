import sys
import os

# Adiciona o caminho da pasta raiz ao sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Agora a importação funcionará corretamente
from src.openai_client import chat_with_openai

# Testando a função
pergunta = "Qual é a capital da França?"
resposta = chat_with_openai(pergunta)
print(resposta)
