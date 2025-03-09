from src.data_loader import get_answer_from_faq, add_to_knowledge_base, knowledge_base
from src.openai_client import chat_with_openai

def chatbot_response(question):
    """
    Função principal do chatbot.
    1. Verifica se a pergunta já está na base de conhecimento (JSON).
    2. Se não encontrar, consulta a OpenAI.
    3. (Opcional) Pode salvar a nova resposta na base de conhecimento.
    """
    # Tenta encontrar a resposta na base de conhecimento
    answer = get_answer_from_faq(question, knowledge_base)
    
    if answer:
        return answer  # Retorna a resposta do JSON
    
    # Se não encontrar, consulta a OpenAI
    openai_response = chat_with_openai(question)
    
    # (Opcional) Adicionar nova resposta à base de conhecimento
    if openai_response:
        add_to_knowledge_base(question, openai_response, knowledge_base)
    
    return openai_response

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Chatbot encerrado. Até logo!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
