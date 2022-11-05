from asyncio.windows_events import NULL
from distutils.command.build import build
from tokenize import String
from uuid import UUID


class CityDomainBuilder:
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
        
    """def CityDomain build():
        return CityDomainBuilder.c"""