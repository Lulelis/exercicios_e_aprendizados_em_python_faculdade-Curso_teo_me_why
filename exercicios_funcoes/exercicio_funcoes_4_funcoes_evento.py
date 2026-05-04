#### 1) calcular_valor_base(tipo_ingresso, valor_padrao=120)

# Crie uma função que receba o tipo de ingresso escolhido pelo participante e um valor padrão opcional.
# Considere os seguintes multiplicadores sobre o valor padrão:
# "regular" → 100% do valor padrão;
# "vip" → 150% do valor padrão;
# "estudante" → 60% do valor padrão.
# A função deve retornar o valor base calculado para o ingresso.

# Exemplo:
# Entrada: tipo_ingresso = "vip", valor_padrao = 120
# Saída esperada: 180.0


def calcular_valor_base(tipo_ingresso, valor_padrao=120):
    # Multiplicadores sobre o valor padrão:
    if tipo_ingresso == "vip":
        valor_final = valor_padrao * 150 / 100
    elif tipo_ingresso == "regular":
        valor_final = valor_padrao * 100 / 100
    elif tipo_ingresso == "estudante":
        valor_final = valor_padrao * 60 / 100
    return valor_final


#### 2) calcular_extras(valor_base, oficinas=0, material_extra=False)

# Crie uma função que receba o valor base do ingresso, a quantidade de oficinas extras escolhidas
# e uma indicação booleana informando se o participante deseja material extra.
# Regras:
# - cada oficina extra adiciona R$ 30,00;
# - se houver material extra, adicionar R$ 20,00.
# A função deve retornar três valores:
# - valor total das oficinas;
# - valor do material extra;
# - valor parcial atualizado.


def calcular_extras(valor_base, oficinas=0, material_extra=False):
    oficinas_extras = 30
    material_extra_adicionado = 20
    valor_final = 0
    if material_extra != False:
        material_extra = material_extra_adicionado
    if oficinas > 0:
        oficinas = oficinas * oficinas_extras
    valor_final = valor_base + oficinas + material_extra
    return oficinas, material_extra, valor_final


#### 3) aplicar_desconto(valor_parcial, cupom=0, taxa_admin=5)

# Crie uma função que receba um valor parcial, um desconto percentual opcional de cupom e uma taxa administrativa percent
# ual padrão.

# A função deve:

# calcular o valor do desconto;
# aplicar o desconto;
# calcular a taxa administrativa sobre o valor já descontado;
# retornar três valores:
# valor do desconto;
# valor da taxa administrativa;
# valor final a pagar.
# Exemplo:

# Entrada: valor_parcial = 200.0, cupom = 10, taxa_admin = 5
# Saída esperada: (20.0, 9.0, 189.0)


def aplicar_desconto(valor_parcial, cupom=0, taxa_admin=5):
    cupom_desconto = cupom
    valor_final = 0
    valor_desconto = cupom_desconto / 100 * valor_parcial
    valor_parcial = valor_parcial - valor_desconto
    valor_taxa_admin = taxa_admin / 100 * valor_parcial
    valor_final = valor_parcial + valor_taxa_admin
    return valor_desconto, valor_taxa_admin, valor_final


#### 4) classificar_participacao(oficinas, material_extra, total_final)

# Crie uma função que receba a quantidade de oficinas, a informação sobre material extra e o valor final da inscrição. A
# função deve retornar uma classificação textual para o perfil da inscrição.

# Sugestão de regras:

# se tiver 2 ou mais oficinas e material extra → "Inscrição completa";
# se tiver pelo menos 1 oficina → "Inscrição intermediária";
# caso contrário → "Inscrição básica".
# Exemplo:


def classificar_participacao(oficinas, material_extra, total_final):
    if oficinas >= 2 and material_extra == True and total_final >= 250:
        return "Inscrição Premium!"
    elif oficinas >= 2 and material_extra == True:
        return "Inscrição Completa"
    elif oficinas >= 1:
        return "Inscrição Intermediária"
    else:
        return "Inscrição Básica"


#### 5 gerar_relatorio_participante(nome, tipo_ingresso, valor_padrao, oficinas, material_extra, cupom=0)

# Crie uma função mais sofisticada, responsável por encadear chamadas das funções anteriores. Ela deve:

# chamar calcular_valor_base;
# usar o resultado para chamar calcular_extras;
# usar o valor parcial para chamar aplicar_desconto;
# usar o total final para chamar classificar_participacao;
# retornar múltiplos valores com os principais dados consolidados do participante.
# Essa função deve retornar, por exemplo:

# valor base;
# valor das oficinas;
# valor do material;
# valor do desconto;
# valor da taxa administrativa;
# valor final;
# classificação da inscrição.
# Exemplo:


# Entrada: nome = "Marina", tipo_ingresso = "vip", valor_padrao = 120, oficinas = 2, material_extra = True, cupom = 10
# Saída esperada: (180.0, 60.0, 20.0, 26.0, 11.7, 245.7, "Inscrição completa")


def gerar_relatorio_participante(
    nome, tipo_ingresso, valor_padrao, oficinas, material_extra, cupom=0
):
    ### Encadeamento de chamada das funções anteriores:
    nome_participante = nome
    ingresso_informado = tipo_ingresso
    valor_informado = valor_padrao
    num_oficinas = oficinas
    existe_material_extra = material_extra
    num_cupons = cupom
    valor_final_ingresso = calcular_valor_base(ingresso_informado, valor_informado)
    oficinas_contabilizadas, material__extra, valor_final = calcular_extras(
        valor_final_ingresso, num_oficinas, existe_material_extra
    )
    valor_desconto, valor_taxa_admin, total_final = aplicar_desconto(
        valor_final, num_cupons, taxa_admin=5
    )
    tipo_inscricao = classificar_participacao(
        num_oficinas, existe_material_extra, total_final
    )
    return (
        valor_final_ingresso,
        oficinas_contabilizadas,
        material__extra,
        valor_desconto,
        valor_taxa_admin,
        total_final,
        tipo_inscricao,
    )
