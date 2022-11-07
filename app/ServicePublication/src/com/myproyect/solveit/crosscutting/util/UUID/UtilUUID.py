import uuid
from util.object.UtilObject import UtilObject
class UtilUUDI:
    DEFAUL_UUID_STRING = "00000000-0000-0000-0000-000000000000"
    DEFAUL_UUID = uuid.UUID
    def __init__(self) -> None:
        pass

    def getDefaultUUID(self,uuid):
        return UtilObject.getDefault(uuid,self.DEFAUL_UUID)

    def getDefaultUUIDOne(self,uuid,defaultUUID):
        return UtilObject.getDefault(uuid,defaultUUID)

    def isEqual(self,uuidOne,uuidTwo):
        return self.getDefaultUUID(uuidOne) == self.getDefaultUUID(uuidTwo)

    def getNewUUID(self):
        return self.DEFAUL_UUID
    
    def geStUUIDFromString(self,uuidString):
        pass

    def geStStringFromUUID(self,uuidString):
        pass