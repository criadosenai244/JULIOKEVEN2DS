"""
Exercício 1 - Ficha de produto
Manipulação básica de dicionários (criação, leitura, atualização e iteração).
"""

# 1. Crie o dicionário produto com as chaves nome, preco e quantidade
produto = {
    "nome": "Teclado Mecânico",
    "preco": 249.90,
    "quantidade": 15
}

# 2. Mostre o nome e o preço
print(f"Produto: {produto['nome']} | Preço: R$ {produto['preco']:.2f}")

# 3. Altere a quantidade para 50
produto["quantidade"] = 50

# 4. Adicione a chave categoria
produto["categoria"] = "Periféricos"

# 5. Com um for, mostre todos os campos no formato chave: valor
print("\nFicha completa do produto:")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")




### Exercício 2 (`ex02.py`)


"""
Exercício 2 - Notas da turma
Iteração sobre uma lista de dicionários e cálculo de média.
"""

# 1. Crie a lista alunos com três dicionários
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 7.0},
    {"nome": "Carla", "nota": 9.5}
]

soma_notas = 0.0

# 2. Mostre cada aluno e 3. Some as notas dentro do for
for aluno in alunos:
    print(f"{aluno['nome']} - nota {aluno['nota']}")
    soma_notas += aluno["nota"]

# Calcule e mostre a média da turma
media = soma_notas / len(alunos)
print(f"\nMédia da turma: {media:.2f}")


### Exercício 3 (`ex03.py`)

"""
Exercício 3 - Leitura segura
Validação de entrada numérica decimal utilizando tratamento de exceções.
"""


def ler_decimal(mensagem: str) -> float:
    """
    Solicita um número decimal ao usuário repetidamente até receber um valor válido.

    Args:
        mensagem (str): O texto exibido ao solicitar a entrada do usuário.

    Returns:
        float: O número decimal válido inserido pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número.")


# Teste pedindo a altura do usuário
altura = ler_decimal("Digite a sua altura (ex: 1.75): ")
print(f"Altura registada: {altura} m")
