from questao_5 import (
    calcular_media,
    classificar_turma,
    contar_aprovados,
    encontrar_maior_nota,
    encontrar_menor_nota,
)

### Testes de Média:

assert calcular_media([50,70,90]) == 70
print(calcular_media([50,70,90]))

assert calcular_media([100]) == 100
print(calcular_media([100]))
assert calcular_media([60, 60, 60]) == 60
print(calcular_media([60,60,60]))

# Testes da maior nota
assert encontrar_maior_nota([50, 70, 90]) == 90
print(encontrar_maior_nota([50, 70, 90]))

assert encontrar_maior_nota([80, 80, 60]) == 80
print(encontrar_maior_nota([80, 80, 60]))

# Testes da menor nota
assert encontrar_menor_nota([50, 70, 90]) == 50
assert encontrar_menor_nota([80, 80, 60]) == 60

# Testes de aprovados
assert contar_aprovados([50, 60, 70]) == 2
assert contar_aprovados([10, 20, 30]) == 0
assert contar_aprovados([60, 60, 60]) == 3

# Testes de classificação da turma
assert classificar_turma([80, 80, 80]) == "Turma Excelente"   # média 80
assert classificar_turma([60, 60, 60]) == "Turma Regular"     # média 60
assert classificar_turma([59, 59, 59]) == "Turma em Atenção"  # abaixo de 60
assert classificar_turma([79, 79, 79]) == "Turma Regular"     # abaixo de 80

print("Todos os testes passaram!")