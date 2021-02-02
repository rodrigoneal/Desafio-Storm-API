"""
Calcula o maximo de agua da chuva que pode ser armazenado entre duas elevações.

:author: Rodrigo Silva de Castro
:date:1/28/2021
"""

from flask_restful import Resource, reqparse

argumento = reqparse.RequestParser()
argumento.add_argument("array", action="append", type=int)


class ReterAgua(Resource):
    """Clase que herda de Resources."""

    def get(self):
        """
        Percorre a lista da esquerda pra direita e pega o maior valor do array no indice.

        N e armazena na variavel esq no indice N
        Percorre a lista da direita pra esquerda e pega o maior valor do array no indice
        N e armazena na variavel dir no indice N
        Pega o menor valor entre as  listas esq e dir no indice N e subtrai com o array no mesmo index esse valor
        é somado na variavel agua
        Exemplo: esq = 3; dir = 2; array = 1;
        primeiro você tira o menor valor que é 2
        logo 2 - 1 = 1
        1 é o valor que cabe de agua
        """
        array = argumento.parse_args()["array"]
        tamanho = len(array)
        agua = 0
        # Cria duas listas com valores zero do tamanho da lista do array
        esq = tamanho * [0]
        dir = tamanho * [0]
        # Pega o primeiro valor do array
        esq[0] = array[0]
        # Declara que ele é o maior valor por enquanto
        max_esq = array[0]

        for index in range(0, tamanho):
            # Verifica se o maior valor do array no indece n é maior que o valor de max
            if max_esq < array[index]:
                # Atualiza o valor de max_esq com o maior valor do array no indice n
                max_esq = array[index]
                # Passa o maior valor para dentro da variavel esq
                esq[index] = max_esq
            else:
                # Se não houver um valor maior passa o valor anterior para o novo no indice n
                esq[index] = max_esq
        # Declara que o ultimo valor do array é o maior por enquanto
        max_dir = array[-1]
        # Pega os indeces de trás pra frente
        for index in range(tamanho - 1, -1, -1):
            # Se o max_dir é menor que o array com os indices de trás pra frente
            if max_dir < array[index]:
                max_dir = array[index]
                # Preenche a lista dir de trás pra frente
                dir[index] = max_dir

            else:
                dir[index] = max_dir

        for index in range(tamanho):

            agua += min(esq[index], dir[index]) - array[index]

        return agua
