from src.chatbot import chatbot_response

def start_chatbot():
    """
    Interface de interação com o chatbot via terminal.
    """
    print("🤖 Chatbot A.C.E. iniciado! Digite 'sair' para encerrar.")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("👋 Chatbot encerrado. Até logo!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chatbot()