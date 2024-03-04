import csv
from reader import Reader


class Runner:
    def __init__(self):
        self.dPath = "./raw/distances.csv"
        self.walkSpeed = 0.91
        self.mPath = "./raw/manhattan.csv"
        self.roads = []
        self.plotPath = "./raw/plots.csv"


    def trim(self, s):
        r = s.replace("\\t", "").replace("/", "")
        r = r.replace("[", "").replace("]", "")
        r = r.replace("<", "").replace(">", "")
        r = r.replace("!CDATA", "").replace("Name", "")
        r = r.replace("bl", "")
        return r


    def getDistances(self):
        dRaw = Reader.extractRows(self.dPath)
        distanceSum = 0
        for distance in dRaw:
            distanceSum += float(distance[0]) * 1000
        average = distanceSum / 62
        print(average / self.walkSpeed / 60)


    def getBuildings(self):
        with open(self.mPath, "r") as file:
            reader = csv.reader(file)
            relative = -1
            count = 0
            can = False
            for row in reader:
                elements = self.trim(str(row))
                if "Figure3D" in elements and relative != 32:
                    relative = 0
                    count += 1
                    can = True
                elif relative == 3 and can:
                    elements = elements.replace("X", "").replace("'", "")
                    coords = [int(element) for element in elements.split("Y")[:2]]
                    print(f"buildings[{count}] = new Building({count}, {coords[0]}, {coords[1]}, );")
                relative += 1


    def printLinks(self):
        for i in range(1, 61, 11):
            for n in range(i, i + 5):
                top = n * 2 - 1
                bottom = n * 2
                topNext = top + 2
                bottomNext = bottom + 2
                if i % 11 == 1:
                    topNext = bottom
                elif i % 11 == 5:
                    bottomNext = top
                print(f"links[{top}] = new Link({top}, {topNext}, {bottom});")
                print(f"links[{bottom}] = new Link({bottom}, {bottomNext}, {top});")
        print()
        for i in range(6, 12):
            for n in range(i, i + 45, 11):
                left = n * 2 - 1
                right = n * 2
                leftNext = left + 22
                rightNext = right + 22
                if i == n:
                    rightNext = left
                if i == n + 44:
                    leftNext = right
                print(f"links[{left}] = new Link({left}, {leftNext}, {right});")
                print(f"links[{right}] = new Link({right}, {rightNext}, {left});")

    
    def printPLots(self):
        for lot in Reader.extractRows(self.plotPath):
            plot = int(lot[0])
            print(f"lots[{plot}] = new ParkingSpot({plot}, 3);")
        


    # def printLinks(self):
    #     id = 1
    #     for i in range(5):



achilles = Runner()
achilles.printLinks()