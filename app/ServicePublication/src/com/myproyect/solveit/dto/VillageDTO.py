import this
from uuid import UUID
from app.ServicePublication.src.com.myproyect.solveit.dto.CityDTO import CityDTO


class VillageDTO:
    id=UUID
    city = CityDTO

    def setId(self,id):
        self.id = id

    def getId():
        return this.id

    def setCity(self,city):
        self.city =city
    
    def getCity():
        return this.city

    def __init__(self,id,city) -> None:
        self.setId(id)
        self.setCity(city)

