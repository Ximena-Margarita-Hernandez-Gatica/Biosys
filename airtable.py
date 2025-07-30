from pyairtable.orm import Model
from pyairtable.orm import fields

#Concectarse a la BD en airtable (conexion en la nube)
class Bioenergia(Model):
    cultivo = fields.TextField("cultivo")
    parte = fields.TextField("parte")
    cantidad = fields.FloatField("cantidad")
    humedad = fields.FloatField ("humedad")
    area = fields.FloatField("area")
    contenido_energetico = fields.FloatField("contenido_energetico")
    municipio = fields.SelectField("municipio")
    latitud = fields.FloatField("latitud")
    longitud = fields.FloatField("longitud")
    class Meta:
        api_key = "patRC60Nf2OXWhGUa.1c566a0abfeabbb2aa5577d73bb13d2b22740c6addcd6c017023a6c6913dfa6d"
        base_id = "appm1EPT4yoxFMFP7"
        table_name = "bionergia"

class Usuario (Model):
        clave = fields.TextField("clave")
        contra = fields.TextField ("contra")
        nombre = fields.TextField("nombre")
        admin = fields.CheckboxField ("admin")
        class Meta:
            api_key = "patRC60Nf2OXWhGUa.1c566a0abfeabbb2aa5577d73bb13d2b22740c6addcd6c017023a6c6913dfa6d"
            base_id = "appm1EPT4yoxFMFP7"
            table_name = "Usuario"
"""
#Creae un nuevo registro y guardarlo
cacao = Bioenergia(
    cultivo = "Cacao",
    parte = "Cascara",
    cantidad = 50.0,
    humedad = 20.0,
    area = 25.0,
    contenido_energetico = 120.0,
    municipio = "Cunduacán",
    latitud = 18.08729035,
    longitud = -93.23213562,
)
"""

"""
from pyairtable import Api

api = Api("patRC60Nf2OXWhGUa.1c566a0abfeabbb2aa5577d73bb13d2b22740c6addcd6c017023a6c6913dfa6d") #Para buscar la base de datos en la nube
tabla = api.table("appm1EPT4yoxFMFP7","Usuario") #(identificador_bd,nombre_tabla)-> el Identificador de la BD se consulta con airtable.com/api

#Altas
yo= {
    'clave': '012', 
    'contra': 'hola', 
    'nombre': 'Ximena', 
    'admin': 1
}

tabla.create(yo) #Mandar los datos a airtable


#Consultas
registros = tabla.all ()
for r in registros:
    print (r["fields"]) # airtable a cada registro de asigna un ID y fecha_registro en automatico y los datos que queremos los guarda en  en la seccion "fields" 
"""
