lista_pendentes = ["relatorio.pdf", "foto png", "planilha.xlsx"]
concluidos = []

print("estado inicial: ")
print(f"pendentes: {pendenetes}")
print(f"concluidos: {concluidos}")
print()

arquivo = lista.pendentes.pop(0)
concluidos.append(arquivo)

print("apos transaferencia:")
print(f"pendentes: {pendentes}") 
print(f"concluidos: {concluidos}") 
