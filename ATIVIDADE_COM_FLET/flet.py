import flet as ft


def main(page: ft.Page):
    page.title = "Contador"
    page.window.width = 400
    page.window.height = 700

    numero = ft.Text("0", size=30)

    def somar(e):
        numero.value = str(int(numero.value) + 1)
        page.update()

    def subtrair(e):
        numero.value = str(int(numero.value) - 1)
        page.update()

    def zerar(e):
        numero.value = "0"
        page.update()

    page.add(
        numero,
        ft.Button("+1", on_click=somar),
        ft.Button("-1", on_click=subtrair),
        ft.Button("Zerar", on_click=zerar),
    )


ft.run(main)