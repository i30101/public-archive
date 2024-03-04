import random

class Scenario:
    speed = 10
    maxTravel = 30000
    setNode = 4
    hubList = [(i, n) for i in range(300, 701, 200) for n in range(300, 701, 200)]

    def __init__(self, restoreData = None):
        # self.nodes = random.randint(4, 8)
        self.nodes = 4
        self.restaurants = []
        self.customers = []
        self.microhubs = []
        self.routeList = []
        self.hubs = Scenario.hubList
        if restoreData != None:
            self.nodes = restoreData[0]
            self.restaurants = restoreData[1]
            self.customers = restoreData[2]
            self.microhubs = restoreData[3]
        else:
            self.generateRestaurants()
            self.generateCustomers()
            self.generateMicrohubs()

    
    @classmethod
    def hubPoints(cls):
        h = {}
        h["points"] = cls.hubList
        return h


    def distance(self, i, k):
        return abs(i[0] - k[0]) + abs(i[1] - k[1])


    def generateRestaurants(self):
        for i in range(self.nodes):
            rCoord = lambda : random.randint(300, 700)
            self.restaurants.append((rCoord(), rCoord()))


    def generateCustomers(self):
        for i in range(self.nodes):
            x = random.randint(50, 950)
            y = 0
            if x > 300 and x < 700:
                y = random.randint(50, 300) if random.random() > 0.5 else random.randint(700, 950)
            else:
                y = random.randint(50, 950)
            self.customers.append((x, y))

    
    def generateMicrohubs(self):
        add = 0
        for restaurant in self.restaurants:
            bestDistance = 1000000
            bestIndex = 0
            for i, hub in enumerate(self.hubs):
                dist = self.distance(restaurant, hub)
                if dist < bestDistance:
                    bestDistance = dist
                    bestIndex = i
            self.microhubs.append(self.hubs[bestIndex])


    def noHubs(self):
        s = {}
        s["points"] = [(500, 500)] + self.restaurants + self.customers
        s["distance_matrix"] = [[self.distance(i, k) for i in s["points"]] for k in s["points"]]
        s["pickups_deliveries"] = [(r, r + self.nodes) for r in range(1, self.nodes + 1)]
        s["paths"] = self.routeList
        s["num_vehicles"] = int(self.nodes * 0.75)
        s["depot"] = 0
        s["hubs"] = False
        return s


    def withHubs(self):
        s = {}
        s["points"] = [(500, 500)] + self.microhubs + self.customers
        s["distance_matrix"] = [[self.distance(i, k) for i in s["points"]] for k in s["points"]]
        s["pickups_deliveries"] = [(r, r + self.nodes) for r in range(1, self.nodes + 1)]
        s["paths"] = self.routeList
        s["num_vehicles"] = int(self.nodes * 0.75)
        s["depot"] = 0
        s["true"] = False
        return s


    def groups(self):
        return [self.hubs, self.restaurants, self.customers]

    def groupsNoHubs(self):
        return [self.restaurants, self.customers]

    def groupsWithHubs(self):
        return [self.microhubs, self.customers]

    def save(self):
        return [[self.nodes], self.restaurants, self.customers, self.microhubs]