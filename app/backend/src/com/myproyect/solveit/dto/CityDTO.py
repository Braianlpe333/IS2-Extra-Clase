from asyncio.windows_events import NULL
from hashlib import new
import this
from tokenize import String
from venv import create

class CityDTO:
    id = int
    description = String

    def setId(self,id):
        self.id = id

    def getId():
        return NULL
    
    def getDescription():
        return NULL
    def setDescription(self,description):
        self.description = description
    
    def __init__(self,id,description) -> None:
        pass

    @classmethod
    def new(cls, id):
        return CityDTO
    
    def __init__(self)-> None:
        pass
    
cityDTO = CityDTO.new(1)
print(cityDTO.id)