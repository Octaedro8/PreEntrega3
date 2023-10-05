from django.db import models

class Menu(models.Model):
    categoria = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    precio = models.FloatField()
    disponible = models.BooleanField()

    def __str__(self):
        return self.descripcion

class Locales(models.Model):
    local = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    cp = models.CharField(max_length=8)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    apellido = models.CharField(max_length=30)
