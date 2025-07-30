import flet as ft
from Conexion_RegiDatos import Biomasa
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
    
    mensaje = ft.Text("")

    Biomasa = Bioenergia
    # Botón para guardar los datos
    def guardar_datos(e):
        try:
            nuevo_registro = Biomasa.create(
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
            mensaje.value = "Datos guardados exitosamente"
            mensaje.color = "green"
        except Exception as err:
            mensaje.value = f"Error al guardar: {err}"
            mensaje.color = "red"
        page.update()
   
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

    btn_guardar = ft.ElevatedButton("Guardar Datos", on_click=guardar_datos)
    

    #Configuracion de la pagina
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.scroll = ft.ScrollMode.ALWAYS
    page.title = "Registro de datos"
    page.window.width = 1000 
    page.window.height = 800 
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }

    #Titulos 
    txt_bienvenido = ft.Text ("BIOMASA", size=70, color=ft.Colors.RED_100,font_family="Kanit")
    txt_CultOrigen = ft.Text ("Cultivo Origen", size=30, color="black",font_family="Consolas")
    txt_Cultparte = ft.Text ("Parte Aprovechada", size=30, color="black",font_family="Consolas")
    txt_Coorde = ft.Text ("Coordenadas", size=30, color="black",font_family="Consolas")

    #Agregar componentes y actualizar la pagina
    page.add(
        txt_bienvenido,
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
        mensaje
    )
    page.update()


if __name__ == "__main__":
    ft.app (target = main, assets_dir="assets")