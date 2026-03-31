import jwt
from datetime import datetime, timedelta, timezone
from config.configuracao import Configuracao

class JwtService:
    @staticmethod
    def gerar_token(cliente_id):
        payload = {
            "client_id":cliente_id,
            "exp":datetime.now(timezone.utc) + timedelta(hours=1)
        }
        
        return jwt.encode(payload, Configuracao.jwt_secret, algorithm="HS256")
    
    @staticmethod
    def validar_token(token):
        try:
            return jwt.decode(token, Configuracao.jwt_secret, algorithms=["HS256"])
        except:
            return None