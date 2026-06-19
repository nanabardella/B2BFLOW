# Bibliotecas que utilizei no projeto
import os
import logging

# Carrega as variáveis do arquivo .env
from dotenv import load_dotenv
print("URL:", os.getenv("SUPABASE_URL"))
print("KEY:", os.getenv("SUPABASE_KEY"))

# Cliente oficial do Supabase
from supabase import create_client, Client

# Carrega as variáveis de ambiente
load_dotenv()

# Configuração dos logs
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

# Dados do Supabase vindos do .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def create_supabase_client() -> Client:
    """
    Cria uma conexão com o Supabase.
    """

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError(
            "SUPABASE_URL e SUPABASE_KEY são obrigatórios."
        )

    return create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )


def main():
    supabase = create_supabase_client()

    print("Conectado ao Supabase com sucesso!")


if __name__ == "__main__":
    main()