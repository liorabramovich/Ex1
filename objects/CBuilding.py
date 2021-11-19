from objects import CElevator


class CBuilding:
    def __init__(self, minFloor, maxFloor, ElevList):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevList = []
        for line in ElevList:
            self.elevList.append(
                CElevator.CElevator(line["_minFloor"], line["_maxFloor"], line["_id"], line["_openTime"],
                                    line["_closeTime"], line["_speed"],
                                    line["_startTime"], line["_stopTime"]))

    def getMinFloor(self):
        return self.minFloor

    def getMaxFloor(self):
        return self.maxFloor

    def getElevator(self, index):
        return self.elevList[index]

    def numOfElev(self):
        return len(self.elevList)
