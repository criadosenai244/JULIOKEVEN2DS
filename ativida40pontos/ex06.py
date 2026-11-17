
# Parte 6 — Desafio final (desafio.py)


# Entrada de dados
nome = input("Nome completo: ")
idade = int(input("Idade: "))
curso = input("Curso: ")
turno = input("Turno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

# Cálculos
matriculado = True
media = (nota1 + nota2) / 2
ano_nascimento = 2026 - idade

# Saída de dados
print()
print("===== COMPROVANTE DE MATRÍCULA =====")
print("Nome:", nome)
print("Idade:", idade)
print("Ano aproximado de nascimento:", ano_nascimento)
print("Curso:", curso)
print("Turno:", turno)
print("Média das notas:", media)
print("Matriculado:", matriculado)

print()
print("===== TIPOS DAS VARIÁVEIS =====")
print("nome:", type(nome))
print("idade:", type(idade))
print("curso:", type(curso))
print("turno:", type(turno))
print("media:", type(media))
print("matriculado:", type(matriculado))