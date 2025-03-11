from data_loader import get_answer_from_faq, add_to_knowledge_base, load_knowledge_base
from ollama_client import chat_with_openai
from fuzzywuzzy import fuzz

# Carregar a base de conhecimento ao iniciar o chatbot
knowledge_base = load_knowledge_base()

def get_most_similar_answer(question, knowledge_base):
    """Busca a pergunta mais parecida na base de conhecimento e retorna a resposta associada."""
    faq = knowledge_base.get("faq", {})
    max_similarity = 0
    best_match = None

    # Verificar a similaridade de cada pergunta com a pergunta atual
    for existing_question in faq.keys():
        similarity = fuzz.ratio(question.lower(), existing_question.lower())
        if similarity > max_similarity and similarity > 70:  # 70% de similaridade
            max_similarity = similarity
            best_match = existing_question

    if best_match:
        return faq[best_match]  # Retorna a resposta associada à pergunta mais parecida
    return None

def chatbot_response(question):
    """Função principal do chatbot"""
    # Passo 1: Procurar resposta exata no JSON
    answer = get_answer_from_faq(question, knowledge_base)
    if answer:
        return answer  # Resposta encontrada no JSON

    # Passo 2: Tentar encontrar a resposta mais parecida no JSON
    similar_answer = get_most_similar_answer(question, knowledge_base)
    if similar_answer:
        return f"Baseado na nossa base de conhecimento, aqui está uma resposta relacionada: {similar_answer}"

    # Passo 3: Consultar o modelo de IA (Ollama/Mistral)
    openai_response = chat_with_openai(question)

    if not openai_response or "❌" in openai_response:
        return "❌ Desculpe, não consegui processar sua pergunta no momento."

    # Passo 4: Adicionar nova resposta ao JSON
    print("📚 Adicionando nova resposta à base de conhecimento...")
    add_to_knowledge_base(question, openai_response, knowledge_base)

    return openai_response

# Interação com o usuário
if __name__ == "__main__":
    while True:
        user_input = input("Faça a sua pergunta: ")
        if user_input.lower() == "sair":
            print("👋 Até mais!")
            break
        response = chatbot_response(user_input)
        print(f"Resposta: {response}")
