#nosso arquivo de configuração
import os
from dotenv import load_dotenv

load_dotenv()

class Configuracao:
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    jwt_secret = os.getenv("JWT_SECRET")
    