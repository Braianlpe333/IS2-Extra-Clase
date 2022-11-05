import string
from uuid import UUID

from app.ServicePerson.src.com.myproyect.solveit.domain.domain.CorregimientoDomian import CorregimientoDomian


class ZoneDomain:

    id = UUID
    description = string
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
    def setCorregimiento(self, corregimiento):
        self.corregimiento = corregimiento
    def setDescription(self, description):
        self.description = description
    
    def __init__(self, id, corregimiento, description):
        self.setId(id)
        self.setDescription(description)
        self.setCorregimiento(corregimiento)
    
    def create(id, corregimeinto, description):
        return CorregimientoDomian(id, corregimeinto, description)