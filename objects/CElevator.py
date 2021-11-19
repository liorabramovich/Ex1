class CElevator:
    def __init__(self, minFloor, maxFloor, idNum, openTime, closeTime, speed, startTime, stopTime):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.idNum = idNum
        self.openTime = openTime
        self.closeTime = closeTime
        self.speed = speed
        self.startTime = startTime
        self.stopTime = stopTime

    def getId(self):
        return self.idNum

    def getSpeed(self):
        return self.speed

    def getMaxFloor(self):
        return self.maxFloor

    def getMinFloor(self):
        return self.minFloor

    def getOpenTime(self):
        return self.openTime

    def getCloseTime(self):
        return self.closeTime

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return self.stopTime
