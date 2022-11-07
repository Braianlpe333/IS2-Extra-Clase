from uuid import UUID
from tokenize import String
import uuid
from app.ServicePerson.src.com.myproyect.solveit.domain.domain.PersonDomain import PersonDomain
from app.ServicePerson.src.com.myproyect.solveit.domain.domain.PublicationDomain import PublicationDomain
from app.ServicePerson.src.com.myproyect.solveit.domain.domain.PublicationTypeDomain import PublicationTypeDomain
from app.ServicePerson.src.com.myproyect.solveit.domain.domain.ZoneDomain import ZoneDomain
class PublicationDomainBuilder:
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

    def __init__(self, tittle, description, publisher, number, publicationType, zone, report, phoneNumber):
        self.setId(uuid.uuid1)
        self.setTittle(tittle)
        self.setDescription(description)
        self.setPublisher(publisher)
        self.setNumber(number)
        self.setPhoneNumber(phoneNumber)
        self.setPublicationType(publicationType)
        self.setZone(zone)
        self.setReport(report)
    def build(self):
        return PublicationDomain.create(self.id, self.tittle, self.description, self.publisher, self.number, self.publicationType, self.zone, self.report, self.phoneNumber)
    
