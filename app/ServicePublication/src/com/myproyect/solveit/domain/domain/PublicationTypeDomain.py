from tokenize import String
from uuid import UUID


class PublicationTypeDomain:
    id =UUID
    description = String

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
        self.setId(id)
        self.setDescription(description)

    def create(id, description):
        return PublicationTypeDomain(id, description)
        