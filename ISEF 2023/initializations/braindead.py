import csv

def p(letter, num):
    return 

class Road:
    def __init__(self, num):
        self.firstLink = num * 2 - 1
        self.secondLink = num * 2

class BrainDead:
    def __init__(self):
        self.roads = 52

    def write(self):
        f = open("links.csv", "w", newline = "")
        writer = csv.writer(f)
        f.truncate()
        writer.writerow(["Road", "Link", "Next", "U-Turn"])
        for i in range(1, self.roads):
            road = Road(i)
            writer.writerow(["r" + str(i), "l" + str(road.firstLink), "", "l" + str(road.secondLink)])
            writer.writerow(["r" + str(i), "l" + str(road.secondLink), "", "l" + str(road.firstLink)])


dead = BrainDead()
dead.write()