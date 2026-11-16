from questao_5 import (
    calcular_media,
    classificar_turma,
    contar_aprovados,
    encontrar_maior_nota,
    encontrar_menor_nota,
    gerar_relatorio,
)


### Testes de Média:
def test_calcular_media():
    assert calcular_media([50,70,90]) == 70
    assert calcular_media([100]) == 100
    assert calcular_media([60, 60, 60]) == 60


# Testes da maior nota
def test_encontrar_maior_nota():
    assert encontrar_maior_nota([50, 70, 90]) == 90
    assert encontrar_maior_nota([80, 80, 60]) == 80

# Testes da menor nota
def test_encontrar_menor_nota():
    assert encontrar_menor_nota([50, 70, 90]) == 50
    assert encontrar_menor_nota([80, 80, 60]) == 60

# Testes de aprovados
def test_contar_aprovados():
    assert contar_aprovados([50, 60, 70]) == 2
    assert contar_aprovados([10, 20, 30]) == 0
    assert contar_aprovados([60, 60, 60]) == 3

def test_classificar_turma():
    # Testes de classificação da turma
    assert classificar_turma([80, 80, 80]) == "Turma Excelente"   # média 80
    assert classificar_turma([60, 60, 60]) == "Turma Regular"     # média 60
    assert classificar_turma([59, 59, 59]) == "Turma em Atenção"  # abaixo de 60
    assert classificar_turma([79, 79, 79]) == "Turma Regular"     # abaixo de 80
def test_gerar_relatorio_turma():
    # Turma com notas diferentes
    assert gerar_relatorio([40, 70, 100]) == {
        "media": 70,
        "maior": 100,
        "menor": 40,
        "aprovados": 2,
        "classificacao": "Turma Regular"
    }

    # Apenas um estudante
    assert gerar_relatorio([100]) == {
        "media": 100,
        "maior": 100,
        "menor": 100,
        "aprovados": 1,
        "classificacao": "Turma Excelente"
    }

    # Nenhum aprovado
    assert gerar_relatorio([10, 20, 30]) == {
        "media": 20,
        "maior": 30,
        "menor": 10,
        "aprovados": 0,
        "classificacao": "Turma em Atenção"
    }
