#River City Rocketry
#Created By: Jacob Taylor Cassady
#Date Created: 10/16/2016
#Last Updated: 10/16/2016

import sys

def getInt(text):
    time = 0
    count = 0
    for i in range(0,len(text),1):
        if(text[i] == ','):
            return int(time);
        else:
            if(count == 0):
                time = int(text[i])
                count += 1
            else:
                time *= 10
                time += int(text[i])
    return time

def examineFile():
    textLocation = input("\n\nPlease input the path to the file you would like to be tested (don't forget your quotes): ")
    text = open("{0}.dat".format(textLocation))
    nextLine = text.readline()
    time = 0
    frequencyCount = 0
    thousandCount = 1
    totalCount = 0
    averageFrequency = float(0)
    
    print("")

    while nextLine != "":
        nextLine = text.readline()
        time = getInt(nextLine)
        if(time >= 1000):
            if( time <= (1000*(thousandCount+1))):
                frequencyCount += 1
            else:
                print("Frequency for range ({0}s - {1}s) = {2}".format(thousandCount,(thousandCount+1),frequencyCount))
                totalCount += frequencyCount
                frequencyCount = 1
                thousandCount += 1

    if(thousandCount == 0):
        print("Time range does not exceed 1 second.")
    else:
        averageFrequency = float(totalCount) / float((thousandCount-1))
        print("Average frequency of file given = {0:0.2F} Hz".format(averageFrequency))
        print("Average time in between readings = {0:0.3}s".format(1/averageFrequency))

while True:
    print("\n\n================= MAIN MENU =================")
    user_ans = input("Select a number: \n 1) Examine a file \n 2) Exit \n")
    if user_ans == 1:
        examineFile()
    elif user_ans == 2:
        print("goodbye")
        sys.exit()
    else:
        print("invalid input")

