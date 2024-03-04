import csv
import gmplot

class Reader:
    def __init__(self):
        self.maxLat = 38.899875
        self.maxLon = -77.019818
        self.minLat = 38.896077
        self.minLon = -77.029622
        self.lats = []
        self.lons = []
        self.validRestaurants = []
        self.andrewLats = []
        self.andrewLons = []
        self.josephLats = []
        self.josephLons = []

    def filter(self):
        with open("restaurants.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            lat = header.index("Latitude")
            lon = header.index("Longitude")
            count = 0
            for row in reader:
                rLat = float(row[lat])
                rLon = float(row[lon])
                if (rLat > self.minLat and rLat < self.maxLat) and (rLon > self.minLon and rLon < self.maxLon):
                    self.validRestaurants.append([rLat, rLon])
                    self.lats.append(rLat)
                    self.lons.append(rLon)
                    if count < 70:
                        self.andrewLats.append(rLat)
                        self.andrewLons.append(rLon)
                    else:
                        self.josephLats.append(rLat)
                        self.josephLons.append(rLon)
                    count += 1


    def write(self):
        f = open("filtered.csv", "w", newline = "")
        writer = csv.writer(f)
        f.truncate()
        writer.writerow(["Latitude", "Longitude"])
        for restaurant in self.validRestaurants:
            writer.writerow(restaurant)

    def generateMap(self):
        gmap = gmplot.GoogleMapPlotter(38.89858,-77.022829, 13)
        gmap.scatter(self.lats, self.lons, '#FF0000', size = 5, marker = False)
        gmap.draw("C:\\Users\\andre\\Documents\\Programming\\PQCT\\map.html")

    def taskMap(self):
        andrew = gmplot.GoogleMapPlotter(38.89858,-77.022829, 13)
        andrew.scatter(self.andrewLats, self.andrewLons, "#FF0000", size = 5, marker = False)
        andrew.draw("C:\\Users\\andre\\Documents\\Programming\\PQCT\\andrew.html")
        joseph = gmplot.GoogleMapPlotter(38.89858,-77.022829, 13)
        joseph.scatter(self.josephLats, self.josephLons, "#FF0000", size = 5, marker = False)
        joseph.draw("C:\\Users\\andre\\Documents\\Programming\\PQCT\\joseph.html")


reader = Reader()
reader.filter()
reader.write()
reader.generateMap()
reader.taskMap()