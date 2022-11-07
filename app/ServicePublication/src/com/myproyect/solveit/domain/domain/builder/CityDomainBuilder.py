from asyncio.windows_events import NULL
from tokenize import String
from uuid import UUID
import uuid

from app.ServicePerson.src.com.myproyect.solveit.domain.domain.CityDomain import CityDomain


class CityDomainBuilder:
    id = UUID
    description = String
    
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id
    
    def getDescription(self):
        return  self.description
    
    def setDescription(self,description):
        self.description = description

    def __init__(self, id, description):
        self.setId(uuid.uuid1)
        self.setDescription(description)
    
    def build(self):
        return CityDomain.create(self.id, self.description)