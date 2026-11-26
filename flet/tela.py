import flet as ft

def main (page: ft. Page):
    page.title = "Meu primeiro app"
    page.window.width = 400 
    page.window.height = 700

    titulo = ft.Text("Bem Vindo!!!", size=30,
                     weight= ft.FontWeight.BOLD, color=ft.Colors.BLUE) 
    subtitulo = ft.Text("Este eu meu primeiro APP" , size=16, color=ft.Colors.GREEN)
    aviso = ft.Text ("Feito com Python e flet", color= ft.Colors.BLUE)
  

    page.add(titulo, subtitulo, aviso , )
    
ft.run(main)