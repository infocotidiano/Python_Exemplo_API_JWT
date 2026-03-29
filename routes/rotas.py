#definido as rotas
from flask import Blueprint
from controllers.autenticacao_controller import AutenticacaoController
from middleware.autenticacao_middleware import requer_token


rotas = Blueprint("rotas", __name__)

#rota login
rotas.route("/login", methods=["POST"])(
    AutenticacaoController.login
)

#rota 1
rotas.route("/listar_cliente", methods=["GET"])(
    requer_token(AutenticacaoController.endpoint_protegido_1)
)

#rota 2
rotas.route("/incluir_cliente", methods=["POST"])(
    requer_token(AutenticacaoController.endpoint_protegido_2)
)
