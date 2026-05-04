## Exercício Integrador_2

####Planejamento básico de viagem
# Uma pessoa deseja fazer uma viagem curta e quer usar um programa simples para estimar os custos principais e organizar
#  melhor as informações.
# Neste exercício, você deverá construir um pequeno projeto com dois arquivos Python:

# funcoes_viagem.py, contendo as funções;
# principal_viagem.py, contendo a lógica principal do programa.
# Funções que devem ser implementadas no arquivo funcoes_viagem.py

#### 1-)  calcular_passagem(valor_base, bagagem=0)

# Crie uma função que receba o valor base da passagem e uma taxa opcional de bagagem. A função deve retornar o valor fi
# nal   da passagem.

# Exemplo:

# Entrada: valor_base = 350.0, bagagem = 80.0
# Saída esperada: 430.0


def calcular_passagem(valor_base, bagagem=0):
    valor_final = valor_base + bagagem
    return valor_final


####  2) calcular_hospedagem(valor_diaria, dias=1, taxa_extra=0)

# Crie uma função que receba o valor da diária, a quantidade de dias e uma taxa extra opcional. A função deve retornar o
# valor final da hospedagem.

# Exemplo:

# Entrada: valor_diaria = 200.0, dias = 3, taxa_extra = 50.0
# Saída esperada: 650.0


def calcular_hospedagem(valor_diaria, dias, taxa_extra):
    calculo_diaria = valor_diaria * dias
    calculo_final = calculo_diaria + taxa_extra
    return calculo_final


#### 3) converter_duracao(total_horas)

# Crie uma função que receba a duração total de uma viagem em horas. A função deve retornar dois valores: a quantidade de
#  dias completos e a quantidade de horas restantes.

# Exemplo:

# Entrada: total_horas = 53
# Saída esperada: (2, 5)

### entrada: receber a duração total de uma viagem em Horas


def converter_duracao(total_horas):
    dias = total_horas // 24
    horas_restantes = total_horas % 24
    return dias, horas_restantes


#### 4) calcular_orcamento(passagem, hospedagem, alimentacao=0)

# Crie uma função que receba o valor da passagem, o valor da hospedagem e um gasto opcional com alimentação. A função deve
# retornar três valores: custo fixo, custo extra e custo total geral.

# Exemplo:

# Entrada: passagem = 430.0, hospedagem = 650.0, alimentacao = 120.0
# Saída esperada: (1080.0, 120.0, 1200.0)


def calcular_orcamento(passagem, hospedagem, alimentacao=0):
    passagem_e_hospedagem = passagem + hospedagem
    preco_alimentacao = alimentacao
    custo_geral_total = passagem_e_hospedagem + preco_alimentacao
    return passagem_e_hospedagem, preco_alimentacao, custo_geral_total
