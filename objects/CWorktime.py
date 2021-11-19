import sys


class CWorkTime:

    def __init__(self):
        self.workPlan = []
        self.time = 0.0
        self.idNum = 0

    def setWorkPlan(self, workPlan):
        self.workPlan = workPlan

    def getWorkPlan(self):
        return self.workPlan

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def getId(self):
        return self.idNum

    def setId(self, idNum):
        self.idNum = idNum

    def findMin(self, workTimeList):
        minTime = sys.float_info.max
        CWorkTimeMinList = []
        for cWorkTime in workTimeList:
            time = cWorkTime.getTime()
            minTime = min(minTime, time)
        for cWorkTime in workTimeList:
            time = cWorkTime.getTime()
            if time == minTime:
                CWorkTimeMinList.append(cWorkTime)
        minWorkMapSize = sys.float_info.max
        workTime = CWorkTime
        for cWorkTime in CWorkTimeMinList:
            size = len(cWorkTime.getWorkPlan())
            if size < minWorkMapSize:
                minWorkMapSize = size
                workTime = cWorkTime

        return workTime
