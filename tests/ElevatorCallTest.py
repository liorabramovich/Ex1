import unittest
from objects import CElevatorCall


class ElevatorCallTest(unittest.TestCase):
    src1 = 1
    src2 = 1
    src3 = -1
    dest1 = 3
    dest2 = -4
    dest3 = 10
    time1 = 12.44324
    time2 = 34.435
    time3 = 56.12353245

    elevCall1 = CElevatorCall.CElevatorCall(src1, dest1, time1, 1)
    elevCall2 = CElevatorCall.CElevatorCall(src2, dest2, time2, 3)
    elevCall3 = CElevatorCall.CElevatorCall(src3, dest3, time3, 2)


    def testGetSrc(self):
        self.assertEqual(self.elevCall1.getSrc(), self.src1, "GetSrc failed")
        self.assertEqual(self.elevCall2.getSrc(), self.src2, "GetSrc failed")
        self.assertEqual(self.elevCall3.getSrc(), self.src3, "GetSrc failed")

    def testGetDest(self):
        self.assertEqual(self.elevCall1.getDest(), self.dest1, "GetDest failed")
        self.assertEqual(self.elevCall2.getDest(), self.dest2, "GetDest failed")
        self.assertEqual(self.elevCall3.getDest(), self.dest3, "GetDest failed")

    def testGetCallTime(self):
        self.assertEqual(self.elevCall1.getCallTime(), self.time1, "GetCallTime failed")
        self.assertEqual(self.elevCall2.getCallTime(), self.time2, "GetCallTime failed")
        self.assertEqual(self.elevCall3.getCallTime(), self.time3, "GetCallTime failed")


if __name__ == '__main__':
    unittest.main()
