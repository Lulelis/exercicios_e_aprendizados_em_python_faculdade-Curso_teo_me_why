import exercicio_funcoes_4_funcoes_evento as fe


def main():
    for i in range(1, 4):
        nome_participante = input("Insira seu nome: ")
        tipo_ingresso = input("Qual o tipo de Ingresso: ")
        qtd_oficinas = int(input("Insira a quantidade de oficianas extras: "))
        material_extra = input("Deseja material extra: TRUE or FALSE:")
        cupom_desconto = float(input("Deseja Cupom Extra. Informe o valor "))
        ingresso_informado = tipo_ingresso
        valor_informado = valor_padrao
        num_oficinas = oficinas
        existe_material_extra = material_extra
        num_cupons = cupom
        valor_final_ingresso = fe.calcular_valor_base(
            ingresso_informado, valor_informado
        )
        oficinas_contabilizadas, material__extra, valor_final = fe.calcular_extras(
            valor_final_ingresso, num_oficinas, existe_material_extra
        )
        valor_desconto, valor_taxa_admin, total_final = fe.aplicar_desconto(
            valor_final, num_cupons, taxa_admin=5
        )
        tipo_inscricao = fe.classificar_participacao(
            num_oficinas, existe_material_extra, total_final
        )
        (
            nome_participante,
            ingresso,
            material_extra,
            valor_do_desconto,
            valor_da_taxa_admin,
            total_final,
            tipo_inscricao,
        ) = fe.gerar_relatorio_participante()
        print(f"O participante com nome: {nome_participante}")
        print(f"Tipo de Ingresso {tipo_ingresso}")
        print(f"O participante com nome: {nome_participante}")
        print(f"O participante com nome: {nome_participante}")
        print(f"O participante com nome: {nome_participante}")
        print(f"O participante com nome: {nome_participante}")
        print(f"O participante com nome: {nome_participante}")
        print(f"O participante com nome: {nome_participante}")


if __name__ == "__main__":
    main()
