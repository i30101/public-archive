from reader import Reader
from graph import Graph

class Stats:
    def __int__(self):
        self.roads = 321
        self.oRead = "./raw/occupancy.csv"
        self.oWrite = "./exports/occupancy.csv"
        self.occupancies = Reader.extractColumns(self.oRead)
        self.averages = {}
    

    # extracts all occupancies 
    def allOccupanies(self):
        del self.occupancies["blockface"]
        for value in self.occupancies:
            floatOccupancies = []
            for occupancy in self.occupancies[value]:
                if occupancy != "":
                    floatOccupancies.append(float(occupancy))
            self.occupancies[value] = floatOccupancies
        Reader.write(self.oWrite, [[row] + self.occupancies[row] for row in self.occupancies], False, False)


    # find averages of every category and segment
    def allAverages(self):
        for value in self.occupancies:
            self.averages[value] = sum(self.occupancies[value]) / len(self.occupancies[value])
        Reader.write(self.oWrite, [[row] + [self.averages[row]] for row in self.averages], True, True)
        Graph.bargraph("Total Averages", self.averages.keys(), "Rate and Time of Day", self.averages.values(), "Occupancy")

    
    # find averages of each category
    def categoryAverages(self):
        for i in range(2):
            letter = ["R", "S"][i]
            modes = ["Rate", "Time Segment"]
            mode = modes[i]
            xLabels = [["None", "First", "Second", "Third", "Fourth"], ["AM", "Midday", "PM", "Saturday"]][i]
            segmentAverages = {}
            for n in range(i, 5):
                segment = f"{letter}{n}"
                segmentOccupacies = []
                for value in self.averages:
                    if segment in value:
                        segmentOccupacies.append(self.averages[value])
                segmentAverages[segment] = sum(segmentOccupacies) / len(segmentOccupacies)
            Reader.write(self.oWrite, [[row] + [segmentAverages[row]] for row in segmentAverages], False, True)
            Graph.bargraph(f"{mode} Averages", xLabels, mode, list(segmentAverages.values()), "Occupancy")

        # no rates R0
        noPilotOccupancies = [100 * occupancy for occupancy in list(self.averages.values())[:4]]
        Graph.bargraph("Parking Occupancy", xLabels[1], modes[1], noPilotOccupancies, "Occupancy %")

        # available occupancy
        available = [100 - occupancy for occupancy in noPilotOccupancies]
        Graph.bargraph("Available Parking Space", xLabels[1], modes[1], available, "Availability %")
