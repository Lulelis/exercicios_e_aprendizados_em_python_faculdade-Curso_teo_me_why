### Observações Importantes:


#### Exercício 1:

### 1) calcular_preco_cafe(preco_base, acrescimo=0)

# Crie uma função que receba o preço base de um café e um acréscimo opcional
# referente ao tamanho escolhido. A função deve retornar o preço final da bebida.

# Exemplo:

# Entrada: preco_base = 8.0, acrescimo = 2.0
# Saída esperada: 10.0
# -----------------------------------------------------------------------------#


def calcular_preco_cafe(preco_base, acrescimo=0):
    resultado = preco_base + acrescimo
    return resultado


### 2- 2) calcular_acompanhamento(preco, desconto=0)

# Crie uma função que receba o preço de um acompanhamento e um desconto percentual
# opcional. A função deve retornar o valor final do acompanhamento após aplicar
# o desconto informado.


def calcular_acompanhamento(preco, desconto=0):
    preco_cafe_com_desconto = preco - (preco * desconto / 100)
    return preco_cafe_com_desconto


### 3) resumo_item(nome, valor)

####Crie uma função que receba o nome de um item e seu valor final. A função deve
# retornar dois valores: uma string com a descrição do item e o valor formatado para exibição.

# Exemplo:

# Entrada: nome = "Capuccino", valor = 10.5
# Saída esperada: ("Capuccino", "R$ 10.50")


def resumo_item(nome, valor):
    return nome, f"R$ {valor:.2f}"


### 4) 4) calcular_totais(valor1, valor2, taxa_servico=10)

# Crie uma função que receba os valores de dois itens e uma taxa de serviço opcional.
# A função deve retornar três valores: subtotal, valor da taxa e total final do pedido.

# Exemplo:

# Entrada: valor1 = 10.0, valor2 = 8.0, taxa_servico = 10
# Saída esperada: (18.0, 1.8, 19.8)


def calcular_totais(valor_1, valor_2, taxa_servico):
    subtotal = valor_1 + valor_2
    valor_taxa = (taxa_servico / 100) * subtotal
    total_final_com_taxa = subtotal + valor_taxa
    return subtotal, valor_taxa, total_final_com_taxa
