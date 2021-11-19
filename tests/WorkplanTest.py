import unittest
from objects import CWorkplan
from objects import CElevator


class MyTestCase(unittest.TestCase):
    idNum1 = 1
    idNum2 = 2
    idNum3 = 3
    workPlan1 = []
    workPlanEta = []

    cworkPlan1 = CWorkplan.CWorkplan(idNum1)

    minFloor1 = -10
    maxFloor1 = 90
    idNum1 = 1
    openTime1 = 1
    closeTime1 = 1
    speed1 = 0.5
    startTime1 = 3
    stopTime1 = 3

    elev1 = CElevator.CElevator(minFloor1, maxFloor1, idNum1, openTime1, closeTime1, speed1, startTime1, stopTime1)

    def testAddTask(self):
        self.assertEqual(self.cworkPlan1.addTask(1,3,10,self.elev1), [1,3], "AddTask Failed")
        self.assertEqual(self.cworkPlan1.addTask(4, 10, 30, self.elev1), [1, 3, 4, 10], "AddTask Failed")
        self.assertEqual(self.cworkPlan1.addTask(4, -3, 31, self.elev1), [1, 3, 4, 10, -3], "AddTask Failed")

    def testCalcCurrentFloor(self):
        self.assertEqual(self.cworkPlan1.calcCurrentFloor(1, 30, 1, 32), 3, "CalcCurrentEta Failed")
        self.assertEqual(self.cworkPlan1.calcCurrentFloor(-3, 12, 2, 20), 13, "CalcCurrentEta Failed")
        self.assertEqual(self.cworkPlan1.calcCurrentFloor(0, 0, 0.5, 4), 2, "CalcCurrentEta Failed")

    def testCalcCurrentEta(self):
        self.assertEqual(self.cworkPlan1.calcCurrentEta(1, 5, 30, 1), 34, "CalcCurrentEta Failed")
        self.assertEqual(self.cworkPlan1.calcCurrentEta(1, -3, 10, 2), 12, "CalcCurrentEta Failed")
        self.assertEqual(self.cworkPlan1.calcCurrentEta(1, 10, 16, 0.5), 34, "CalcCurrentEta Failed")

    def testFindCurrentEta(self):
        self.cworkPlan1.updateWorkPlan([1, 3, 4, 10, -3], 30, self.elev1)
        self.assertEqual(self.cworkPlan1.findCurrentEta(40, self.elev1, 3), [44, 96, 146, 206, 280], "FindCurrentETA Failed")

    def testFindCurrentPos(self):
        self.cworkPlan1.updateWorkPlan([1, 3, 4, 10, -3], 30, self.elev1)
        self.assertEqual(self.cworkPlan1.findCurrentPos(40, self.elev1), 5,  "FindCurrentPos Failed")

    def testGetWorkPlan(self):
        self.cworkPlan1.updateWorkPlan([1, 3, 4, 10, -3], 30, self.elev1)
        self.assertEqual(self.cworkPlan1.getWorkplan(), [1, 3, 4, 10, -3], "GetWorkPlan Failed")


if __name__ == '__main__':
    unittest.main()
