import json
import csv
from objects import CBuilding
from objects import CElevatorAlgo
from objects import CElevatorCall
import sys


def outputCalls(newCalls,building,callName):

    callsFile = open("outputCalls-"+building+"-"+callName+ ".csv", "w", newline='')
    callsWriter = csv.writer(callsFile)
    for line in newCalls:
        callsWriter.writerow(line)


def loadBuilding(building):
    cbuilding = CBuilding.CBuilding(building["_minFloor"], building["_maxFloor"], building["_elevators"])
    return cbuilding


def loadCalls(callsReader):
    callsList = []
    for line in callsReader:
        callsList.append(CElevatorCall.CElevatorCall(line[2], line[3], line[1], line[5]))
    return callsList


def main():
    cBuilding = 0
    callsList = []
    buildingFileName = ""
    callsFileName = ""

    if len(sys.argv) < 3:
        while True:
            try:
                buildingFileName = input('please enter the path for the Building json file: ')
                buildingFile = open(buildingFileName)
                building = json.load(buildingFile)
                cBuilding = loadBuilding(building)
                break
            except:
                print("Error! Please Try again.")

        while True:
            try:
                callsFileName = input("please enter the path for the calls csv file: ")
                callsFile = open(callsFileName)
                callsReader = csv.reader(callsFile)
                callsList = loadCalls(callsReader)
                break
            except:
                print("Error! Please try again.")
    else:
        try:
            buildingFileName = sys.argv[1]
            buildingFile =open(buildingFileName)
            building = json.load(buildingFile)
            cBuilding = loadBuilding(building)
        except:
            print("Error! Please Try again.")

        try:
            callsFileName = sys.argv[2]
            callsFile = open(callsFileName)
            callsReader = csv.reader(callsFile)
            callsList = loadCalls(callsReader)
        except:
            print("Error! Please try again.")

    print("Started...\n")
    elevAlgo = CElevatorAlgo.CElevatorAlgo(cBuilding)
    newCallList = []
    for call in callsList:
        newCall = ['Elevator call', str(call.getCallTime()), str(call.getSrc()), str(call.getDest()), '0']
        elevId = elevAlgo.allocateAnElevator(call)
        newCall.append(str(elevId))
        newCallList.append(newCall)

    buildingFileName = buildingFileName.split("/")[-1].split('.')[0]
    callsFileName = callsFileName.split("/")[-1].split('.')[0]
    outputCalls(newCallList,buildingFileName,callsFileName)
    print("Completed: Output file path = outputCalls.csv")



if __name__ == '__main__':
    main()
    # for b in range(1,5):
    #     for c in "abcd":
    #         main(f"data/B{b}.json",f"data/Calls_{c}.csv")



