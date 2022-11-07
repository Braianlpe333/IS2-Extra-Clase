from django.db import models

class City(models.Model):
    description = models.CharField(max_length = 50, null = False)
    
class Corregimiento(models.Model):
    description = models.CharField(max_length = 50, verbose_name = 'Description', null = False)
    city_id = models.ForeignKey(City ,verbose_name = 'City', on_delete = models.CASCADE, null = False)
    
class Zone(models.Model):
    description = models.CharField(max_length = 50, null = False)
    corregimiento_id = models.ForeignKey(Corregimiento, verbose_name = 'Corregimiento', null = False,on_delete = models.CASCADE)

class Id_Type(models.Model):
    description = models.CharField(max_length = 50, null = False)
    
class User(models.Model):
    zone_id = models.ForeignKey(Zone, verbose_name = 'Zone', null = False,on_delete = models.CASCADE)
    idType_id = models.ForeignKey(Id_Type, verbose_name = 'Id_Type', null = False,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50, verbose_name = 'Name', null = False)
    lastname = models.CharField(max_length = 50, verbose_name = 'Lastname', null = False)
    description = models.CharField(max_length = 50, verbose_name = 'Description', null = False)
    idnumber = models.PositiveIntegerField(verbose_name = 'Id_Number', null = False)
    phone = models.PositiveIntegerField(verbose_name = 'Phone', default = 0)
    mail = models.EmailField(verbose_name = 'Mail', null = False)
    password = models.CharField(verbose_name = 'Password', null = False,max_length = 50)