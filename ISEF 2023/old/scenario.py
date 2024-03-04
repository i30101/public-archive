import random

class Scenario:
    vehicles = 4
    maxTravel = 3000000
    speed = 50000
    routeList = []
    distance = lambda i, k : abs(i[0] - k[0]) + abs(i[1] - k[1])
    rDistance = sum([113, 99, 107, 126, 110, 101])
    cDistance = sum([47, 44, 44,  51, 47, 48])
    additionalTime = 0


    # @staticmethod
    # def generateScenario():
    #     output = []
    #     r = lambda : random.randint(50, 300) if random.random() > 0.5 else random.randint(700, 950)
    #     for i in range(10):
    #         output.append(f"({r()}, {r()})")
    #     print(", ".join(output))

    # Additional travel distance for restaurants:
    # [113, 99  107, 126, 110, 101]
    # Total additional travel time for restaurants: 656
    # Additional travel distance for customers:
    # [47, 44,  44,  51, 47, 48]
    # Total additional travel time for customers: 281
    # Difference between two adjustments: 375


    @staticmethod
    def generateAdjustments():
        rDistance = 100
        rStDev = 10
        cDistance = 50
        cStDev = 5
        rDistances = [int(random.normalvariate(rDistance, rStDev)) for i in range(6)]
        print(f"Additional travel distance for restaurants: \n{[str(distance) + ' ' for distance in rDistances]}")
        print(f"Total additional travel time for restaurants: {sum(rDistances)}")
        cDistances = [int(random.normalvariate(cDistance, cStDev)) for i in range(6)]
        print(f"Additional travel distance for customers: \n{[str(distance) + ' ' for distance in cDistances]}")
        print(f"Total additional travel time for customers: {sum(cDistances)}")
        print(f"Difference between two adjustments: {sum(rDistances) - sum(cDistances)}\n")


    def destinations():
        restaurants = [(476, 516), (656, 493), (306, 571), (403, 478), (373, 681), (639, 358)]
        hubs = [(340, 626), (440, 497), (648, 427)]
        return [restaurants, hubs]


    
    
    @staticmethod
    def controlScenario():
        data = {}
        data["points"] = [
            (500, 500), # starting point
            (476, 516), (656, 493), (306, 571), (403, 478), (373, 681), (639, 358), # restaurants
            (908, 895), (582, 778), (940, 768), (189, 286), (213, 191), (727, 110) # customers
        ]
        data["distance_matrix"] = [[Scenario.distance(p, point) for p in data["points"]] for point in data["points"]]
        data["pickups_deliveries"] = [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]
        data["num_vehicles"] = Scenario.vehicles
        data["depot"] = 0
        data["hubs"] = False
        return data


    @staticmethod
    def hubScenario():
        data = {}
        data["points"] = [
            (500, 500), # starting point
            (340, 626), (440, 497), (440, 498), (440, 499), (648, 427), (648, 426), # hubs
            (908, 895), (582, 778), (940, 768), (189, 286), (213, 191), (727, 110) # customers
        ]
        data["distance_matrix"] = [[Scenario.distance(p, point) for p in data["points"]] for point in data["points"]]
        # data["pickups_deliveries"] = [[1, 7], [2, 8], [2, 5], [2, 4], [3, 6], [3, 9]]
        data["pickups_deliveries"] = [[1, 10], [2, 11], [3, 8], [4, 7], [5, 9], [6, 12]]
        data["num_vehicles"] = Scenario.vehicles
        data["depot"] = 0
        data["hubs"] = True
        return data



    @staticmethod
    def presentScenario(d):
        for point in d["points"]:
            print(point)
        for row in d["distance_matrix"]:
            print(row)
        

    @staticmethod
    def customScenario1():
        data = {}
        data["points"] = [
            (500, 500), (875, 886), (323, 416), (496, 288), (826, 735), (542, 352), (506, 653), (940, 477), 
            (250, 314), (573, 217), (686, 917), (220, 685), (169, 741), (263, 319), (181, 243), (173, 588), (160, 523)
        ]
        # data["distance_matrix"] = [[abs(p[0] - point[0]) + abs(p[1] - point[1]) for p in data["points"]] for point in data["points"]]
        data["distance_matrix"] = [[Scenario.distance(p, point) for p in data["points"]] for point in data["points"]]
        data["time_matrix"] = [[distance / Scenario.speed for distance in point] for point in data["distance_matrix"]]
        data["demands"] = [0, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        data["vehicle_capacities"] = [1, 2, 3, 2, 3]
        data["pickups_deliveries"] = [[1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [8, 16]]
        data["paths"] = Scenario.routeList
        data["num_vehicles"] = Scenario.vehicles
        data["depot"] = 0
        return data


    def example1():
        data = {}
        data["points"] = [
            (456, 320), (228, 0), (912, 0), (0, 80), (114, 80), (570, 160), (798, 160), (342, 240),
            (684, 240), (570, 400), (912, 400), (114, 480), (228, 480), (342, 560), (684, 560), (0, 640), (798, 640)
        ]
        data["distance_matrix"] = [[abs(p[0] - point[0]) + abs(p[1] - point[1]) for p in data["points"]] for point in data["points"]]
        data["pickups_deliveries"] = [[1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [8, 16]]
        # data["paths"] = [[0, 5, 8, 6, 2, 10, 16, 14, 13, 0], [0, 7, 1, 4, 3, 15, 11, 12, 9, 0]]
        data["paths"] = Scenario.routeList
        data["num_vehicles"] = Scenario.vehicles
        data["depot"] = 0
        return data


    def example2():
        data = {}
        data['distance_matrix'] = [
            [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
            [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
            [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
            [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
            [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
            [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
            [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
            [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],
            [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],
            [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],
            [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354],
            [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],
            [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],
            [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],
            [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],
            [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],
            [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0],
        ]
        data['pickups_deliveries'] = [[1, 6], [2, 10], [4, 3], [5, 9], [7, 8], [15, 11], [13, 12], [16, 14]]
        data['num_vehicles'] = 4
        data['depot'] = 0
        return data
