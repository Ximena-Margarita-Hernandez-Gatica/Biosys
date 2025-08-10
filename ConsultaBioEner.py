#Consultar la Tabla de Bioenergias
import flet as ft
import principal as pl
import airtable as at

def main (page: ft.Page):
    #Configuración de la pagina
    page.title = "Consultas de Bioenergias"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.width = 1000 
    page.window.height = 800
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    page.appbar = ft.AppBar( 
        title= ft.Text ("Listado de Bioenergias",font_family="Kanit",size=40),
        center_title= True,
        leading= ft.Icon ("NATURE",size=30),
        bgcolor= ft.Colors.RED_100,
        color= "black",
    )
    #Tabla de Bioenergias
    encabezado = [
        ft.DataColumn(ft.Text("Origen del Cultivo")),
        ft.DataColumn(ft.Text("Parte Aprovechada")),
        ft.DataColumn(ft.Text("Cantidad (Toneladas)")),
        ft.DataColumn(ft.Text("Porcentaje de Humedad")),
        ft.DataColumn(ft.Text("Área Cultivada")),
        ft.DataColumn(ft.Text("Contenido Energetico")),
        ft.DataColumn(ft.Text("Municipio")),
        ft.DataColumn(ft.Text("Latitud")),
        ft.DataColumn(ft.Text("Longitud")),
    ]
    filas = []
    datos = at.Bioenergia.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.cultivo))
        celda2 = ft.DataCell(ft.Text(d.parte))
        celda3 = ft.DataCell(ft.Text(d.cantidad))
        celda4 = ft.DataCell(ft.Text(d.humedad))
        celda5 = ft.DataCell(ft.Text(d.area))
        celda6 = ft.DataCell(ft.Text(d.contenido_energetico))
        celda7 = ft.DataCell(ft.Text(d.municipio))
        celda8 = ft.DataCell(ft.Text(d.latitud))
        celda9 = ft.DataCell(ft.Text(d.longitud))
        fila = ft.DataRow([celda1,celda2,celda3,celda4,celda5,celda6,celda7,celda8,celda9])
        filas.append(fila)
    tbl_bioenergias = ft.DataTable(encabezado,filas)
    
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
    page.add(tbl_bioenergias,btn_regresar)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main,view= ft.AppView.WEB_BROWSER)