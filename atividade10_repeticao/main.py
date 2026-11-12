# WHILE EXTERNO - MANTÉM O PROGRAMA RODANDO ENQUANTO O USUÁRIO QUISER CONTINUAR
continuar = 's'

while continuar == 's':
    # Solicita um número inteiro para gerar a tabuada
    numero = int(input('\nDigite um número inteiro: '))

    print(f'--- Tabuada do {numero} ---')

    # FOR - RANGE(1, 11) - PERCORRE DE 1 ATÉ 10
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

    # Pergunta se quer continuar e padroniza a resposta para minúsculo
    continuar = input('\nDeseja ver outra tabuada? (s/n): ').lower()

print('\nPrograma encerrado. Até a próxima!')