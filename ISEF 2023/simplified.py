import csv
from scenario import Scenario
from reader import Reader
from graph import Graph
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


diffPath = "./differences.csv"
distPath = "./distances.csv"
pickupPath = "./pickups.csv"


def find_solution(data):
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    dimension_name = "Distance"
    routing.AddDimension(transit_callback_index, 0, Scenario.maxTravel, True, dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    for request in data["pickups_deliveries"]:
        pickup_index = manager.NodeToIndex(request[0])
        delivery_index = manager.NodeToIndex(request[1])
        routing.AddPickupAndDelivery(pickup_index, delivery_index)
        routing.solver().Add(routing.VehicleVar(pickup_index) == routing.VehicleVar(delivery_index))
        routing.solver().Add(distance_dimension.CumulVar(pickup_index) <= distance_dimension.CumulVar(delivery_index))

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)    
    search_parameters.time_limit.seconds = 30

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        routeList = []
        total_distance = 0
        pickup_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)            
            plan_output = f"Route for vehicle {vehicle_id}:\n"
            planList = []
            route_distance = 0
            can = True
            while not routing.IsEnd(index):
                node = manager.IndexToNode(index)
                plan_output += f"{node} -> "
                planList.append(node)
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
                if can:
                    pickup_distance += route_distance
                    can = False
            routeList.append(planList + [0])
            total_distance += route_distance
        return (total_distance, int(pickup_distance))


def newTrialSimplified():
    differences = []
    distances = []
    pickupDistances = []
    for i in range(50):
        s = Scenario()
        noHubs = find_solution(s.noHubs())
        withHubs = find_solution(s.withHubs())
        dNoHubs = noHubs[0]
        dWithHubs = withHubs[0]
        improvement = dNoHubs - dWithHubs
        # if improvement > 200:
        print(dNoHubs, dWithHubs, improvement)
        differences.append(improvement)
        distances.append((dNoHubs, dWithHubs))
        pickupDistances.append((noHubs[1], withHubs[1]))
        del s
    Reader.write(diffPath, [[difference] for difference in differences])
    Reader.write(distPath, [[1, distance[0], distance[1]] for distance in distances])
    Reader.write(pickupPath, [[1, pickup[0], pickup[1]] for pickup in pickupDistances])


def present():
    data = []
    with open(diffPath, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(int(row[0]))
    print(f"Average decrease in travel distance: {sum(data) / len(data)} or ")
    Graph.histogram("Distribution of Improvements", "Improvement", "Count", 200, data)


if __name__ == "__main__":
    newTrialSimplified()
