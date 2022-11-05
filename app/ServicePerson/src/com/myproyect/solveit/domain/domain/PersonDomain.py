from selectors import SelectorKey
import string
from tokenize import String
from uuid import UUID

from app.PersonService.src.com.myproyect.solveit.domain.domain.IdTypeDomain import IdTyopeDomain, IdTypeDomain
from app.PersonService.src.com.myproyect.solveit.domain.domain.ZoneDomain import ZoneDomain


class PersonaDomain:
    id= UUID
    name= string
    lastName= string
    idNumber= int
    idType = IdTypeDomain()
    number=int
    mail=string
    description=string
    zone= ZoneDomain()
    password = string
    #SETTERS
    def setName(self, name):
        self.name = name
    def setId(self, id):
        self.id = id
    def setLastName(self, lastName):
        self.lastName = lastName
    def setIdType(self, idType):
        self.idType = idType
    def setNumber(self, number):
        self.number = number
    def setMail(self, mail):
        self.mail = mail
    def setDescription(self, description):
        self.description = description
    def setZone(self, zone):
        self.zone = zone
    def setPassword(self, password):
        self.password = password
    
    #GETTERS
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getLastName(self):
        return self.lastName
    def getIdType(self):
        return self.idType
    def getNumbe(self):
        return self.number
    





    def __init__(self, id, name, lastName, idNumber, idType, number, mail, description, zone, password ):
        self.id= id
        self.name=name
        self.lastName=lastName
        self.idNumber=idNumber
        self.idType=idType


