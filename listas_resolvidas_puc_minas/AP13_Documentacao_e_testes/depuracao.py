#### O problema da função anterior é justamente o caso de borda, por isso ao passar o caso: [70,80,90] o resultado foi correto, por que não possuia caso de borda


### erro é ter usado > quando a regra estabelecida para os critérios de aprovação exige >=.

def contar_aprovados(notas):
    quantidade = 0

    # A condição original utilizava ">"
    # Isso excluía estudantes com nota exatamente igual a 60,
    # embora a regra de aprovação seja nota maior ou igual a 60.
    for nota in notas:
        if nota >= 60:
            quantidade += 1

    return quantidade


# Testes

assert contar_aprovados([70, 80, 90]) == 3

# Caso que revela o defeito
assert contar_aprovados([60]) == 1

# Mistura de aprovados e reprovados
assert contar_aprovados([50, 60, 70]) == 2

# Nenhum aprovado
assert contar_aprovados([10, 20, 30]) == 0

print("Todos os testes passaram!")