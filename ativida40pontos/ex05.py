
# ex01 — Ficha pessoal
# 
nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")
curso = input("Curso: ")

print()
print("===== FICHA =====")
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)
print("Curso:", curso)


# 
# ex02 — Ano de nascimento
# 
nome = input("Nome: ")
idade = int(input("Idade: "))

# Variável com o ano atual
ano_atual = 2026

# Cálculo para estimar o ano de nascimento
ano_nascimento = ano_atual - idade

print(f"{nome} nasceu aproximadamente em {ano_nascimento}")


# 
# ex03 — Idade em dias
# 
idade = int(input("Idade: "))

# Cálculo da idade aproximada em meses (12/ano) e dias (365/ano)
meses = idade * 12
dias = idade * 365

print(f"Você tem aproximadamente {meses} meses")
print(f"Você tem aproximadamente {dias} dias")



# ex04 — Média de três notas

aluno = input("Aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

# Cálculo da média aritmética simples
media = (nota1 + nota2 + nota3) / 3

print(f"Média de {aluno}: {media}")


# ex05 — Conta do restaurante

conta = float(input("Valor da conta: "))

# Cálculo da taxa de serviço (10%) e do valor total
taxa = conta * 0.10
total = conta + taxa

print("Taxa de serviço:", taxa)
print("Total a pagar:", total)


# ex06 — Divisão da conta

valor_total = float(input("Valor total: "))
pessoas = int(input("Quantidade de pessoas: "))

# Cálculo da divisão do valor total pelo número de pessoas
cada_pessoa = valor_total / pessoas

print("Cada pessoa paga:", cada_pessoa)


# ex07 — Conversor de temperatura

celsius = float(input("Temperatura em Celsius: "))

# Conversão de Celsius para Fahrenheit (F = C * 9 / 5 + 32)
fahrenheit = celsius * 9 / 5 + 32

print("Temperatura em Fahrenheit:", fahrenheit)



# ex08 — Conversor de moeda

reais = float(input("Valor em reais: "))
cotacao = float(input("Cotação do dólar: "))

# Conversão de Reais para Dólares
dolares = reais / cotacao

print("Valor em dólares:", dolares)


# ex09 — Retângulo

base = float(input("Base: "))
altura = float(input("Altura: "))

# Cálculo da área e do perímetro do retângulo
area = base * altura
perimetro = 2 * base + 2 * altura

print(f"Área: {area} m²")
print(f"Perímetro: {perimetro} m")


# ex10 — Consumo de combustível

distancia = float(input("Distância (km): "))
litros = float(input("Litros consumidos: "))

# Cálculo do consumo médio em km/l
consumo = distancia / litros

print(f"Consumo: {consumo} km/l")


# ex11 — Aumento de salário

salario = float(input("Salário atual: "))
percentual = float(input("Percentual de aumento: "))

# Cálculo do valor do aumento e do novo salário
aumento = salario * percentual / 100
novo_salario = salario + aumento

print("Valor do aumento:", aumento)
print("Novo salário:", novo_salario)



# ex12 — Cadastro de produto

produto = input("Produto: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade: "))

# Definição da variável booleana de disponibilidade
disponivel = True

# Cálculo do valor total do estoque (preço * quantidade)
valor_total = preco * quantidade

print()
print("Produto:", produto)
print("Preço:", preco)
print("Quantidade:", quantidade)
print("Disponível:", disponivel)
print("Valor total em estoque:", valor_total)
print()
print("Tipo de nome:", type(produto))
print("Tipo de preço:", type(preco))
print("Tipo de quantidade:", type(quantidade))
print("Tipo de disponível:", type(disponivel))