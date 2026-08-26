def situacao_falta(faltas):
    if faltas <= 4:
        return "regular"
    
    elif faltas <=10:
        return "atenção"
    
    else:
        return "reprovado por falta"
    
assert situacao_falta(0) == "regular"
assert situacao_falta(4) == "regular"
assert situacao_falta(5) == "atencao"
assert situacao_falta(10) == "atencao"
assert situacao_falta(11) == "reprovado por falta"

# foi necessario adicionar as funções para classificar as faltas como "regular" , "atenção" , "reprovado por falta"

