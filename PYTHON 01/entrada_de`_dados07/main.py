# capitura texto
nome = ('Digite seu nome :')
print(f'Olá, {nome}')

#SEM conversão gera erro (errado para calculo)
# idade = input ('Idadde: ')
# print (idade + 1) TypeErro

#COM conversão (correto):
idade = int (input('Digite sua idade: '))
print(f'Você tem {idade}anos')
print(f'Em 10 anos você tera {idade + 10}ano')