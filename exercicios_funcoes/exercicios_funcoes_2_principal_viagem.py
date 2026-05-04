# Importanto as funções criadas em funcoes_viagem:

import exercicios_funcoes_2_funcoes_viagem as fv


def main():

    ### Passagem
    valor_passagem = float(input("Informe o valor da passagem: "))
    valor_hospedagem = float(input("Informe o valor da Hospedagem: "))
    valor_final_passagem = fv.calcular_passagem(valor_passagem, valor_hospedagem)
    print("O valor Final da passagem é ", valor_final_passagem)

    ### Hospedagem
    valor_diaria = float(input("O valor da diária é: "))
    dias = int(input("Informe a quantidade de dias: "))
    taxa_extra_opcional = float(input("Informe a taxa extra (opcional): "))
    valor_final_hospedagem = fv.calcular_hospedagem(
        valor_diaria, dias, taxa_extra_opcional
    )
    print(
        f"O valor da diária {valor_diaria}, em {dias} e com taxa extraopcional de {taxa_extra_opcional} possui valor final de: ",
        valor_final_hospedagem,
    )

    # Horas viagem
    horas_totais = float(input("Digite a duração da total da viagem em horas: "))
    dias, horas_restantes = fv.converter_duracao(horas_totais)
    print(dias, horas_restantes)

    ### Alimentacao e calculos finais:

    alimentacao = float(input("Insira o valor da alimentação: "))
    valor_final_passagem, valor_final_hospedagem, alimentacao = fv.calcular_orcamento(
        valor_final_hospedagem, valor_final_hospedagem, alimentacao
    )

    ### Resumo final viagem:
    print("O resumo Final da Viagem: ")
    print("O valor final da passagem foi: ", valor_final_passagem)
    print("O valor final da hospedagem ", valor_final_hospedagem)
    print(
        f"A duração da viagem foi de:{dias} e com um total de horas {horas_restantes}"
    )
    print(
        "O valor fixo foi de:",
        valor_final_hospedagem,
        valor_final_passagem,
        f"alimentação de:{alimentacao}",
    )


if __name__ == "__main__":
    main()
