def calcular_media(notas):
    """
    Calcula a média aritmética das notas de uma turma.

    Parâmetros:
        notas (list): lista contendo as notas dos estudantes.

    Retorno:
        float: média das notas da lista.

    Observação:
        Considera que a lista de notas não está vazia.
    """
    
    soma_notas = 0

    for posicao in range(len(notas)):
        soma_notas += notas[posicao]

    media = soma_notas / len(notas)

    return media


def encontrar_maior_nota(notas):
    """
    Encontra a maior nota presente na lista.

    Parâmetros:
        notas (list): lista contendo as notas dos estudantes.

    Retorno:
        int ou float: maior nota encontrada.

    Observação:
        Considera que a lista de notas não está vazia.
    """

    maior = notas[0]

    for i in range(len(notas)):
        if notas[i] > maior:
            maior = notas[i]

    return maior


def encontrar_menor_nota(notas):
    """
    Encontra a menor nota presente na lista.

    Parâmetros:
        notas (list): lista contendo as notas dos estudantes.

    Retorno:
        int ou float: menor nota encontrada.

    Observação:
        Considera que a lista de notas não está vazia.
    """

    menor = notas[0]

    for i in range(len(notas)):
        if notas[i] < menor:
            menor = notas[i]

    return menor