#Conexión a Airtable
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
        table_name = "bioenergia"

class Usuario (Model):
        clave = fields.TextField("clave")
        contra = fields.TextField ("contra")
        nombre = fields.TextField("nombre")
        admin = fields.CheckboxField ("admin")
        class Meta:
            api_key = "patRC60Nf2OXWhGUa.1c566a0abfeabbb2aa5577d73bb13d2b22740c6addcd6c017023a6c6913dfa6d"
            base_id = "appm1EPT4yoxFMFP7"
            table_name = "Usuario"
