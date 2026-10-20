
# Parte 2 — Identificar tipos 



# Etapa A — Sem executar nada

# a) "Brasília" -> str
# b) 42 -> int
# c) 3.14 -> float
# d) True -> bool
# e) "42" -> str
# f) -7 -> int
# g) 0.5 -> float
# h) False -> bool
# i) "True" -> str
# j) 1000000 -> int
# k) "" -> str
# l) 2.0 -> float


# Etapa B — Confira com o Python

print(type("Brasília"))
print(type(42))
print(type(3.14))
print(type(True))
print(type("42"))
print(type(-7))
print(type(0.5))
print(type(False))
print(type("True"))
print(type(1000000))
print(type(""))
print(type(2.0))


# Etapa C — Reflexão

# 1. Quantas respostas da Etapa A você acertou?
# Resposta: Acertei todas as 12 respostas.

# 2. Por que "42" e "True" são do tipo str?
# Resposta: Porque estão delimitados por aspas. Qualquer valor contido entre aspas é interpretado pelo Python como texto (string), independentemente de conter números ou palavras reservadas.

# 3. Por que 2.0 é float, e não int?
# Resposta: Porque contém um ponto decimal (.0). Em Python, a presença do ponto decimal define a variável como sendo de ponto flutuante (float), mesmo que a parte fracionária seja zero.