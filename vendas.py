def analisar_vendas(nome, lista_vendas, meta_mensal):
    soma = 0

    for venda in lista_vendas:
    soma = soma + venda 

    media = soma / len(lista_vendas) 

    if media >= meta_mensal:
    resultado = "bateu a meta"
    else:
    resultado = "não bateu a meta" 


return "o vendedor", nome, "teve media de", media, "e", resultado


nome = "carlos" 
vendas = [1200, 1500, 1100, 1900] 
meta = 1400 

print(analisar_vendas(nome, vendas, meta))



