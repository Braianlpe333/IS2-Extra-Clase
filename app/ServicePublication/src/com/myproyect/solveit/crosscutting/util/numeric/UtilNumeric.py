from util.object.UtilObject import UtilObject
class UtilNumeric:
    ZERO = 0


    def __init__(self) -> None:
        pass

    def getDefault(self,value,default): return UtilObject.getDefault(value,default)

    def getDefaultZero(self,value): return UtilObject.getDefault(value,self.ZERO)

    def isGreatherThan(self,oneValue,twoValue): return self.getDefaultZero(oneValue) > self.getDefaultZero(twoValue) 
    
    def isLessThan(self,oneValue, twoValue): return self.getDefaultZero(oneValue) < self.getDefaultZero(twoValue)

    def isEqualThan(self,oneValue,twoValue): return self.getDefault(oneValue) == self.getDefault(twoValue)
	
    def isGreatherOrEqualThan(self,oneValue,twoValue): return self.getDefault(oneValue) > self.getDefault(twoValue) or self.getDefault(oneValue) == self.getDefault(twoValue)
	
    def isLessOrEqualThan(self, oneValue,twoValue): return self.getDefault(oneValue) < self.getDefault(twoValue) or self.getDefault(oneValue) == self.getDefault(twoValue)

    def isBetween(self,value,initialRange,finalRange,incluedeInitialRange:bool ,includeFinalRnage:bool): return (self.isGreatherOrEqualThan(value,initialRange),self.isGreatherThan(value,initialRange))[incluedeInitialRange] and (self.isLessOrEqualThan(value,finalRange),self.isLessThan(value,finalRange))[includeFinalRnage]
	
    def isBetweenIncludeRanges(self,value,initialRange, finalRange): return self.isBetween(value,initialRange,finalRange,True,True)

    def isPositive(self,value): return self.isGreatherOrEqualThan(value,self.ZERO)

    def isNegative(self,value): return not self.isPositive(value)