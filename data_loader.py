import json
import os

# Caminho do arquivo de dados
DATA_PATH = os.path.join("data", "knowledge_base.json")

def load_knowledge_base():
    """Carrega a base de conhecimento do JSON."""
    if not os.path.exists(DATA_PATH):
        print(f"⚠️ Arquivo {DATA_PATH} não encontrado! Criando base vazia.")
        return {"faq": {}}
    
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("❌ Erro ao carregar a base de conhecimento. O arquivo JSON pode estar corrompido.")
        return {"faq": {}}

def get_answer_from_faq(question, knowledge_base):
    """Procura a resposta para uma pergunta dentro da base de conhecimento (FAQ)."""
    faq = knowledge_base.get("faq", {})
    
    # Verifica se há uma correspondência exata
    if question in faq:
        return faq[question]
    
    return None  # Caso não encontre, o chatbot tentará a Ollama depois
