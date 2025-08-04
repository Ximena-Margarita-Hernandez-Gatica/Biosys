import flet as ft
import principal as pr
import airtable as at
from pyairtable.formulas import match

def main (page: ft.Page):

    def validar_usuario (e: ft.ControlEvent):
        usuario = txt_usuario.value
        contra = txt_contra.value
        snackbar = ft.SnackBar(content=None, bgcolor="red", show_close_icon=True)

        if usuario == "":
            snackbar.content = ft.Text("Introduce tu usuario")
            page.open(snackbar)
            return
        elif contra == "":
            snackbar.content = ft.Text("Introduce tu contraseña")
            page.open(snackbar)
            return

        # Verificar en la base de datos si los datos son correctos
        try:
            formula = match({"clave": usuario, "contra": contra})
            registro = at.Usuario.first(formula=formula)

            if registro:
                page.clean()
                pr.main(page)
                print (" Funciona !")
                snackbar.content = ft.Text(f"Bienvenid@ {registro.nombre}")
                page.open(snackbar)
            else:
                print (f" Usuario ’{ usuario }’ no encontrado .")
                snackbar.content = ft.Text(f"Usuario '{usuario}' no encontrado.")
                page.open(snackbar)

        except Exception as e:
            print (f" Error de Airtable : {e}")
            snackbar.content = ft.Text(f"Error de Airtable: {e}")
            page.open(snackbar)

    # Configuración de la página
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesión"
    page.window.width = 800
    page.window.height = 600
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }

    # Componentes de la página
    logo = ft.Icon("person", size=60, color=ft.Colors.RED_100)
    page.appbar = ft.AppBar(
        title=ft.Text("Bienvenid@", font_family="Kanit"),
        center_title=True,
        leading=ft.Icon("person_add"),
        color="black",
        bgcolor=ft.Colors.RED_100,
    )
    txt_usuario = ft.TextField(label="Username/Correo", width=250)
    txt_contra = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)
    btn_login = ft.FilledButton(
        "Iniciar sesión",
        icon=ft.Icons.LOGIN,
        width=300,
        color="black",
        bgcolor=ft.Colors.RED_100,
        on_click=validar_usuario  
    )

    page.add(logo, txt_usuario, txt_contra, btn_login)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)