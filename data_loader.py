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
    
    return None  # Caso não encontre, o chatbot tentará a OpenAI depois

def add_to_knowledge_base(question, answer, knowledge_base):
    """Adiciona uma nova pergunta e resposta à base de conhecimento e salva no JSON."""
    faq = knowledge_base.get("faq", {})
    
    # Verifica se a pergunta já existe antes de adicionar
    if question not in faq:
        faq[question] = answer
        knowledge_base["faq"] = faq
        
        # Salva a nova entrada no arquivo JSON
        with open(DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(knowledge_base, file, indent=4, ensure_ascii=False)
        print("✅ Nova entrada adicionada à base de conhecimento!")
    else:
        print("❌ Pergunta já existe na base de conhecimento. Não foi adicionada.")
