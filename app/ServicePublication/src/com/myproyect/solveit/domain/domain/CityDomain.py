from asyncio.windows_events import NULL
from tokenize import String
from uuid import UUID


class CityDomain:
    id = UUID
    description = String
    
    def setId(self,id):
        self.id = id

    def getId():
        return NULL
    
    def getDescription():
        return NULL
    
    def setDescription(self,description):
        self.description = description
        
    def CityDomainCreate(self, id, description):
        print("hola")
        return CityDomain(id, description)