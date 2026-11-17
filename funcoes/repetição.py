# WHILE
contador = 1

while contador <= 5:
    print(f'Contagem: {contador}')
    contador += 1

print('Fim')

# ===================
SENHA = 'senai2026'
tentativas = 0
MAX = 3

while tentativas < MAX:
    senha = input('Digite a senha: ')
    tentativas += 1

    if senha == SENHA:
        print('Acesso concedido')
        break
    else:
        restantes = MAX - tentativas
        if restantes > 0:
            print(f'{restantes} tentativas restantes')
if tentativas == MAX and senha != SENHA:
    print('Conta bloqueada')


    # FRO - RANGE

# Imprimir números de 0 a 4
for i in range(5):
    print(i, end='')
print()

# Imprimir 6 dígitos: 0, 1, 2, 3, 4, 5
for i in range(6):
    print(i, end='')
print()

# Imprimir números pares: 0, 2, 4, 6, 8, 10
for i in range(0, 11, 2):
    print(i, end='')
print()

# Contagem regressiva de 11 até 1
for i in range(11, 0, -1):
    print(i, end='')
print()

    
#BREACK e CONTINUE
#break - para o loop
for n in range(1,11):
    if n ==6:
        print('Achei o 6! Parando')
        break
    print(n,end='')

    #Continue - pula a interação atual
    for n in range(1, 11):
        if n % 2 == 0: #pula pares 
            continue
    print(n, end='')


