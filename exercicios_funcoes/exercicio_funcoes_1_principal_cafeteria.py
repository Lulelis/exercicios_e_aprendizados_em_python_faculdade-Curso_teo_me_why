##### Lógica Principal do Programa


### Declarar o nome do arquivo contendo as funções de execução: exercicio_funcoes_1_funcoes_cafeteria

import exercicio_funcoes_1_funcoes_cafeteria as fc


def main():
    ### Construindo a lógica principal do programa:
    ### ler o nome e o preço base do café;
    nome_cafe = input("Digite o nome do café: ")
    preco_base = float(input("Digite o preço base do café: "))
    acrescimo = float(input("Digite o acréscimo sugerido: "))
    preco_cafe_final = fc.calcular_preco_cafe(preco_base, acrescimo)

    ### Acompanhamento:
    nome_acompanhamento = input("Digite o nome do acompanhamento: ")
    preco_acompanhamento = float(input("Digite o preço do acompanhamento: "))
    desconto = float(input("Digite o desconto do acompanhamento em %: "))
    preco_acompanhamento_final = fc.calcular_acompanhamento(
        preco_acompanhamento, desconto
    )

    ### Resumos:
    resumo_cafe = fc.resumo_item(nome_cafe, preco_cafe_final)
    resumo_acompanhamento = fc.resumo_item(
        nome_acompanhamento, preco_acompanhamento_final
    )

    ### Totais:
    taxa_servico = float(input("Informe a taxa de serviço %: "))
    subtotal, valor_taxa, total_final = fc.calcular_totais(
        preco_cafe_final, preco_acompanhamento_final, taxa_servico
    )

    ### Saída organizada:
    print("Resumo do Pedido")
    print("Café: ", resumo_cafe)
    print("Acompanhamento: ", resumo_acompanhamento)
    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Taxa de Serviço: R${valor_taxa:.2f}")
    print(f"Total Final: R$: {total_final:.2f}")


if __name__ == "__main__":
    main()
