

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
        maior = max(maior, notas[i])

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
        menor = min(menor, notas[i])

    return menor


### Funções:
def contar_aprovados(notas):
    """
    Conta a quantidade de estudantes aprovados na turma.

    Parâmetros:
        notas (list): lista contendo as notas dos estudantes.

    Retorno:
        int: quantidade de estudantes com nota maior ou igual a 60.

    Observação:
        Considera aprovação com nota maior ou igual a 60.
    """

    quantidade_aprovados = 0

    for i in range(len(notas)):
        if notas[i] >= 60:
            quantidade_aprovados += 1

    return quantidade_aprovados

def classificar_turma(notas):
    """
    Classifica o desempenho geral da turma com base na média das notas.

    Parâmetros:
        notas (list): lista contendo as notas dos estudantes.

    Retorno:
        str: classificação da turma.

    Observação:
        Utiliza a função calcular_media() para obter a média da turma.
        A classificação segue as regras:
        - Turma Excelente: média maior ou igual a 80.
        - Turma Regular: média maior ou igual a 60 e menor que 80.
        - Turma em Atenção: média menor que 60.
    """

    media_turma = calcular_media(notas)

    if media_turma >= 80:
        return "Turma Excelente"
    elif media_turma >= 60 and media_turma < 80:
        return "Turma Regular"
    elif media_turma < 60:
        return "Turma em Atenção"

def gerar_relatorio(notas):
    """
    Gera um relatório consolidado da turma.

    Parâmetros:
        notas (list): lista contendo as notas dos estudantes.

    Retorno:
        dict: dicionário contendo a média da turma,
        maior nota, menor nota, quantidade de aprovados
        e classificação da turma.

    Observação:
        Reutiliza as funções já existentes no módulo
        para calcular cada informação do relatório.
    """
    media_turma = calcular_media(notas)
    maior_nota = encontrar_maior_nota(notas)
    menor_nota = encontrar_menor_nota(notas)
    qtd_aprovados = contar_aprovados(notas)
    classificacao_turma = classificar_turma(notas)
    dicio_relatorio ={}
    dicio_relatorio["media"] = media_turma
    dicio_relatorio["maior"] = maior_nota
    dicio_relatorio["menor"] = menor_nota
    dicio_relatorio["aprovados"] = qtd_aprovados
    dicio_relatorio["classificacao"] = classificacao_turma
    return dicio_relatorio
