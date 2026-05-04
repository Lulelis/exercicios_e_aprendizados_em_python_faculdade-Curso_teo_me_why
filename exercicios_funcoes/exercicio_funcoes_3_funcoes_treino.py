#### Exercício 3


# 1) calcular_calorias(calorias_base, bonus=0)


# Crie uma função que receba a quantidade base de calorias gastas em um treino e um bônus opcional referente a uma atividade complementar. A função deve retornar o total de calorias.
#
# Exemplo:
#
# Entrada: calorias_base = 280, bonus = 40
# Saída esperada: 320


def calcular_calorias(calorias_base, bonus=0):
    bonus_opcional = bonus
    total_calorias = calorias_base + bonus_opcional
    return total_calorias


#### 2) calcular_tempo_treino(tempo_principal, aquecimento=10)


# Crie uma função que receba o tempo principal do treino e um tempo opcional de aquecimento. A função deve retornar o tempo total do treino, em minutos.


# Exemplo:


# Entrada: tempo_principal = 45, aquecimento = 15
# Saída esperada: 60


def calcular_tempo_treino(tempo_principal, aquecimento=10):
    tempo_aquecimento = aquecimento
    tempo_total = tempo_principal + tempo_aquecimento
    return tempo_total


#### 3) analisar_desempenho(total_minutos)


# Crie uma função que receba o total de minutos treinados na semana. A função deve retornar dois valores: quantidade de horas completas e minutos restantes.


# Exemplo:


# Entrada: total_minutos = 135
# Saída esperada: (2, 15)


def analisar_desempenho(total_minutos):
    horas_do_treino = total_minutos // 60  # horas completas
    resto_em_minutos = total_minutos % 60  # minutos restantes
    return horas_do_treino, resto_em_minutos


#### 4) consolidar_treino(calorias, tempo, meta=300)


# Crie uma função que receba as calorias gastas, o tempo total treinado e uma meta opcional de calorias. A função deve retornar três valores: diferença para a meta, valor booleano indicando se a meta foi atingida e uma mensagem de resumo.


# Exemplo:


# Entrada: calorias = 320, tempo = 60, meta = 300
# Saída esperada: (20, True, "Meta atingida")


def consolidar_treino(calorias, tempo, meta=300):
    meta_opcional = meta
    diferenca_meta = calorias - meta_opcional
    if calorias >= meta_opcional:
        return diferenca_meta, True, "Meta atingida"
    else:
        return diferenca_meta, False, "Meta não atingida"
