import flet as ft
import airtable as at
import principal as pl

def main(page: ft.Page):
    #Funcion que hara el proceso de guardar al usuario
    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra2 = txt_contra2.value
        nombre = txt_nombre.value
        #Validar campos
        if clave == "":
            snackbar = ft.SnackBar (ft.Text("Introduce tu clave de usuario"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
            return
        elif contra == "":
            snackbar = ft.SnackBar (ft.Text("Introduce la contraseña"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
        elif contra2 == "":
            snackbar = ft.SnackBar (ft.Text("Confirma la contraseña"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
        elif nombre == "":
            snackbar = ft.SnackBar (ft.Text("Introduce tu nombre"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
        #Confirmar contraseña
        if contra != contra2:
            snackbar = ft.SnackBar (ft.Text("Las contraseñas no coinciden"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
            return
        #Guardar usuario en la nube
        nuevo = at.Usuario(
            clave = clave,
            contra = contra,
            nombre = nombre,
            admin = chk_admin.value
        )
        try:
            nuevo.save()
            snackbar = ft.SnackBar (ft.Text("Usuario registrado"), bgcolor="green", show_close_icon=True)
            page.open(snackbar)
        except Exception:
            snackbar = ft.SnackBar (ft.Text(error), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
    
    def regresar (e: ft.ControlEvent):
        page.clean()
        pl.main(page)

    btn_regresar = ft.FilledButton (
        text= "Regresar a la pagina principal",
        color="black",
        bgcolor= ft.Colors.RED_100,
        icon= "ARROW_BACK",
        icon_color = "black",
        on_click = regresar
    )

    #Configuracion de la pagina
    page.title = "Altas"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.window.width = 800
    page.window.height = 600
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    page.appbar = ft.AppBar (
        title= ft.Text ("Nuevo Usuario",font_family="Kanit",size=30),
        center_title=True,
        leading= ft.Icon ("person_add"),
        color = "black",
        bgcolor= ft.Colors.RED_100,
    )
    #Componentes de la pagina
    txt_clave = ft.TextField (label="Clave de usuario",width=250)
    txt_contra = ft.TextField (label="Contraseña",password=True,width=250)
    txt_contra2 = ft.TextField (label="Confirmar contraseña",password=True,width=250)
    txt_nombre = ft.TextField (label="Nombre completo",width=250)
    chk_admin = ft.Checkbox(label="¿Es administrador?")
    btn_guardar = ft.FilledButton (
        text= "Guardar",
        #font_family="Consolas",
        icon= "save",
        bgcolor= "green",
        on_click= guardar_usuario,#LLama a la funcion para guardar usuario
    )
    btn_cancelar = ft.FilledButton (
        text= "Cancelar",
        icon= "cancel",
        bgcolor="red"
    )
    fila = ft.Row(controls=[btn_guardar,btn_cancelar])


    page.add (txt_clave,txt_contra,txt_contra2,txt_nombre,chk_admin,fila,btn_regresar)
    page.update()

if __name__ == "__main__":
    ft.app(target=main,view= ft.AppView.WEB_BROWSER)