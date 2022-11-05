from tokenize import String
from uuid import UUID
import uuid

from app.ServicePerson.src.com.myproyect.solveit.domain.domain.IdTypeDomain import IdTypeDomain

class IdTypeDomainBuilder:
    id = UUID
    description= String

    #GETTERS
    def getId(self):
        return self.id
    def getDescription(self):
        return self.description
    
    #SETTERS
    def setId(self, id):
        self.id = id
    def setDescription(self, description):
        self.description = description
    
    def __init__(self, id, description):
        self.setId(uuid.uuid1)
        self.setDescription(description)
    
    def build(self):
        return IdTypeDomain.create(self.id, self.description)