from asyncio.windows_events import NULL
from tokenize import String
from uuid import UUID

class CityDTO:
    id = UUID
    description = String

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id
    
    def getDescription(self):
        return self.description

    def setDescription(self,description):
        self.description = description
    
    def build(self,id,description):
        self.setId(id)
        self.setDescription(description)

    
    def __init__(self)-> None:
        self.setId(0)
        self.setDescription("")

