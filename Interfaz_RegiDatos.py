#Registro de Bioenergias
import flet as ft
from airtable import Bioenergia
import principal as pl

def main (page: ft.Page):
    #Listas de Cultivo Origen,Parte Aprovechada y Municipio
    Cul_Ori = ["Hoja","Caña de azúcar","Cacao","Maíz","Coco","Plátano"]
    cultivo_dropdown = ft.Dropdown(
        label="Cultivo Origen",
        options=[ft.dropdown.Option(text) for text in Cul_Ori]
    )

    Par_Aprov = ["Tallo", "Cáscara","Bagazo","Rastrojo"]
    parte_dropdown = ft.Dropdown(
        label="Parte Aprovechada",width=300,
        options=[ft.dropdown.Option(text) for text in Par_Aprov]
    )

    Municipio = [
        "Balancán",
        "Cárdenas",
        "Centla",
        "Centro/Villahermosa",
        "Comalcalco",
        "Cunduacán",
        "Emiliano Zapata",
        "Huimanguillo",
        "Jalapa",
        "Jalpa de Méndez",
        "Jonuta",
        "Macuspana",
        "Nacajuca",
        "Paraíso",
        "Tacotalpa",
        "Teapa",
        "Tenosique",
    ]
    municipio_dropdown = ft.Dropdown(
        label="Municipio",
        options=[ft.dropdown.Option(text) for text in Municipio]
    )

    #Campos de textos
    cantidad = ft.TextField(label="Cantidad (Ton)", keyboard_type=ft.KeyboardType.NUMBER,width=300)
    humedad = ft.TextField(label="% Humedad", keyboard_type=ft.KeyboardType.NUMBER,width=300)
    area = ft.TextField(label="Área Cultivada", keyboard_type=ft.KeyboardType.NUMBER,width=300)
    contenido = ft.TextField(label="Contenido Energético", keyboard_type=ft.KeyboardType.NUMBER,width=300)
    latitud = ft.TextField(label="Latitud", keyboard_type=ft.KeyboardType.NUMBER,width=300)
    longitud = ft.TextField(label="Longitud", keyboard_type=ft.KeyboardType.NUMBER,width=300)
    
    #Snackbar
    snackbar = ft.SnackBar(content=None,show_close_icon=True,duration=4000,bgcolor=ft.Colors.RED_100)

    # Botón para guardar los datos
    def guardar_datos(e):
        #Validar que los campos no esten vacios
        campos = [
            (cultivo_dropdown, "Cultivo Origen"),
            (parte_dropdown, "Parte Aprovechada"),
            (cantidad, "Cantidad (Ton)"),
            (humedad, "% Humedad"),
            (area, "Área Cultivada"),
            (contenido, "Contenido Energético"),
            (municipio_dropdown, "Municipio"),
            (latitud, "Latitud"),
            (longitud, "Longitud"),
        ]
        for campo,nombre in campos:
            if campo.value in (None, ""):
                snackbar.content = ft.Text(f"Por favor, completa el campo: {nombre}", color="black")
                page.open(snackbar)
                return

        #Guardar datos
        try:
            nuevo_registro = Bioenergia(
                cultivo=cultivo_dropdown.value,
                parte=parte_dropdown.value,
                cantidad=float(cantidad.value),
                humedad=float(humedad.value),
                area=float(area.value),
                contenido_energetico=float(contenido.value),
                municipio=municipio_dropdown.value,
                latitud=float(latitud.value),
                longitud=float(longitud.value)
            )
            nuevo_registro.save()
            snackbar.content = ft.Text("¡Datos guardados exitosamente!", color="black")
            page.open(snackbar)
        except Exception as err:
            snackbar.content = ft.Text(f"Error al guardar: {err}", color="black")
            page.open(snackbar)

        page.update()
    #Botones
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

    btn_guardar = ft.ElevatedButton(
        "Guardar Datos",
        color="black",
        bgcolor= ft.Colors.RED_200,
        icon= "SAVE",
        icon_color = "black",
        on_click=guardar_datos
    )
    
    #Configuracion de la pagina
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = ft.ScrollMode.AUTO
    page.title = "Registro de datos"
    #page.window.width = 1000 
    #page.window.height = 800 
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }

    #Titulos 
    txt_titulo = ft.Text ("REGISTRO DE BIOMASAS", size=70, color=ft.Colors.RED_100,font_family="Kanit")
    txt_CultOrigen = ft.Text ("Origen Del Cultivo", size=30, color="black",font_family="Consolas")
    txt_Cultparte = ft.Text ("Información Del Cultivo", size=30, color="black",font_family="Consolas")
    txt_Coorde = ft.Text ("Coordenadas", size=30, color="black",font_family="Consolas")

    #Agregar componentes y actualizar la pagina
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Row(
                [
                    ft.Column(
                        [
                            txt_titulo,
                            txt_CultOrigen,
                            cultivo_dropdown,
                            txt_Cultparte,
                            parte_dropdown,
                            cantidad,
                            humedad,
                            area,
                            contenido,
                            municipio_dropdown,
                            txt_Coorde,
                            latitud,
                            longitud,
                            btn_guardar,
                            btn_regresar,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app (target = main, assets_dir="assets",view= ft.AppView.WEB_BROWSER)