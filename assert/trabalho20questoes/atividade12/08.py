def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2 

def verificar_situacao(media):
# 4. Se a função fosse alterada para media > 6, qual teste falharia?
# O teste da média 6 falharia, porque 6 não é maior que 6.
# A função retornaria "Reprovado", mas o teste espera "Aprovado".
    if media >=6:
        return "aprovado"
    return "reprovado"

# para criar a função para calcular a média 
assert calcular_media(8, 6) == 7
assert calcular_media(10, 10) == 10
assert calcular_media(0, 0) == 0

assert verificar_situacao(7) == "Aprovado"
# 2. Qual teste verifica o valor mínimo para aprovação?
# Este teste verifica o valor mínimo, que é 6
assert verificar_situacao(6) == "Aprovado"                
# 3. Por que testar a nota 5.9 é importante?
# Porque 5.9 está abaixo de 6 e verifica se uma média menor
# que 6 é considerada "Reprovado".
assert verificar_situacao(5.9) == "Reprovado"

print("Todos os testes passaram!")

# 1. O que acontece quando todos os testes passam?
# O programa continuara normalmente e mostra a mensagem
# "Todos os testes passaram!".