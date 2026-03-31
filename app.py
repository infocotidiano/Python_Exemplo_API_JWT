#nossa aplicacao principal
from flask import Flask
from routes.rotas import rotas

app = Flask(__name__)

app.register_blueprint(rotas)

if __name__ == "__main__":
    app.run(debug=True)