import unittest
from objects import CWorktime

class WorkTimeTest(unittest.TestCase):
    workPlan1 = [1,3,4,5,-1]
    workPlan2 = [7,1,-9,10]
    workPlan3 = [1,10,-8]
    time1 = 10.9
    time2 = 13.12
    time3 = 7.98
    idNum1 = 1
    idNum2 = 2
    idNum3 = 3

    workTime1 = CWorktime.CWorkTime()
    workTime1.setTime(time1)
    workTime1.setWorkPlan(workPlan1)
    workTime1.setId(idNum1)

    workTime2 = CWorktime.CWorkTime()
    workTime2.setTime(time2)
    workTime2.setWorkPlan(workPlan2)
    workTime2.setId(idNum2)

    workTime3 = CWorktime.CWorkTime()
    workTime3.setTime(time3)
    workTime3.setWorkPlan(workPlan3)
    workTime3.setId(idNum3)

    workTimeList = [workTime1, workTime2, workTime3]



    def testGetWorkPlan(self):
        self.assertEqual(self.workTime1.getWorkPlan(), self.workPlan1, "GetWorkPlan failed")
        self.assertEqual(self.workTime2.getWorkPlan(), self.workPlan2, "GetWorkPlan failed")
        self.assertEqual(self.workTime3.getWorkPlan(), self.workPlan3, "GetWorkPlan failed")

    def testGetTime(self):
        self.assertEqual(self.workTime1.getTime(), self.time1, "GetTime failed")
        self.assertEqual(self.workTime2.getTime(), self.time2, "GetTime failed")
        self.assertEqual(self.workTime3.getTime(), self.time3, "GetTime failed")

    def testGetId(self):
        self.assertEqual(self.workTime1.getId(), self.idNum1, "GetId failed")
        self.assertEqual(self.workTime2.getId(), self.idNum2, "GetId failed")
        self.assertEqual(self.workTime3.getId(), self.idNum3, "GetId failed")

    def testFindMin(self):
        self.assertEqual(self.workTime1.findMin(self.workTimeList), self.workTime3, "FindMin failed")




if __name__ == '__main__':
    unittest.main()
