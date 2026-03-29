#validacao dos dados
from config.configuracao import Configuracao

class ClienteModel:
    @staticmethod
    def validar_clientes(client_id, client_secret):
        return (
            client_id == Configuracao.client_id and
            client_secret == Configuracao.client_secret
        )