from app.backend.src.com.myproyect.solveit.dto.CityDTO import CityDTO


class VillageDTO:
    id=int
    city = CityDTO

    def __init__(self,id,city) -> None:
        self.id = id
        self.city = city

