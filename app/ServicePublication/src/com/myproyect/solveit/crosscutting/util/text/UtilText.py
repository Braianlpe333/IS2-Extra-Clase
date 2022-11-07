from util.object.UtilObject import UtilObject
class UtilText:
    EMPTY=""
    SPACE=" "
    
    def __init__(self) -> None:
        pass
    def isNull(self,value): return UtilObject.isNull(self,value)

    def getDefault(self,value,defaultValue): return UtilObject.getDefault(value,defaultValue)

    def getDefaultEmpty(self,value): return self.getDefault(value,self.EMPTY)

    def trim(self,value): return self.getDefaultEmpty(value).strip()

    def isEmpty(self,value): return self.EMPTY == value.strip()