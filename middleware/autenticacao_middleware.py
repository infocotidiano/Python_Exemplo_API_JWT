#tokens
from functools import wraps 
from flask import request, jsonify
from services.jwt_service import JwtService

def requer_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"Erro":"Token não enviado !"}), 401
        
        try:
            token = auth_header.split(" ")[1]
        except:
            return jsonify({"Erro":"Formato invalido !"}), 401
        
        dados = JwtService.validar_token(token)
        
        if not dados:
            return jsonify({"Erro":"Token invalido !"}), 401
        
        return f(*args,**kwargs)
    return decorator        