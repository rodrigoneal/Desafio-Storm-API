"""
Calcular o lucro maximo obtido numa operação de vendas e compras de ação.

author:Rodrigo Silva De Castro
Date 30/01/2021
"""

from flask_restful import Resource, reqparse

argumento = reqparse.RequestParser()
argumento.add_argument("acoes", action="append", type=int)


class LucroMax(Resource):
    """Classe que importa herda o objeto Resource para calcular o lucro maximo da venda de ações."""

    def get(self):
        """
        Calcula o lucro maximo possivel na compra e venda de uma ação.

        :return: Json
        """
        acoes = argumento.parse_args()["acoes"]
        # Reverte os valores
        acoes.reverse()

        # Lucro e valor de compra
        lucro = 0
        compra = 0
        # Pega cada valor de dentro das ações
        for valor in acoes:
            # Verifica se o valor da ação é maior que o valor da compra
            if valor > compra:
                compra = valor
            # Verifica se a venda da ação vai render mais lucro que o valor anterior
            if compra - valor > lucro:
                lucro = compra - valor

        return {"lucro_maximo": lucro}
