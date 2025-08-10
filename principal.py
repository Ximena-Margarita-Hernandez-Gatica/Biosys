#Menú Principal
import flet as ft
import Interfaz_RegiDatos as IRD
import ConsultasUsu as CS
import alta_usuario as AU
import ConsultaBioEner as CBE
import main as mn

def main(page: ft.Page):
    page.clean()
    page.scroll = None
    # Configuración de la pagina
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = "Menú Principal"
    #page.window.width = 800
    #page.window.height = 600
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }

    # Funciones para abrir las otras páginas
    def mostrar_consultaBio(e):
        page.clean()
        CBE.main(page)

    def mostrar_registrodatos(e):
        page.clean()
        IRD.main(page)

    def mostrar_consultasUsu(e):
        page.clean()
        CS.main(page)

    def mostrar_altaUsu(e):
        page.clean()
        AU.main(page)

    def cerrar_sesion(e):
        page.clean()
        mn.main(page)

    # AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Sistema de Gestión de Bionergías", font_family="Kanit", size=40),
        center_title=True,
        leading=ft.Icon("ENERGY_SAVINGS_LEAF",size=30),
        color="black",
        bgcolor=ft.Colors.RED_100,
    )

    # Menú principal
    menubar = ft.MenuBar(
        expand=False,
        style=ft.MenuStyle(
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.RED_100
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Bioenergías",size=18,weight="bold",color="black"),
                leading=ft.Icon("ENERGY_SAVINGS_LEAF_OUTLINED",size=22),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Consulta de bioenergías",color="black"),
                        leading=ft.Icon("CONTENT_PASTE_SEARCH",size=20),
                        on_click=mostrar_consultaBio
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Registro de bioenergías",color="black"),
                        leading=ft.Icon("ENERGY_SAVINGS_LEAF_OUTLINED",size=20),
                        on_click=mostrar_registrodatos
                    ),
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text("Usuarios",size=18,weight="bold",color="black"),
                leading=ft.Icon("SUPERVISED_USER_CIRCLE_OUTLINED",size=22),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Consulta de usuarios",color="black"),
                        leading=ft.Icon("PERSON_SEARCH",size=20),
                        on_click=mostrar_consultasUsu
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Registro de usuarios (altas)",color="black"),
                        leading=ft.Icon("PERSON_ADD",size=20),
                        on_click=mostrar_altaUsu
                    ),
                ]
            ),
            ft.MenuItemButton(
                content=ft.Text("Cerrar sesión",size=18,weight="bold",color="black"),
                leading=ft.Icon("CLOSE",size=22),
                on_click=cerrar_sesion
            )
        ]
    )

    #Fondo e integración del menú
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    menubar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
    )
    )
        
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

