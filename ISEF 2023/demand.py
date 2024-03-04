from graph import Graph
from reader import Reader

rawPath = "data/rViolations.csv"
readPath = "data/violations.csv"
writePath = "data/fViolations.csv"
newPath = "data/2017.csv"

def filterTimes(path):
    Reader.write(readPath, [[t] for t in Reader.getColumn(path, "ISSUE_TIME")])

violationTimes = [v[0] for v in Reader.extractRows(readPath)]
timeList = []

def floatTime(data):
    times = data.split(" ")
    time = times[0].split(":")
    print(times)
    ampm = times[1]
    # print(times, time)
    hour = int(time[0])
    minute = int(time[1]) / 60
    total = hour + minute
    if (ampm == "AM" and hour == 12) or (ampm == "PM" and hour != 12):
        total += 12
    return total

for violationTime in violationTimes:
    timeList.append(floatTime(violationTime))

Reader.write(writePath, [[t] for t in timeList])