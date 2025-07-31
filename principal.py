import flet as ft

def main (page: ft.Page):
    #Configuración de la pagina
    page.theme_mode = "light" 
    page.title = "Menú Principal" 
    page.appbar = ft.AppBar (
        title= ft.Text ("Sistema de Gestión de Bionergías",font_family="Kanit",size=30),
        center_title=True,
        leading= ft.Icon ("ENERGY_SAVINGS_LEAF"),
        color = "black",
        bgcolor= ft.Colors.RED_100,
    )
    #Componentes de la pagina
    btn_registro = ft.ElevatedButton (on_click= mostrar_registro)
    btn_consulta = ft.ElevatedButton("Consulta")

    #Añadir a la pagina y actualizar
    page.add(btn_registro,btn_consulta) 
    page.update() 

if __name__ == "__main__":
    ft.app(target=main,view= ft.AppView.WEB_BROWSER)