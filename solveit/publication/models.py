from django.db import models

class City(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    
class Corregimiento(models.Model):
    description = models.CharField(max_length = 50, verbose_name = 'Description', null = False)
    city_id = models.ForeignKey(City ,verbose_name = 'City', on_delete = models.CASCADE, null = False)
    
class Zone(models.Model):

    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    corregimiento_id = models.ForeignKey(Corregimiento, verbose_name = 'Corregimiento', on_delete = models.CASCADE, null = False)

class Id_Type(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    
class User(models.Model):
    zone_id = models.ForeignKey(Zone, verbose_name = 'Zone', on_delete = models.CASCADE, null = False)
    idType_id = models.ForeignKey(Id_Type, verbose_name = 'Id_Type', on_delete = models.CASCADE ,null = False)
    name = models.CharField(max_length = 50, verbose_name = 'Name', null = False)
    lastname = models.CharField(max_length = 50, verbose_name = 'Lastname', null = False)
    description = models.CharField(max_length = 50, verbose_name = 'Description', null = False)
    idnumber = models.PositiveIntegerField(verbose_name = 'Id_Number', null = False)
    phone = models.PositiveIntegerField(verbose_name = 'Phone', default = 0, null = False)
    mail = models.EmailField(verbose_name = 'Mail', null = False)
    password = models.CharField(max_length = 50,verbose_name = 'Password', null = False)
    
class RequestState(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    
class MessageState(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    
class Message(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    user_id = models.ForeignKey(User, verbose_name = 'User_Id', on_delete = models.CASCADE, null = False)
    messagestate_id = models.ForeignKey(MessageState, verbose_name = 'MessageState_Id', on_delete = models.CASCADE, null = False)

class Publication_Type(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    
class Report(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    user_id = models.ForeignKey(User, verbose_name = 'User_Id', on_delete = models.CASCADE, null = False)
    
class Publication(models.Model):
    user_id = models.ForeignKey(User, verbose_name = 'User_Id', on_delete = models.CASCADE, null = False)
    report_id = models.ForeignKey(Report, verbose_name= 'Report_Id', on_delete = models.CASCADE, null = False)
    publication_type_id = models.ForeignKey(Publication_Type, verbose_name = 'Publication_Type_Id', on_delete = models.CASCADE, null = False)
    title = models.CharField(max_length = 50, verbose_name = 'Title', null = False)
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    phone = models.PositiveIntegerField(verbose_name = 'Phone', null = False)
    zone_id = models.ForeignKey(Zone, verbose_name = 'Zone', on_delete = models.CASCADE, null = False)
    
class Score(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    user_id = models.ForeignKey(User, verbose_name = 'User_Id', on_delete = models.CASCADE, null = False)
    publication_id = models.ForeignKey(Publication, verbose_name = 'Publication_Id', on_delete = models.CASCADE, null = False)
    
class Request(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    user_id = models.ForeignKey(User, verbose_name = 'User_id', on_delete = models.CASCADE, null = False)
    requeststate_id = models.ForeignKey(RequestState, verbose_name = 'RequestState_Id', on_delete = models.CASCADE, null = False)
    score_id = models.ForeignKey(Score, verbose_name = 'Score', on_delete = models.CASCADE, null = False)
    
class Notification(models.Model):
    description = models.CharField(max_length = 50, null = False, verbose_name = 'Description')
    user_id = models.ForeignKey(User, verbose_name = 'User_id', on_delete = models.CASCADE, null = False)
    message_id = models.ForeignKey(Message, verbose_name = 'Message_Id', on_delete = models.CASCADE, null = False)
    request_id = models.ForeignKey(Request, verbose_name = 'Request_Id', on_delete = models.CASCADE, null = False)
    publication_id = models.ForeignKey(Publication, verbose_name = 'Publication_Id', on_delete = models.CASCADE, null = False)
