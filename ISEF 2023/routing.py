"""Simple Pickup Delivery Problem (PDP)."""
from scenario import Scenario
from plotter import Plotter
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

class Routing:
    def __init__(self, d, p):
        self.data = d
        self.routeList = []
        self.total_distance = 0
        self.printDetails = p


    def print_solution(self, manager, routing, solution):
        """Prints solution on console."""
        if self.printDetails: 
            print(f"\nObjective: {solution.ObjectiveValue()}")
        for vehicle_id in range(self.data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f"Route for vehicle {vehicle_id}:\n"
            planList = []
            route_distance = 0
            while not routing.IsEnd(index):
                node = manager.IndexToNode(index)
                plan_output += f"{node} -> "
                planList.append(node)
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            self.routeList.append(planList + [0])
            plan_output += '{}\n'.format(manager.IndexToNode(index))
            plan_output += 'Distance of the route: {}m\n'.format(route_distance)
            if self.printDetails:
                print(plan_output)
            self.total_distance += route_distance
        if self.printDetails:
            print(f"Total distance of all routes: {self.total_distance}m")



    def find_solution(self):
        """Main body of program"""
        # create routing index manager
        manager = pywrapcp.RoutingIndexManager(len(self.data['distance_matrix']), self.data['num_vehicles'], self.data['depot'])

        # create routing model
        routing = pywrapcp.RoutingModel(manager)


        # create and register transit callback
        def distance_callback(from_index, to_index):
            """Returns distance between given nodes"""
            # convert from routing variable Index to distance matrix NodeIndex
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return self.data["distance_matrix"][from_node][to_node]
        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # define cost of each arc
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


        # add distance constraint
        dimension_name = "Distance"
        routing.AddDimension(
            transit_callback_index, #index for distance_callback
            0, #slack for delivery
            Scenario.maxTravel, # maximum vehicle travel distance
            True, # start time cumul at 0
            dimension_name)
        distance_dimension = routing.GetDimensionOrDie(dimension_name)
        distance_dimension.SetGlobalSpanCostCoefficient(100)


        # Define Transportation Requests.
        for request in self.data["pickups_deliveries"]:
            pickup_index = manager.NodeToIndex(request[0])
            delivery_index = manager.NodeToIndex(request[1])
            routing.AddPickupAndDelivery(pickup_index, delivery_index)
            routing.solver().Add(routing.VehicleVar(pickup_index) == routing.VehicleVar(delivery_index))
            routing.solver().Add(distance_dimension.CumulVar(pickup_index) <= distance_dimension.CumulVar(delivery_index))


        # set the first solution heuristic
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)    
        search_parameters.time_limit.seconds = 30


        # solve the problem
        solution = routing.SolveWithParameters(search_parameters)

        # status update
        if self.printDetails:
            print("Solver status: ", routing.status())

        # print solution
        if solution:
            self.print_solution(manager, routing, solution)
