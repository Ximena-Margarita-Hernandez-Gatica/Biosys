import peewee as pw

base_datos = pw.SqliteDatabase("Biomasa.db")

class Biomasa(pw.Model):
    cultivo = pw.TextField()
    parte = pw.TextField()
    cantidad = pw.FloatField()
    humedad = pw.FloatField()
    area = pw.FloatField()
    contenido_energetico = pw.FloatField()
    municipio = pw.TextField()
    latitud = pw.FloatField()
    longitud = pw.FloatField()

    class Meta:
        database = base_datos


#Este archivo seria para conectar el registro de biomasas con MYSQL (conexcion local)