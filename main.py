# Biblioteca usada para acessar variáveis de ambiente
import os

# Biblioteca usada para exibir mensagens de log no terminal
import logging

# Biblioteca que carrega as variáveis do arquivo .env
from dotenv import load_dotenv

# Cliente oficial do Supabase para conectar no banco
from supabase import create_client, Client


# Carrega as informações salvas no arquivo .env
load_dotenv()

# Configura o formato dos logs exibidos no terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

# Dados do Supabase vindos do .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def create_supabase_client() -> Client:
    """
    Cria a conexão com o Supabase.
    """

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL e SUPABASE_KEY são obrigatórios.")

    return create_client(SUPABASE_URL, SUPABASE_KEY)


def get_contacts(supabase: Client) -> list:
    """
    Busca até 3 contatos cadastrados na tabela 'contatos'.
    """

    response = (
        supabase
        .table("contatos")
        .select("nome_contato, telefone")
        .limit(3)
        .execute()
    )

    return response.data


def main() -> None:
    """
    Função principal usada para buscar os contatos no Supabase.
    """

    supabase = create_supabase_client()

    contacts = get_contacts(supabase)

    logging.info(f"{len(contacts)} contato(s) encontrado(s).")

    print(contacts)


if __name__ == "__main__":
    main()