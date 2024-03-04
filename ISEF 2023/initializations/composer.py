import csv

class Composer:
    def __init__(self):
        self.idList = list(range(1, 105))
        self.buildingList = list(range(1, 63))
        self.alpPath = "./new/PQCT.csv"

    def midgetize(self, s, characters):
        output = s
        for character in characters:
            output = output.replace(character, "")
        return output
    
    def linkInit(self):
        rows = []
        with open("./new/linkInit.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                link = row[0]
                next = row[1]
                u = row[2]
                rows.append(f"links[{link}] = new Link({link}, {next}, {u});")
        with open("./new/linkInit.txt", "w") as file:
            file.truncate()
            file.write("\n".join(rows))

    def buildingInit(self):
        global pre
        pre = []
        global buildings
        buildings = []
        with open("./new/closestLinks.csv", "r") as c:
            reader = csv.reader(c)
            for row in reader:
                pre.append([int(row[0]), "x", "y", int(row[1])])
        with open(self.alpPath, "r") as a:
            reader = csv.reader(a)
            relative = -1
            count = 0
            can = False
            for row in reader:
                elements = self.midgetize(str(row), ["\\t", "'", "[", "]", "<", ">", "!CDATA", "/", "Name", "bld"])
                if "Figure3D" in elements and relative != 32:
                    relative = 0
                    count += 1
                    can = True
                elif relative == 2 and can and "*" not in elements:
                    try:
                        count != int(elements)
                    except:
                        print("unhappy")
                elif relative == 3 and can and "*" not in elements:
                    elements = self.midgetize(elements, "X")
                    coords = elements.split("Y")
                    buildings.append(f"buildings[{count}] = new Building({count}, {int(coords[0])}, {int(coords[1])}, {pre[count - 1][3]});")
                elif count == 63:
                    break
                relative += 1
        with open("./new/buildingInit.txt", "w") as file:
            file.truncate()
            file.write("\n".join(buildings))





chopin = Composer()
chopin.buildingInit()