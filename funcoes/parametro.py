#função co um parâmetro
def exibir_cabecalho(titulo):
    print('=' * 30)
    print(titulo)
    print('=' * 30)

exibir_cabecalho ('Cadastro de Alunos')
exibir_cabecalho ('Relatório de Notas')

#Vários parâmetros
def apresentar_aluno(nome,curso, idade):
    print(nome, 'tem', iade, 'anos e estuda', curso)

    apresentar_aluno('fulano',' DS', '17')
    apresentar_aluno('fulano',' DS', '17')

#Valor Padrao
def calcular_aluno(nome, percentual = 10):
    desconto = valor * percentual / 100
    print ('desconto:', desconto)
    calcular_desconto(200)  #usa 10%