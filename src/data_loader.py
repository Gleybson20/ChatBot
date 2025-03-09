import json
import os

# Caminho do arquivo de dados
DATA_PATH = os.path.join("data", "knowledge_base.json")

def load_knowledge_base():
    """
    Carrega a base de conhecimento da empresa a partir de um arquivo JSON.
    """
    if not os.path.exists(DATA_PATH):
        print(f"⚠️ Arquivo {DATA_PATH} não encontrado! Criando base vazia.")
        return {"faq": {}}

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def get_answer_from_faq(question, knowledge_base):
    """
    Procura a resposta para uma pergunta dentro da base de conhecimento (FAQ).
    """
    faq = knowledge_base.get("faq", {})
    
    # Busca por uma pergunta idêntica na base
    for stored_question, answer in faq.items():
        if question.lower() in stored_question.lower():
            return answer

    return None  # Caso não encontre, o chatbot tentará a OpenAI depois

# Carregar a base de conhecimento ao iniciar
knowledge_base = load_knowledge_base()
