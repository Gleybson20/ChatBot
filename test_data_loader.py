from src.data_loader import load_knowledge_base, get_answer_from_faq

# Carregar a base de conhecimento
knowledge_base = load_knowledge_base()

# Testar uma pergunta do FAQ
pergunta = "Qual é o horário de funcionamento?"
resposta = get_answer_from_faq(pergunta, knowledge_base)

print(f"Pergunta: {pergunta}")
print(f"Resposta: {resposta if resposta else 'Pergunta não encontrada no FAQ.'}")
