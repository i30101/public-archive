from graph import Graph
from reader import Reader

normalPath = "./normal.csv"

titles = ["Vehicle Flow Rate vs. Background Traffic Cruising Duration",
          "Vehicle Flow Rate vs. Delivery Vehicle Cruising Duration", 
          "Vehicle Flow Rate vs. Mean Vehicle Speed", 
          "Vehicle Flow Rate vs. Mean Distance Parked from Destination",
          "Vehicle Flow Rate vs. Percent of Spaces Occupied"]

normal = Reader.extractRows(normalPath)
for i in range(5):
    print(titles[i])
    residuals = [float(row[i]) for row in normal[1:]]
    output = " ".join([str(r) for r in residuals])
    Graph.histogram(titles[i], "Residual", "Count", 10, residuals)