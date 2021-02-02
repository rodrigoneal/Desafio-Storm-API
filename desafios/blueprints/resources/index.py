"""
Recebe um array de valores e um valor alvo e calcula se a soma de algum dos valores dentro do array for igual ao alvo retorna o indice dos dois numeros.

author: Rodrigo Silva de Castro
date:1/28/2021
"""

from flask_restful import Resource, reqparse

argumento = reqparse.RequestParser()
argumento.add_argument("nums", action="append", type=int)
argumento.add_argument("alvo", type=int)


class IndexValor(Resource):
    """Classe que herda de Rosources."""

    def get(self):
        """Recebe uma lista e um numeros de alvo que calcula os valores retornao indice dos valores que se somam."""
        nums = argumento.parse_args()["nums"]
        alvo = argumento.parse_args()["alvo"]
        for i in range(len(nums)):
            # Pula o valor de i pra não gerar soma por ele mesmo
            for v in range(i + 1, len(nums)):
                # Verifica se o index de nums no index i e v == alvo
                if nums[i] + nums[v] == alvo:
                    return {"index": [i, v]}
