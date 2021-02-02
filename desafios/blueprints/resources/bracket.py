"""Verifica se um brackte que abre tem um fechamento; balanceado ou não balanceado."""

from flask_restful import Resource, reqparse

argumento = reqparse.RequestParser()
argumento.add_argument("brackts", type=str)


class BalacendoBracket(Resource):
    """Classe que herda resource."""

    def get(self):
        """
        Pega um arquivo json com os brackets "({[]})" e verifica se são balanceadas {[}] Não balanceada {[]} Balanceada.

        :return: Json
        """
        brackts = argumento.parse_args()["brackts"]

        pilha = []
        for bracket in brackts:
            if bracket in ["(", "{", "["]:
                pilha.append(bracket)
            else:
                if not pilha:
                    return {"balanced": False}
                bracket_atual = pilha.pop()
                if bracket_atual == "(":
                    if bracket != ")":
                        return {"balanced": False}
                if bracket_atual == "{":
                    if bracket != "}":
                        return {"balanced": False}
                if bracket_atual == "[":
                    if bracket != "]":
                        return {"balanced": False}
        if pilha:
            return {"balanced": False}
        return {"balanced": True}
