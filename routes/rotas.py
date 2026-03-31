from flask import Blueprint
from controllers.autenticacao_controller import AutenticacaoController
from middleware.autenticacao_middleware import requer_token

rotas = Blueprint("rotas",__name__)

#rota /login
rotas.route("/login", methods=["POST"])(
    AutenticacaoController.login
)

#rota de lista clientes
rotas.route("/listar_clientes", methods=["GET"])(
    requer_token(AutenticacaoController.endpoint_lista_cliente)
)

#rota de inclui clientes
rotas.route("/incluir_clientes", methods=["POST"])(
    requer_token(AutenticacaoController.endpoint_inclui_cliente)
)