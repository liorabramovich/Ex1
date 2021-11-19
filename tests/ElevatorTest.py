import unittest
from objects import CElevator


class ElevatorTest(unittest.TestCase):
    minFloor1 = -10
    minFloor2 = 1
    minFloor3 = -3
    maxFloor1 = 90
    maxFloor2 = 73
    maxFloor3 = 12
    idNum1 = 1
    idNum2 = 2
    idNum3 = 3
    openTime1 = 1
    openTime2 = 2.3
    openTime3 = 3
    closeTime1 = 1
    closeTime2 = 2.3
    closeTime3 = 3
    speed1 = 0.5
    speed2 = 1
    speed3 = 2
    startTime1 = 3
    startTime2 = 4
    startTime3 = 5
    stopTime1 = 3
    stopTime2 = 4
    stopTime3 = 5

    elev1 = CElevator.CElevator(minFloor1, maxFloor1, idNum1, openTime1, closeTime1, speed1, startTime1, stopTime1)
    elev2 = CElevator.CElevator(minFloor2, maxFloor2, idNum2, openTime2, closeTime2, speed2, startTime2, stopTime2)
    elev3 = CElevator.CElevator(minFloor3, maxFloor3, idNum3, openTime3, closeTime3, speed3, startTime3, stopTime3)


    def testGetId(self):
        self.assertEqual(self.elev1.getId(), self.idNum1, "GetId failed")
        self.assertEqual(self.elev2.getId(), self.idNum2, "GetId failed")
        self.assertEqual(self.elev3.getId(), self.idNum3, "GetId failed")

    def testGetSpeed(self):
        self.assertEqual(self.elev1.getSpeed(), self.speed1, "GetId failed")
        self.assertEqual(self.elev2.getSpeed(), self.speed2, "GetId failed")
        self.assertEqual(self.elev3.getSpeed(), self.speed3, "GetId failed")

    def testGetMaxFloor(self):
        self.assertEqual(self.elev1.getMaxFloor(), self.maxFloor1, "GetId failed")
        self.assertEqual(self.elev2.getMaxFloor(), self.maxFloor2, "GetId failed")
        self.assertEqual(self.elev3.getMaxFloor(), self.maxFloor3, "GetId failed")

    def testGetMinFloor(self):
        self.assertEqual(self.elev1.getMinFloor(), self.minFloor1, "GetId failed")
        self.assertEqual(self.elev2.getMinFloor(), self.minFloor2, "GetId failed")
        self.assertEqual(self.elev3.getMinFloor(), self.minFloor3, "GetId failed")

    def testGetOpenTime(self):
        self.assertEqual(self.elev1.getOpenTime(), self.openTime1, "GetId failed")
        self.assertEqual(self.elev2.getOpenTime(), self.openTime2, "GetId failed")
        self.assertEqual(self.elev3.getOpenTime(), self.openTime3, "GetId failed")

    def testGetCloseTime(self):
        self.assertEqual(self.elev1.getCloseTime(), self.closeTime1, "GetId failed")
        self.assertEqual(self.elev2.getCloseTime(), self.closeTime2, "GetId failed")
        self.assertEqual(self.elev3.getCloseTime(), self.closeTime3, "GetId failed")

    def testGetStartTime(self):
        self.assertEqual(self.elev1.getStartTime(), self.startTime1, "GetId failed")
        self.assertEqual(self.elev2.getStartTime(), self.startTime2, "GetId failed")
        self.assertEqual(self.elev3.getStartTime(), self.startTime3, "GetId failed")

    def testGetStopTime(self):
        self.assertEqual(self.elev1.getStopTime(), self.stopTime1, "GetId failed")
        self.assertEqual(self.elev2.getStopTime(), self.stopTime2, "GetId failed")
        self.assertEqual(self.elev3.getStopTime(), self.stopTime3, "GetId failed")




if __name__ == '__main__':
    unittest.main()
