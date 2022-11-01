import string
from tokenize import String

from app.backend.src.com.myproyect.solveit.domain.domain.IdTypeDomain import IdTyopeDomain, IdTypeDomain
from app.backend.src.com.myproyect.solveit.domain.domain.ZoneDomain import ZoneDomain


class PersonaDomain:
    id=int
    name= string
    lastName= string
    idNumber= int
    idType = IdTypeDomain()
    number=int
    mail=string
    description=string
    zone= ZoneDomain()
    password = string

    def setName(self)





    def __init__(self, id, name, lastName, idNumber, idType, number, mail, description, zone, password ):
        self.id= id
        self.name=name
        self.lastName=lastName
        self.idNumber=idNumber
        self.idType=idType


