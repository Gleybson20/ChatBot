import os

class Config:
    # Configuração do servidor Flask
    SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
    SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
    DEBUG = os.getenv(("DEBUG", "True") == "True")

    # Configuração do banco de dados
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///chatbot.db")

    # Configuração do chatbot
    CHATBOT_MODEL = os.getenv("CHATBOT_MODEL", "default_model")

    # Configuração de logs
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Instância global da configuração
config = Config()
