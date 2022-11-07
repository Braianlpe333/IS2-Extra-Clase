from selectors import SelectorKey
import string
from tokenize import String
from uuid import UUID

from app.ServicePublication.src.com.myproyect.solveit.domain.domain.IdTypeDomain import IdTypeDomain
from app.ServicePublication.src.com.myproyect.solveit.domain.domain.ZoneDomain import ZoneDomain


class PersonDomain:
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
    def setIdNumber(self, idNumber):
        self.idNumber = idNumber
    
    #GETTERS
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getLastName(self):
        return self.lastName
    def getIdType(self):
        return self.idType
    def getNumber(self):
        return self.number
    def  getMail(self):
        return self.mail
    def getDescription(self):
        return self.description
    def getZone(self):
        return self.zone
    def setPassword(self):
        return self.password
    





    def __init__(self, id, name, lastName, idNumber, idType, number, mail, description, zone, password ):
        self.setId(id)
        self.setName(name)
        self.setLastName(lastName)
        self.setIdNumber(idNumber)
        self.setIdType(idType)
        self.setNumber(number)
        self.setZone(zone)
        self.setMail(mail)
        self.setPassword(password)
        self.setDescription(description)

    
    def create( id, name, lastName, idNumber,  idType, number, zone, mail, password, description):
        return PersonDomain(id, name, lastName, idNumber, idType, number, zone, mail, password, description)

