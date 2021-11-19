import unittest
from objects import CBuilding
from objects import CElevator

class BuidlingTest(unittest.TestCase):
    elevList1 = [CElevator.CElevator(-10, 10, 1, 1, 1, 2, 3, 3), CElevator.CElevator(-5, 10, 2, 1.5, 1.5, 2, 3, 3), CElevator.CElevator(-10, 9, 3, 1, 1, 2, 3, 3), CElevator.CElevator(-9, 3, 4, 4, 4, 2, 3, 3)]
    elevList2 = [CElevator.CElevator(-11, 9, 1, 0.5, 0.5, 3, 4, 4), CElevator.CElevator(-12, 80, 2, 2.5, 2.5, 2, 4, 4), CElevator.CElevator(-10, 9, 3, 1, 1, 2, 3, 3), CElevator.CElevator(-9, 3, 4, 4, 4, 2, 3, 3)]
    elevList3 = [CElevator.CElevator(-10, 10, 1, 1, 1, 2, 3, 3), CElevator.CElevator(-5, 10, 2, 1, 1, 2, 2, 2), CElevator.CElevator(-10, 12, 3, 1, 1, 2, 3, 3), CElevator.CElevator(-9, 24, 4, 4, 4, 2, 3, 3)]

    minFloor1 = -10
    minFloor2 = -12
    minFloor3 = 3
    maxFloor1 = 10
    maxFloor2 = 87
    maxFloor3 = 24
    buidling1 = CBuilding.CBuilding(minFloor1, maxFloor1, elevList1)
    buidling2 = CBuilding.CBuilding(minFloor2, maxFloor2, elevList2)
    buidling3 = CBuilding.CBuilding(minFloor3, maxFloor3, elevList3)


    def testGetMinFloor(self):
        self.assertEqual(self.buidling1.getMinFloor(), self.minFloor1, "Failed")
        self.assertEqual(self.buidling2.getMinFloor(), self.minFloor2, "Failed")
        self.assertEqual(self.buidling3.getMinFloor(), self.minFloor3, "Failed")

    def testGetMaxFloor(self):
        self.assertEqual(self.buidling1.getMaxFloor(), self.maxFloor1, "Failed")
        self.assertEqual(self.buidling2.getMaxFloor(), self.maxFloor2, "Failed")
        self.assertEqual(self.buidling3.getMaxFloor(), self.maxFloor3, "Failed")

    def testGetElevator(self):
        self.assertEqual(self.buidling1.getElevator(1), self.elevList1[1], "Failed")
        self.assertEqual(self.buidling2.getElevator(3), self.elevList2[3], "Failed")
        self.assertEqual(self.buidling3.getElevator(2), self.elevList3[2], "Failed")

    def testNumOfElev(self):
        self.assertEqual(self.buidling1.numOfElev(), self.elevList1, "Failed")
        self.assertEqual(self.buidling2.numOfElev(), self.elevList2, "Failed")
        self.assertEqual(self.buidling3.numOfElev(), self.elevList3, "Failed")



if __name__ == '__main__':
    unittest.main()
