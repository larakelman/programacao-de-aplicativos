livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware: "]
livros_emprestados = []
emprestimo = input("digite o nome do livro que deseja: ") 

if livros_disponiveis in livros_emprestados:
    livros_disponiveis.remove(livros_emprestados)
    livros_emprestados.append(emprestimo)
    print(f"emprestimo realizado com sucesso!")

else:
    ("desculpe, este livro não está no acervo") 

livro = input("digite o nome do livro que está devolvendo: ")
if livro in livros_emprestados:
    livros_emprestados.remove(livros)
    livros_disponiveis.append(livros)
    print(f"este livro nao consta como emprestado") 

else:
    print("este livro nao e emprestado")  

del livros_disponiveis[0:2]
print (f"estado final das duas listas {livros_disponiveis} e {livros_emprestados}")


