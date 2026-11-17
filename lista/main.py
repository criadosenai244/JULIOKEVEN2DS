#Lista para amarzenar os salários coletados
salarios = []

#Laço de coleta: solicita 5 salários e adiciona à lista 
for i in range(1, 6):
    salario = float(input(f'Salário do Funcionário {i}: '))
    salarios.append(salario)

#Cálculos
total = sum(salarios)
media = total / len(salarios)
maior = max(salarios)
menor = min(salarios)

#Conta quantos funcionários ganham acima da média
acima = sum(1 for s in salarios if s > media)

print(f'Salários registrados:{salarios}')
print(f'Média salarial: R$ {media:>8.2f}')
print(f'Maior salário: R$ {maior:>8.2f}')
print(f'Menor salário: R$ {menor:>8.2f}')
print(f'Acima da média: R$ {acima} funcionários(s)')
print(f'Total da folha : R$ {total:>8.2f}')



