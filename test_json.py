from src.data_loader import get_answer_from_faq, knowledge_base

def test_json_manual():
    """
    Permite que o usuário faça perguntas manualmente e teste a base de conhecimento (JSON).
    """
    print("🔍 Teste manual do JSON iniciado!")
    print("💬 Digite sua pergunta ou 'sair' para encerrar.\n")

    while True:
        question = input("Você: ").strip()

        if question.lower() in ["sair", "exit", "quit"]:
            print("👋 Encerrando o teste manual. Até mais!")
            break

        response = get_answer_from_faq(question, knowledge_base)

        if response:
            print(f"🤖 Chatbot (JSON): {response}\n")
        else:
            print("❌ Pergunta não encontrada no JSON.\n")

if __name__ == "__main__":
    test_json_manual()
