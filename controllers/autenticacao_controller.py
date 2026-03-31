#regras de entrada e saida
from flask import request, jsonify
from models.cliente_model import ClienteModel
from services.jwt_service import JwtService

class AutenticacaoController:
    @staticmethod
    def login():
        dados = request.json       
        client_id = dados.get("client_id")
        client_secret = dados.get("client_secret")
        
        if not ClienteModel.validar_clientes(client_id, client_secret):
            return jsonify({"Erro":"Credenciais inválidas !"}), 401
        
        token = JwtService.gerar_token(client_id)
        return jsonify({"access_token":token}), 200
    
    @staticmethod
    def endpoint_lista_cliente():
        return jsonify({"Mensagem":"token valido, retornando lista de clientes !"}), 200
        
    @staticmethod
    def endpoint_inclui_cliente():
        return jsonify({"Mensagem":"token valido, cliente cadastrado !"}), 200