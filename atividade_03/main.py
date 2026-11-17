numero1 = float(input('Digite o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))
operacao = input('Escolha entre (+, -, *, /):')

if operacao == '+' :
    resultado = numero1 + numero2
    print('O resultado é:', resultado)
elif operacao == '-' :
    resultado = numero1 - numero2
    print('O resultado é:', resultado)
elif operacao == '*' :
    resultado = numero1 * numero2
    print('O resultado é:', resultado)
elif operacao == '/':
    resultado = numero1 / numero2
    print(f'O resultado é: {resultado:.2f}')
