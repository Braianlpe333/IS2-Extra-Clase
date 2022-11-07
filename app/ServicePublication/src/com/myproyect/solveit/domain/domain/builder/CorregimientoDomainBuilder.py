from tokenize import String
from uuid import UUID
import uuid
from app.ServicePerson.src.com.myproyect.solveit.domain.domain.CityDomain import CityDomain
from app.ServicePerson.src.com.myproyect.solveit.domain.domain.CorregimientoDomian import CorregimientoDomian


class CorregimientoDomianBuilder:
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
        self.setId(uuid.uuid1)
        self.setDescription(description)
        self.setCity(city)
    def build(self):
        return CorregimientoDomian.create(self.id, self.description, self.city)