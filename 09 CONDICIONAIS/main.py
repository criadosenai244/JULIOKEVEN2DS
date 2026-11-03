#Estrutura Condicionais
idade = int(input('Digite sua idade: '))
#if simples
if idade >= 18:
    print('Maior de idade')
    print('Acesso Permitido')

else:
    print('Menor de idade')
    print('Acesso Negado')

#if/else
nota = float(input('Digite a nota do aluno: '))
if nota>= 7.0:
    print('Aprovado')
else:
    print ('Recuperação')

#if/elif/else
matematica = float(input('Digite a nota: '))
if matematica >= 9.0:
    conceito = 'A'
    situacao = 'Exelente'

elif matematica >= 7.0:
    conceito = 'B'
    situacao = 'Bom'

elif matematica >= 5.0:
    conceito = 'C'
    situacao = 'Regular'

else :
    conceito = 'D'
    situacao = 'Ruim'
    print(f'Conceito: {conceito} | Situação: {situacao}')

