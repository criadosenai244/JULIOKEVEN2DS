# Parte 3 — Encontre o erro (arquivo erros.py)


# Trecho A - NameError: o print estava com P maiúsculo.
print("Olá, turma!")

# Trecho B - SyntaxError: faltava fechar as aspas da string.
print("Bem-vindo ao SENAI")

# Trecho C - SyntaxError / NameError: o texto do valor atribuído à variável não estava entre aspas.
curso = "Desenvolvimento de Sistemas"
print(curso)

# Trecho D - NameError: o valor booleano True deve ser escrito com a primeira letra em maiúsculas.
ativo = True
print(ativo)

# Trecho E - SyntaxError: os nomes de variáveis não podem começar por números.
nome2 = "Ana"
print(nome2)

# Trecho F - SyntaxError: faltava uma vírgula a separar a string da variável dentro da função print.
total = 150
print("Total:", total)

# Trecho G - TypeError: a função input devolve uma string, por isso é necessário convertê-la para int antes de efetuar a soma.
idade = int(input("Digite sua idade: "))
print("Ano que vem você terá:", idade + 1)

# Trecho H - erro de lógica: em Python, as casas decimais são separadas por ponto (.) e não por vírgula (,).
preco = 10.50
print("Preço de duas unidades:", preco * 2)

# Trecho I - erro de lógica: faltavam os parênteses em (nota1 + nota2) para garantir que a soma é realizada antes da divisão por 2.
nota1 = 8
nota2 = 6
media = (nota1 + nota2) / 2
print("Média:", media)