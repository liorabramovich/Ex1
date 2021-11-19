class CElevatorCall:
    def __init__(self, src, dest, callTime, elevId):
        self.src = int(src)
        self.dest = int(dest)
        self.callTime = float(callTime)
        self.elevId = int(elevId)

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getCallTime(self):
        return self.callTime
