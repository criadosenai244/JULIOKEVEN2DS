import flet as ft

def main(page: ft.Page):
    page.title = "Saudação"
    page.window.width = 400
    page.window.height = 700

    campo_nome = ft.TextField(label="Digite seu nome")
    mensagem = ft.Text(size=30)

    def saudar(e):
        """Mostrar uma saudação com o nome digitado"""
        if  campo_nome.value == "":
            mensagem.value = 'digite seu nome antes de clicar'
        else:
            mensagem.value = f"Olá, {campo_nome.value}!" 
            campo_nome.value = ""
        page.update()

    botao = ft.Button("Saudar", on_click=saudar)
    page.add(campo_nome, botao, mensagem)

ft.run(main)
