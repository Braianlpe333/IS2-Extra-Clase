class GeneralException:
    userMessage:str
    technicalMessage:str
    rootException:Exception

    def getUserMessage(self):
        return self.userMessage
    
    def getTechnicalMessage(self):
        return self.technicalMessage
    def getRootException(self):
        return self.rootException

    def setTechnicalMessage(self,technicalMessage):
        self.technicalMessage = technicalMessage
    
    def setUserMessage(self,userMessage):
        self.userMessage =userMessage

    def setRootException(self,rootException):
        self.rootException =rootException

    def __init__(self,userMessage,technicalMessage,rootException):
        self.setUserMessage()
        self.setTechnicalMessage()
        self.setRootException()
    

        
        