from tokenize import String
from uuid import UUID

from app.ServicePerson.src.com.myproyect.solveit.domain.domain.CityDomain import CityDomain
class CorregimientoDomian:
    id = UUID
    description = String
    city = CityDomain()

    #GETTERS
    def getId(self):
        return self.id
    def getDescription(self):
        return self.description
    def getCity(self):
        return self.city
    
    #SETTERS
    def setId(self, id):
        self.id = id
    def setDescription(self, description):
        self.description = description
    def setCity(self, city):
        self.city = city
    
    def __init__(self, id, description, city):
        self.setId(id)
        self.setDescription(description)
        self.setCity(city)

    
    def create(id, description, city):
        return CorregimientoDomian(id, description, city)
