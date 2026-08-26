def situacao_aluno(media):
    if media >= 6:
        return "aprovado"
    return "reprovado"

assert situacao_aluno(8) == "aprovado"
assert situacao_aluno(6) == "aprovado"
assert situacao_aluno(5.9) == "reprovado"
assert situacao_aluno(0) == "reprovado"
assert situacao_aluno(10) == "aprovado"

assert situacao_aluno(-1) == "reprovado"

print("todos os testes se passaram!")