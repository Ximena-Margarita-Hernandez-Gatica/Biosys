import flet as ft
#import principal as pr
#import airtable as at#
#Función principal
def main (page: ft.Page):

    #*Configuración de la pagina*
    page.theme_mode = "light" #Si queremos el modo oscuro escribiriamos "dark" en vez de "light"
    page.horizontal_alignment = "center" #Centrar(tambien se puede poner vertical)
    page.title = "Inicio de sesión" #Poner titulo a la pagina (se veria en lo que seria la pestaña de la pagina)
    
    #*Componentes de la pagina*
    #logo = ft.Icon ("person", size=60, color=ft.Colors.RED_100) #Poner el logo,configurar su tamaño y color (el icono se busca en "Flet Icons browser" y se escribe el nombre del icono [solo el nombre qu e va despues del icon.])
    #txt_bienvenido = ft.Text ("Bienvenid@", size=40,color=ft.Colors.RED_100) #Cartelito de bienvenida
    page.appbar = ft.AppBar (
        title= ft.Text ("Bienvenid@"),
        center_title=True,
        leading= ft.Icon ("person_add"),
        color = "black",
        bgcolor= ft.Colors.RED_100,
    )
    txt_usuario = ft.TextField (label="Username/Correo") #Poner el campo de texto en donde el usuario agregara su nombre/correo, ademas se configura ancho y largo de ese campo de texto
    txt_contra = ft.TextField (label="Contraseña", password=True,can_reveal_password=True) #Poner el campo de texto en donde el usuario agregara su contraseña, ademas se configura ancho y largo de ese campo de texto y ocultar la contraseña (can_reveal_password=True para el ojito que permite ocultar y ver la pagina)
    btn_login = ft.FilledButton ( #Si la linea es muy larga se puede ordenar como aqui
        "Iniciar sesión", 
        width=300,
        color="black",#Color de la letra del boton
        on_click = ingresar # Ejecutar un funcion que valide al usuario (que los campos no este vacios,etc)
        ) #Boton de inicion de sesión junto con un icono
    
    #*Agregar icono,caja del nombre/correo, caja de correo y todos los demas componentes a la pagina (que se puedan mostrar)*
    page.add(txt_usuario,txt_contra,btn_login) #Es importante agregarlar en el orden en que queremos que se muestre (en base a nuestro diseño)
#

    #*Actulizar la pagina*
    page.update() #Importante para que se vallan viendo los cambios


#Inicializar la aplicación
if __name__ == "__main__":
    ft.app (target = main, view= ft.AppView.WEB_BROWSER)