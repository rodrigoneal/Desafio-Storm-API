"""
Inicializa e registra as blueprints do flask.

:author: Rodrigo Silva de Castro
date: 1/28/2021
"""

from flask import Blueprint
from flask_restful import Api
from .resources.index import IndexValor
from .resources.bracket import BalacendoBracket
from .resources.lucro import LucroMax
from .resources.agua import ReterAgua

bp = Blueprint("questions", __name__)
api = Api(bp)


def init_app(app):
    """
    Função para registrar e iniciar as bluprint para o flask.

    :param app: object flask
    :return: None
    """
    api.add_resource(IndexValor, "/question1")
    api.add_resource(BalacendoBracket, "/question2")
    api.add_resource(LucroMax, "/question3")
    api.add_resource(ReterAgua, "/question4")
    app.register_blueprint(bp)
