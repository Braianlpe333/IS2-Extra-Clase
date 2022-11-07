class UtilObject:

    INSTANCE= object.__init__

    def __init__(self):
        pass

    def getUtilObject(self):
        return self.INSTANCE
    
    def isNull(self, obj:object):
        return obj == None

    def getDefault(obj:object,defaultValue:object):
        return (defaultValue,obj)[UtilObject.isNull(obj)]

