from scenario import Scenario
from routing import Routing
from router import Router
from plotter import Plotter
from reader import Reader
from graph import Graph

runs = 1
resultPath = "./data/results.csv"
bestPath = "./data/best.csv"
worstPath = "./data/worst.csv"
distancesPath = "./data/distances.csv"


def newTrial():
    improvements = []

    totalTravel = 0
    for i in range(runs):
        # initialize scenario
        s = Scenario()
        
        # perfrom vrp for no hub scenario
        r = Routing(s.noHubs(), False)
        r.find_solution()
        s.routeList = r.routeList
        noHubDistance = r.total_distance + 800
        totalTravel += noHubDistance

        # perform vrp for hub scenario
        r = Routing(s.withHubs(), False)
        r.find_solution()
        s.routeList = r.routeList
        withHubDistance = r.total_distance

        # output travel distance difference
        improvement = noHubDistance - withHubDistance
        print(improvement)
        Plotter.plotGroups(s.groups())
        Plotter.plotPaths(s.noHubs())
        Plotter.plotPaths(s.withHubs())

        improvements.append(improvement)
        
        # clean up objects
        del s
        del r
    # Reader.write(resultPath, [[improvement] for improvement in improvements])
    print(f"Average decrease in travel distance: {sum(improvements) / runs} or {100 * sum(improvements) / totalTravel}%")
    # retrieve()


def newTrialSimplified():
    improvements = []
    totalTravel = 0
    max = 0
    min = 0
    for i in range(runs):
        s = Scenario()
        if i % 1000 == 0:
            print(i)
        noHubDistance = Router.find_solution(s.noHubs()) + 800
        totalTravel += noHubDistance
        withHubDistance = Router.find_solution(s.withHubs())
        improvement = noHubDistance - withHubDistance
        improvements.append(improvement)
        if improvement > max:
            Reader.write(bestPath, s.save())
            max = improvement
        elif improvement < min:
            Reader.write(worstPath, s.save())
            min = improvement
        del s
    Reader.write(resultPath, [[improvement] for improvement in improvements])
    print(f"Average decrease in travel distance: {sum(improvements) / runs} or {100 * sum(improvements) / totalTravel}%")
    retrieve()


def retrieve():
    retrieved = [int(i[0]) for i in Reader.extractRows(resultPath)]
    Graph.histogram("Distribution of Improvements", "Improvement", "Count", 200, retrieved)


def restore(saved):
    unprocessed = Reader.extractRows(bestPath if saved == "best" else worstPath)

    def extract(groupList):
        processed = []
        for group in groupList:
            tempGroup = group.replace("(", "").replace(")", "").replace("[", "").replace("]", "").split(", ")
            tempGroup = [int(i) for i in tempGroup]
            processed.append(tempGroup)
        return processed
    
    nodes = int(unprocessed[0][0])
    restaurants = extract(unprocessed[1])
    customers = extract(unprocessed[2])
    microhubs = extract(unprocessed[3])
    return Scenario([nodes, restaurants, customers, microhubs])


def presentRestored(saved = "best"):
    # initialize scenario
    s = restore(saved)
    
    # perfrom vrp for no hub scenario
    r = Routing(s.noHubs(), False)
    r.find_solution()
    s.routeList = r.routeList
    noHubDistance = r.total_distance
    Plotter.plotGroups(s.groupsNoHubs())
    Plotter.plotPaths(s.noHubs())


    # perform vrp for hub scenario
    r = Routing(s.withHubs(), False)
    r.find_solution()
    s.routeList = r.routeList
    withHubDistance = r.total_distance
    Plotter.plotGroups(s.groupsWithHubs())
    Plotter.plotPaths(s.withHubs())


    # output travel distance difference
    improvement = noHubDistance - withHubDistance
    print(f"Decrease in travel distance: {improvement} or {100 * improvement / noHubDistance}%")


def recordDistances():
    distances = []

    totalTravel = 0
    for i in range(runs):
        # initialize scenario
        s = Scenario()
        temp = []
        
        # perfrom vrp for no hub scenario
        r = Routing(s.noHubs(), False)
        r.find_solution()
        temp.append(r.total_distance + 800)

        # perform vrp for hub scenario
        r = Routing(s.withHubs(), False)
        r.find_solution()
        temp.append(r.total_distance)

        distances.append(temp)
    
    Reader.write(distancesPath, distances)


if __name__ == "__main__":
    newTrial()