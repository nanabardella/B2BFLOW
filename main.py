# Bibliotecas que utilizei no projeto:
import os
import logging
import requests

# Carrega as variáveis do arquivo .env
from dotenv import load_dotenv

# Importa o cliente do Supabase
from supabase import create_client, Client

# Carrega as variáveis de ambiente
load_dotenv()

# Configura os logs exibidos no terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)