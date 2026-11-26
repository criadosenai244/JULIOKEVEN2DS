import flet as ft

def main(page: ft.Page):
    page.title ="Calculadora"
    page.window.width = 400
    page.window.height = 700

    titulo = ft.Text ("Calculadora de Média", size = 26, weight= ft.FontWeight.BOLD)
    campo_nota1 = ft.TextField(label="Nota 1")
    campo_nota2 = ft.TextField(label= "Nota 2")
    campo_nota3 = ft.TextField(label= "Nota 3")
    campo_nota4 = ft.TextField(label= "Nota 4")
    resultado = ft.Text (size= 20)

    def calcular (e):
        try:
            nota1 = float(campo_nota1.value.replace(",","."))
            nota2 = float(campo_nota2.value.replace(",","."))
            nota3 = float(campo_nota3.value.replace(",","."))
            nota4 = float(campo_nota4.value.replace(",","."))

        except ValueError:
            resultado.value = "Digite notas válidas"
            resultado.color = ft.Colors.ORANGE
            page.update()
            return
    
        media= (nota1 + nota2 + nota3 + nota4) /4

        if media >= 7:
            resultado.value = "Média: " + str(media) + "Aprovado"
            resultado.color = ft.Colors.GREEN

        else:
            resultado.value = "Média: " + str(media) + "Reprovado"
            resultado.color = ft.Colors.RED
        page.update()

    botao = ft.Button ("Calcular", on_click=calcular)
    page.add (titulo, campo_nota1, campo_nota2, campo_nota3, campo_nota4,botao, resultado)
ft.run(main)