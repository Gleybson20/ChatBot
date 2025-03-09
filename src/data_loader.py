import json
import os
from difflib import get_close_matches

# Caminho do arquivo de dados
DATA_PATH = os.path.join("data", "knowledge_base.json")

def load_knowledge_base():
    """
    Carrega a base de conhecimento da empresa a partir de um arquivo JSON.
    """
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
    """
    Procura a resposta para uma pergunta dentro da base de conhecimento (FAQ).
    Se não encontrar uma correspondência exata, tenta encontrar a mais próxima.
    """
    faq = knowledge_base.get("faq", {})
    
    # Verifica se há uma correspondência exata
    if question in faq:
        return faq[question]
    
    # Procura correspondências aproximadas
    matches = get_close_matches(question, faq.keys(), n=1, cutoff=0.7)
    if matches:
        return faq[matches[0]]
    
    return None  # Caso não encontre, o chatbot tentará a OpenAI depois

def add_to_knowledge_base(question, answer, knowledge_base):
    """
    Adiciona uma nova pergunta e resposta à base de conhecimento e salva no JSON.
    """
    knowledge_base["faq"][question] = answer
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(knowledge_base, file, indent=4, ensure_ascii=False)
    print("✅ Nova entrada adicionada à base de conhecimento!")

# Carregar a base de conhecimento ao iniciar
knowledge_base = load_knowledge_base()
