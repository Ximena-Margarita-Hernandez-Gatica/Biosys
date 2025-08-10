#Consultar la Tabla de Usuarios
import flet as ft
import principal as pl
import airtable as at

def main (page: ft.Page):
    #Configuración de la pagina
    page.title = "Consultas de Usuarios"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    #page.window.width = 1000 
    #page.window.height = 800
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    page.appbar = ft.AppBar( 
        title= ft.Text ("Listado de Usuarios",font_family="Kanit",size=40),
        center_title= True,
        leading= ft.Icon ("cloud",size=30),
        bgcolor= ft.Colors.RED_100,
        color= "black"
    )
    #Tabla de usuario
    encabezado = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre Completo")),
        ft.DataColumn(ft.Text("¿Es administrador?"))
    ]
    filas = []
    datos = at.Usuario.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra,color="white",selectable=True,show_selection_cursor=True))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Text(d.admin))
        fila = ft.DataRow([celda1,celda2,celda3,celda4])
        filas.append(fila)
    tbl_usuarios = ft.DataTable(encabezado,filas)
    
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
    #Agregar componentes y actualizar la pagina 
    page.add(tbl_usuarios,btn_regresar)
 
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main,view= ft.AppView.WEB_BROWSER)


