import csv

class LinkWriter:
    def __init__(self):
        self.linkPath = "./csv/links.csv"
        self.lotsPath = "./scv/noLots.csv"
        self.angryPath = "./scv/andrewAngry.csv"
        self.linkIndex = 0
        self.nextIndex = 1
        self.uIndex = 2
        self.linkIDs = list(range(1, 105))

    def printLinkInitializations(self):
        with open(self.linkPath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                link = row[self.linkIndex]
                next = row[self.nextIndex]
                u = row[self.uIndex]
                print(f"links[{link}] = new Link({next}, {u});")

    def printNoSpaces(self):
        with open(self.lotsPath, "r") as file:
            reader = csv.reader(file)
            haveSpaces = []
            for row in reader:
                haveSpaces.append(int("".join(row)))
            for link in self.linkIDs:
                if link not in haveSpaces:
                    print(f"links[{link}].setNoSpace();")

    def printParkingSpots(self):
        with open(self.angryPath, "r") as file:
            reader = csv.reader(file)
            global relative
            relative = 0
            count = 0
            global plotID
            plotID = 0
            for row in reader:
                eString = str(row).replace("\\t", "").replace("'", "")
                eString = eString.replace("[", "").replace("]", "")
                eString = eString.replace("<", "").replace(">", "")
                eString = eString.replace("!CDATA", "").replace("/", "")
                if "plot" in eString:
                    relative = 0
                    eString = eString.replace("plot", "").replace("Name", "")
                    plotID = int(eString)
                    count += 1
                elif "ParkingSpaceCount" in eString:
                    eString = eString.replace("ParkingSpaceCount", "")
                    print(f"lots[{plotID}] = new ParkingSpot({int(eString)});")
                if count == 80:
                    break
                relative += 1


    def writeBuildings(self):
        # 84 buildings
        global output
        output = [[""]]
        global count
        count = 0
        global relative
        relative = 0
        global buildingID
        buildingID = -1
        global x
        x = -1
        global y 
        y = -1
        can = False
        with open(self.angryPath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                eString = str(row).replace("\\t", "").replace("'", "")
                eString = eString.replace("[", "").replace("]", "")
                eString = eString.replace("<", "").replace(">", "")
                eString = eString.replace("!CDATA", "")
                if "Figure3D" in eString and "/Figure3D" not in eString:
                    # print(left)
                    # print(eString)
                    relative = 0
                    can = True
                # elif relative == 2:
                #     # print(eString)
                #     eString = eString.replace("Name", "").replace("/", "").replace("b", "")
                #     print(eString)
                #     # buildingID = int(eString)
                elif relative == 3 and can:
                    eString = eString.replace("Y", "X").replace("/", "")
                    eList = eString.split("X")
                    # print(eList)
                    count += 1
                    x = int(eList[1])
                    y = int(eList[3])
                    print(f"buildings[{count}] = new Building({x}, {y}, z);")
                elif count == 85:
                    break
                relative += 1

    def printCase(self, number, prefix):
        for id in range(1, number + 1):
            print(f"case {id}: return {prefix}{id};")

    def printPlotNumber(self):
        with open(self.lotsPath, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                id = str(row).replace("[", "").replace("]", "").replace("'", "")
                print(f"case {id}: return plot{id};")

            

writer = LinkWriter()
writer.printLinkInitializations()