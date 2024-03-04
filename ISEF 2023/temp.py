from scenario import Scenario
from plotter import Plotter
from routing import Routing

s = Scenario()
r = Routing(s.noHubs(), False)
r.find_solution()
print(r.print_solution())