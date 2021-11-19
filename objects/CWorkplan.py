import numpy


class CWorkplan:
    def __init__(self, idNum):
        self.idNum = idNum
        self.workPlan = []
        self.workPlanEta = []
        self.lastPos = 0
        self.lastPosEta = 0

    def addTask(self, src, dest, currentTime, elev):
        """
            gets a request and a position
             of a elevator and decides where to put the new request in the current work plan

        :param src: the calls source
        :param dest: the calls destanation
        :param currentTime: the time of the call
        :param elev: the current elevator
        :return: the updated work plan
        """
        newWorkPlan = self.workPlan

        pos = self.findCurrentPos(currentTime, elev)
        index = 0
        for i in range(len(self.workPlanEta) - 1):
            if self.workPlanEta[i] < currentTime and self.workPlanEta[i + 1] <= currentTime:
                index = i
        newWorkPlan = newWorkPlan[index:]

        if len(newWorkPlan) <= 1:
            newWorkPlan.append(src)
            newWorkPlan.append(dest)

            newWorkPlanNoDup = [newWorkPlan[0]]
            for i in range(1, len(newWorkPlan) - 1):
                if newWorkPlan[i] == newWorkPlan[i + 1] or newWorkPlan[i] != newWorkPlan[i - 1]:
                    newWorkPlanNoDup.append(newWorkPlan[i])
            newWorkPlanNoDup.append(newWorkPlan[-1])
            newWorkPlan = newWorkPlanNoDup

            return newWorkPlan

        newWorkPlan.insert(1, pos)
        nextfloor = newWorkPlan[2]
        currentDir = numpy.sign(nextfloor - pos)
        goingUp = 0 < currentDir

        if currentDir == 0:
            self.workPlan.pop(1)
            self.workPlanEta.pop(1)
            return self.addTask(src, dest, currentTime, elev)

        upPlan1 = []
        upPlan2 = []
        downPlan1 = []
        downPlan2 = []
        i = 0

        if goingUp:
            while True:
                upPlan1.append(newWorkPlan[i])
                i += 1
                if not(i < len(newWorkPlan) and newWorkPlan[i-1] < newWorkPlan[i]):
                    break
            if i < len(newWorkPlan):
                while True:
                    downPlan1.append(newWorkPlan[i])
                    i += 1
                    if not(i < len(newWorkPlan) and newWorkPlan[i] < newWorkPlan[i-1]):
                        break
            if i < len(newWorkPlan):
                while True:
                    upPlan2.append(newWorkPlan[i])
                    i += 1
                    if not(i < len(newWorkPlan) and newWorkPlan[i-1] < newWorkPlan[i]):
                        break
            if i < len(newWorkPlan):
                while True:
                    downPlan2.append(newWorkPlan[i])
                    i += 1
                    if not(i < len(newWorkPlan) and newWorkPlan[i] < newWorkPlan[i-1]):
                        break
        else:
            while True:
                downPlan1.append(newWorkPlan[i])
                i += 1
                if not(i < len(newWorkPlan) and newWorkPlan[i] < newWorkPlan[i-1]):
                    break
            if i < len(newWorkPlan):
                while True:
                    upPlan1.append(newWorkPlan[i])
                    i += 1
                    if not(i < len(newWorkPlan) and newWorkPlan[i-1] < newWorkPlan[i]):
                        break
            if i < len(newWorkPlan):
                while True:
                    downPlan2.append(newWorkPlan[i])
                    i += 1
                    if not(i < len(newWorkPlan) and newWorkPlan[i] < newWorkPlan[i-1]):
                        break
            if i < len(newWorkPlan):
                while True:
                    upPlan2.append(newWorkPlan[i])
                    i += 1
                    if not(i < len(newWorkPlan) and newWorkPlan[i-1] < newWorkPlan[i]):
                        break

        if dest < src:  #Down
            if goingUp or src < pos:
                downplan = downPlan1
            else:
                downplan = downPlan1

            downplan.append(src)
            downplan.append(dest)
            downplan.sort(reverse=True)
        elif src < dest:  #Up
            if not goingUp or pos < src:
                upPlan = upPlan1
            else:
                upPlan = upPlan2

            upPlan.append(src)
            upPlan.append(dest)
            upPlan.sort(reverse=False)

        newWorkPlan.clear()
        if goingUp:
            newWorkPlan += upPlan1
            newWorkPlan += downPlan1
            newWorkPlan += upPlan2
            newWorkPlan += downPlan2
        else:
            newWorkPlan += downPlan1
            newWorkPlan += upPlan1
            newWorkPlan += downPlan2
            newWorkPlan += upPlan2

        newWorkPlanNoDup = [newWorkPlan[0]]
        for i in range(1, len(newWorkPlan)-1):
            if newWorkPlan[i] == newWorkPlan[i+1] or newWorkPlan[i] != newWorkPlan[i-1]:
                newWorkPlanNoDup.append(newWorkPlan[i])
        newWorkPlanNoDup.append(newWorkPlan[-1])
        newWorkPlan = newWorkPlanNoDup

        return newWorkPlan

    def calcCurrentFloor(self, lastFloor, lastEta, speed, currentTime):
        """

        :param lastFloor: the last floor of the elevator
        :param lastEta: the last eta of the last floor
        :param speed: the speed of the elevator
        :param currentTime: the current time
        :return: the elevator's position
        """
        currentFloor = lastFloor + (currentTime - lastEta) * speed
        return currentFloor

    def calcCurrentEta(self, lastFloor, nextFloor, currentTime, speed):
        """

        :param lastFloor: the last floor that the elevator were in
        :param nextFloor: the next floor that the elevator needs to go to
        :param currentTime: the current time
        :param speed: the elevator's speed
        :return: the eta of the next floor
        """
        currentEta = (abs(nextFloor - lastFloor) + speed * currentTime) / speed
        return currentEta

    def findCurrentEta(self, currentTime, elev, pos):
        """

        :param currentTime: the current time
        :param elev: the current elevator
        :param pos: the current position of the elevator
        :return: an updated array of all the ETAs
        """
        newWorkPlanEta = []
        totalTime = 0
        for i in range(len(self.workPlan)):
            if i == 0:
                totalTime = self.calcCurrentEta(pos, self.workPlan[i], currentTime, elev.getSpeed())
            else:
                totalTime += abs(self.workPlan[i] - self.workPlan[i-1]) / elev.getSpeed()
                #totalTime += self.calcCurrentEta(self.workPlan[i-1], self.workPlan[i], currentTime, elev.getSpeed())
                totalTime += elev.getOpenTime() + elev.getCloseTime() + elev.getStartTime() + elev.getStopTime()
            newWorkPlanEta.append(totalTime)
        return newWorkPlanEta

    def findCurrentPos(self, currentTime, elev):
        """

        :param currentTime: current time
        :param elev: current elevator
        :return: the elevator's current position
        """
        currentPos = 0
        for i in range(1, len(self.workPlanEta)):
            if self.workPlanEta[0] > currentTime:
                speed = numpy.sign(self.workPlan[1] - self.workPlan[0]) * elev.getSpeed()
                currentPos = self.calcCurrentFloor(self.lastPos, self.lastPosEta, speed, currentTime)
                self.lastPosEta = self.calcCurrentEta(self.lastPos, currentPos, currentTime, elev.getSpeed())
                break
            if self.workPlanEta[i] > currentTime:
                speed = numpy.sign(self.workPlan[i] - self.workPlan[i-1]) * elev.getSpeed()
                currentPos = self.calcCurrentFloor(self.workPlan[i-1], self.workPlanEta[i-1], speed, currentTime)
                break
            if int(self.workPlanEta[i]) == int(currentTime):
                currentPos = self.workPlan[i]
                break
            else:
                currentPos = self.workPlan[-1]

            if currentPos != 0:
                self.lastPos = int(currentPos)
        return int(currentPos)

    def updateWorkPlan(self, newWorkplan, currentTime, elev):
        """

        :param newWorkplan: an updated workplan array
        :param currentTime: the current time
        :param elev: the current elevator
        """
        pos = self.findCurrentPos(currentTime, elev)
        self.workPlan = newWorkplan
        self.workPlanEta = self.findCurrentEta(currentTime, elev, pos)

    def getWorkplan(self):
        return self.workPlan

    def setWorkplan(self, newWorkPlan):
        self.workPlan = newWorkPlan
