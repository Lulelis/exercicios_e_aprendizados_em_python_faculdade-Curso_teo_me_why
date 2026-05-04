#### Função Principal do Programa:


import exercicio_funcoes_3_funcoes_treino as ft


def main():
    # Primeira função: Calcular calorias
    calorias_treino = float(input("Informe a quantidade de calorias do Treino: "))
    bonus_caloria = float(input("Informe a quantidade de calorias do Bônus Opcional: "))
    total_gasto = ft.calcular_calorias(calorias_treino, bonus_caloria)

    # Segunda: Tempo gasto
    tempo_principal_treino = float(input("Informe o Tempo Principal do Treino: "))
    tempo_aquecimento = float(input("Informe o tempo de aquecimento, caso tenha: "))
    tempo_total = ft.calcular_tempo_treino(tempo_principal_treino, tempo_aquecimento)
    horas_treino, resto_em_minutos = ft.analisar_desempenho(tempo_total)

    # Terceira: Meta Semanal de Calorias
    meta_opcional = float(
        input("Informe a meta opcional de calorias; Opcional = 300: ")
    )
    diferenca_meta, foi_atingida, mensagem = ft.consolidar_treino(
        total_gasto, tempo_total, meta_opcional
    )

    # Relatório Final
    print(f"O total gasto de calorias foi de: {total_gasto}")
    print(
        f"O tempo gasto de treino foi de: {horas_treino} hrs e {resto_em_minutos} minutos"
    )
    print(f"A meta de calorias teve como resultado: {diferenca_meta}")
    print(f"Atingiu a meta? : {foi_atingida}")
    print(f"Resumo: {mensagem}")


if __name__ == "__main__":
    main()
