import flet as ft
import Views.Prerequisitos

def main(page:ft.Page):
    tela = Views.Prerequisitos.view()
    page.add(tela)
ft.app(main)