import unittest
from src.chatbot import chatbot_response
from src.data_loader import load_knowledge_base, add_to_knowledge_base

class TestChatbot(unittest.TestCase):
    def setUp(self):
        """Carrega a base de conhecimento antes de cada teste."""
        self.knowledge_base = load_knowledge_base()

    def test_json_response(self):
        """Testa se perguntas conhecidas retornam a resposta correta do JSON."""
        question = "O que é a A.C.E. Consultoria?"
        expected_answer = self.knowledge_base.get("faq", {}).get(question, None)
        if expected_answer:
            self.assertEqual(chatbot_response(question), expected_answer)
        else:
            self.skipTest("Pergunta não encontrada no JSON. Adicione-a para testar corretamente.")

    def test_openai_fallback(self):
        """Testa se perguntas desconhecidas retornam uma resposta válida da OpenAI."""
        question = "Qual é o significado da vida?"
        response = chatbot_response(question)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 5)  # Garante que há uma resposta significativa
    
    def test_add_to_knowledge_base(self):
        """Testa se uma nova pergunta pode ser adicionada ao JSON."""
        new_question = "Quem fundou a A.C.E. Consultoria?"
        new_answer = "A empresa foi fundada por um grupo de estudantes de engenharia."
        add_to_knowledge_base(new_question, new_answer, self.knowledge_base)
        
        updated_knowledge_base = load_knowledge_base()
        self.assertEqual(updated_knowledge_base["faq"].get(new_question), new_answer)

if __name__ == "__main__":
    unittest.main()
