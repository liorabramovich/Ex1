import unittest
from objects import CElevatorAlgo
from objects import CElevator
from objects import CBuilding
from objects import CElevatorCall
from objects import CWorktime


class ElevatorAlgoTest(unittest.TestCase):

    elevList1 = [{"_minFloor": -10, "_maxFloor": 10, "_id": 1, "_openTime": 1, "_closeTime": 1, "_speed": 2, "_startTime": 2, "_stopTime": 2}]

    minFloor1 = -10
    minFloor2 = -12
    minFloor3 = 3
    maxFloor1 = 10
    maxFloor2 = 87
    maxFloor3 = 24
    buidling1 = CBuilding.CBuilding(minFloor1, maxFloor1, elevList1)
    src1 = 1
    dest1 = 3
    time1 = 12.44324

    elevCall1 = CElevatorCall.CElevatorCall(src1, dest1, time1, 1)

    elevalgo1 = CElevatorAlgo.CElevatorAlgo(buidling1)

    workPlan1 = [1,3]
    time1 = 0
    idNum1 = 1

    workTime1 = CWorktime.CWorkTime()
    workTime1.setTime(time1)
    workTime1.setWorkPlan(workPlan1)
    workTime1.setId(idNum1)
    def testGetBuilding(self):
        self.assertEqual(self.elevalgo1.getBuilding(), self.buidling1, "GetBuilding Failed")

    def testAllocateAnElevator(self):
        self.assertEqual(self.elevalgo1.allocateAnElevator(self.elevCall1), 1,
                         "GetBuilding Failed")


if __name__ == '__main__':
    unittest.main()
