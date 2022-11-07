from uuid import UUID
from tokenize import String

from app.ServicePublication.src.com.myproyect.solveit.domain.domain.PersonDomain import PersonDomain
from app.ServicePublication.src.com.myproyect.solveit.domain.domain.PublicationTypeDomain import PublicationTypeDomain
from app.ServicePublication.src.com.myproyect.solveit.domain.domain.ZoneDomain import ZoneDomain
class PublicationDomain:
    id = UUID
    tittle = String
    description =String
    publisher = PersonDomain()
    number = int
    phoneNumber=int
    publicationType = PublicationTypeDomain()
    zone = ZoneDomain()
    report =[String]

    #SETTERS
    def setId(self, id):
        self.id= id
    def setTittle(self, tittle):
        self.tittle = tittle
    def setDescription(self, description):
        self.description = description
    def setPublisher(self, publisher):
        self.publisher= publisher
    def setNumber(self, number):
        self.number = number
    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    def setPublicationType(self, publicationType):
        self.publicationType = publicationType
    def setZone(self, zone):
        self.zone = zone
    def setReport(self, report):
        self.report = report
    #GETTERS
    def getId(self):
        return self.idget
    def getTittle(self):
        return self.tittle
    def getDescription(self):
        return self.description
    def getPublisher(self):
        return self.publisher
    def getNumber(self):
        return self.number
    def getPhoneNumber(self):
        return self.number
    def getPublicationType(self):
        return self.publicationType
    def getZone(self):
        return self.zone
    def getReport(self):
        return self.report

    def __init__(self, id, tittle, description, publisher, number, publicationType, zone, report, phoneNumber):
        self.setId(id)
        self.setTittle(tittle)
        self.setDescription(description)
        self.setPublisher(publisher)
        self.setNumber(number)
        self.setPhoneNumber(phoneNumber)
        self.setPublicationType(publicationType)
        self.setZone(zone)
        self.setReport(report)
    

    def create(id, tittle, description, publisher, number, publicationType, zone, report, phoneNumber):
        return PublicationDomain(id, tittle, description, publisher, number, publicationType, zone, report, phoneNumber)
    