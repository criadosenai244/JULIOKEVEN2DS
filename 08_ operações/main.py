#Operadores aritmeticos
numero1 = 17
numero2 = 5

print(numero1 + numero2) # Adição 
print(numero1 - numero2) # Subtração
print (numero1 * numero2) #Multiplicação 
print(numero1 / numero2) #Divisão (sempre float)
print(numero1 // numero2) #Divisao interia (descarta o decimal)
print(numero1 % numero2) #Modulo (Resto da divisão)
print(numero1 ** numero2) #Potenciação

# Precendencia - igual a matematica
print (2 + 3 * 4) # 14 (não 20)
print((2 + 3) * 4) # 20


# operadores de atribuição
saldo = 1000
saldo += 500 # saldo = saldo + 500
saldo -= 200 # 1300
saldo *= 2 # 2600
print(saldo)


#Operadores relacionais 
x = 10 
y = 7

print(x == y) #False - igual a 
print(x != y) #True - diferente de
print(x > y) # True - maior que
print(x <= y) #False - menor que 
print(x >= y) #True - maior ou igual
print(x <= y) #False - menor ou igual

#Comparando String
nome = 'Ana'
print(nome == 'Ana') # true
print(nome == 'ana') #false (case-sensitive)


# Operadores lógicos: and, or, not
idade = 20
tem_carteira = True

#and: as duas condições precisam ser verdadeiras 
pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir) #true
