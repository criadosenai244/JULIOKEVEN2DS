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