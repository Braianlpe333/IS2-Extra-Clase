from tokenize import String
from uuid import UUID

from app.ServicePerson.src.com.myproyect.solveit.domain.domain.CorregimientoDomian import CorregimientoDomian
from app.ServicePerson.src.com.myproyect.solveit.domain.domain.ZoneDomain import ZoneDomain


class ZoneDomainBuilder:
    id= UUID
    description =String
    corregimiento = CorregimientoDomian()


    #GETTERS
    def getId(self):
        return self.id
    def getDescription(self):
        return self.description
    def getCorregimiento(self):
        return self.corregimiento
    
    #SETTERS
    def setId(self, id):
        self.id = id
    def setDescription(self, description):
        self.description = description
    def setCorregimiento(self, corregimiento):
        self.corregimiento = corregimiento
    
    def __init__(self, id, description, corregimiento):
        self.setId(id)
        self.setDescription(description)
        self.setCorregimiento(corregimiento)
    
    def  build(self):
        return ZoneDomain.create(self.id, self.corregimiento, self.description)