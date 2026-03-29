#regras de entrada e saida
from flask import request, jsonify
from models.cliente_model import ClienteModel
from services.jwt_service import JwtService

class AutenticacaoController:
    @staticmethod
    def login():
        dados = request.json
        cliente_id = dados.get("client_id")
        cliente_secret = dados.get("client_secret")
        if not ClienteModel.validar_clientes(cliente_id, cliente_secret):
            return jsonify({"Erro":"credenciais inválidas"}), 401
        
        token = JwtService.gerar_token(cliente_id)
        return jsonify({"access_token":token}), 200
    
    @staticmethod
    def endpoint_protegido_1():
        return jsonify({"mensagem": "pedido de lista de cliente OK"}), 200
        
    @staticmethod
    def endpoint_protegido_2():
        return jsonify({"mensagem": "Incluir Cliente OK"}), 200
        
            