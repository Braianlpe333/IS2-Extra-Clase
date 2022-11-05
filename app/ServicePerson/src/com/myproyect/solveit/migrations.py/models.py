from django.db import models

class Ciudad(models.Model):
    codigo = models.PositiveIntegerField(default=0, primary_key=True)
    descripcion = models.CharField(max_lenght=50)
    
class Corregimiento(models.Model):
    codigo = models.PositiveIntegerField(default=0, primary_key=True)
    descripcion = models.CharField(max_lenght=50)
    
class Zona(models.Model):
    codigo = models.PositiveIntegerField(default=0, primary_key=True)
    descripcion = models.CharField(max_lenght=50)
    
class 
    
