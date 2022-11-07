from django.db import models

#Recordar manejo de nulos directamente desde aqui
class City(models.model):
    code = models.AutoField(default=0, primary_Key=True, verbose_name = 'Code')
    description = models.CharField(max_lenght = 200, verbose_name = 'Decription')
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cityes'
        db_table = 'city'
        ordering = ['code', '-description']
    
class Corregimiento(models.model):
    code = models.AutoField(default=0, primary_Key=True, verbose_name = 'Code')
    description = models.CharField(max_lenght = 200, verbose_name = 'Description')
    city_id = models.ForeignKey(City ,verbose_name = 'City', on_delete = models.CASCADE)
    
class Zone(models.model):
    code = models.AutoField(default=0, primary_Key=True)
    description = models.CharField(max_lenght = 200)
    
# Create your models here.
