from objects import CWorkplan
from objects import CWorktime


class CElevatorAlgo:
    def __init__(self, building):
        self.building = building
        self.workPlanList = []
        for i in range(self.building.numOfElev()):
            self.workPlanList.append(CWorkplan.CWorkplan(self.building.getElevator(i).getId()))

    def getBuilding(self):
        """
        :return: the instance's building
        """
        return self.building

    def calcTime(self, call, elev):
        """
              gets a request and en elevator and calculates
               how much time will it take for the elevator to do the request
        :param call: the request
        :param elev: the elevator that the request is for
        :return: a class that holds the elevator id, the time, and the workplan of the elevator
        """
        workPlan = (self.workPlanList[elev.getId()-1]).addTask(call.getSrc(), call.getDest(), call.getCallTime(), elev)
        srcIndex = workPlan.index(call.getSrc())
        destFloor = call.getDest()
        destIndex = srcIndex
        while workPlan[destIndex] != destFloor:
            destIndex += 1

        totalTime = 0

        for i in range(destIndex-1):
            distance = abs(workPlan[i] - workPlan[i+1])
            time = distance*elev.getSpeed()
            totalTime += time

        cWorkTime = CWorktime.CWorkTime()
        cWorkTime.setId(elev.getId())
        cWorkTime.setWorkPlan(workPlan)
        cWorkTime.setTime(totalTime)

        return cWorkTime

    def allocateAnElevator(self, call):
        """
            gets a request and return the elevator with the min time to do the request
        :param call:
        :return:
        """
        workTimeList = []
        if self.building.numOfElev() > 1:
            workTime = CWorktime.CWorkTime()
            for i in range(self.building.numOfElev()):
                workTimeList.append(self.calcTime(call, self.building.getElevator(i)))
            workTime = workTime.findMin(workTimeList)
            elev = self.building.getElevator(workTime.getId()-1)
            self.workPlanList[workTime.getId()-1].updateWorkPlan(workTime.getWorkPlan(), call.getCallTime(), elev)
            return workTime.getId()
        else:
            return 0
