from data_loader import load_knowledge_base, get_answer_from_faq
from ollama_client import chat_with_ollama
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregar a base de conhecimento
knowledge_base = load_knowledge_base()

def get_dynamic_response(user_question, knowledge_base):
    """Verifica se a pergunta está na base de dados e retorna a resposta."""
    
    # Normaliza a pergunta para minúsculas e remove espaços extras
    user_question = user_question.strip().lower()
    
    # Itera sobre as perguntas da base de conhecimento
    for question in knowledge_base["faq"]:
        # Compara a pergunta do usuário com a base de dados
        if user_question == question.lower():
            return knowledge_base["faq"][question]
    
    return None  # Caso não encontre, o chatbot tentará a Ollama depois

def get_most_similar_answer(user_question, knowledge_base):
    # Cria uma lista de perguntas da base de conhecimento
    questions = list(knowledge_base["faq"].keys())
    answers = list(knowledge_base["faq"].values())
    
    # Adiciona a pergunta do usuário na lista
    questions.append(user_question)
    
    # Calcula o TF-IDF para todas as perguntas
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(questions)
    
    # A última linha da matriz TF-IDF será a pergunta do usuário, e comparamos com as outras
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Encontra a pergunta mais parecida com a do usuário
    most_similar_idx = cosine_sim.argmax()
    
    # Retorna a resposta correspondente
    return answers[most_similar_idx], cosine_sim[0][most_similar_idx]

def chatbot_response(user_question, knowledge_base):
    
    # Primeiro, tenta encontrar a resposta diretamente
    dynamic_response = get_dynamic_response(user_question, knowledge_base)
    
    if dynamic_response:
        return dynamic_response  # Se encontrou uma resposta direta, retorna essa resposta
    else:
        # Caso não tenha encontrado, consulta a Ollama
        # Agora, chamamos a função de similaridade para encontrar a resposta mais parecida
        most_similar_answer, similarity = get_most_similar_answer(user_question, knowledge_base)
        
        if similarity > 0.5:  # Limiar de similaridade ajustável
            return most_similar_answer
        else:
            context = "Aqui estão algumas informações sobre a A.C.E. Consultoria: " + "\n" + \
                      f"Missão: {knowledge_base['faq'].get('Qual é a missão da A.C.E. Consultoria?')}\n" + \
                      f"Fundação: {knowledge_base['faq'].get('Qual o ano de fundação?')}\n" + \
                      f"Valores: {knowledge_base['faq'].get('Quais são os valores da A.C.E. Consultoria?')}\n"
            
            prompt = context + f"\nPergunta: {user_question}"
            
            # Usando a Ollama para gerar uma resposta
            response_from_ollama = chat_with_ollama(prompt)
            return response_from_ollama

# Função para interagir com o chatbot no terminal
def main():
    print("Faça sua pergunta")
    
    while True:
        user_question = input("Você: ")
        if user_question.lower() == "sair":
            print("Tchau!")
            break
        response = chatbot_response(user_question, knowledge_base)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
