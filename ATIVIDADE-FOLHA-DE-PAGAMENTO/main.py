# Lista vazia para armazenar os salários dos 5 funcionários
salarios = []

# Laço de repetição para coletar os 5 salários
for i in range(5):
    valor = float(input(f"Digite o salário do {i + 1}º funcionário: R$ "))
    salarios.append(valor)

# Cálculos estatísticos usando funções built-in (sum, len, max, min)
total_folha = sum(salarios)
media_salarial = total_folha / len(salarios)
maior_salario = max(salarios)
menor_salario = min(salarios)

# Contagem de quantos funcionários ganham acima da média
acima_da_media = 0
for s in salarios:
    if s > media_salarial:
        acima_da_media += 1

# Exibição do relatório final formatado com 2 casas decimais
print("\n" + "=" * 40)
print("     RELATÓRIO DA FOLHA DE PAGAMENTO")
print("=" * 40)
print(f"Total da folha de pagamento: R$ {total_folha:.2f}")
print(f"Média salarial:              R$ {media_salarial:.2f}")
print(f"Maior salário:               R$ {maior_salario:.2f}")
print(f"Menor salário:               R$ {menor_salario:.2f}")
print(f"Funcionários acima da média: {acima_da_media}")
print("=" * 40)