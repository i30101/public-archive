import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.interpolate import griddata


CATEGORY = "deltime"

# extract data
hubs_without = pd.read_csv(r'hubs_without.csv')
hubs_with = pd.read_csv(r'hubs_with.csv')


# data without hubs
x1 = np.array(hubs_without["vh"])
y1 = np.array(hubs_without["perdel"])
z1 = np.array(hubs_without[CATEGORY])


# data with hubs
x2 = np.array(hubs_with["vh"])
y2 = np.array(hubs_with["perdel"])
z2 = np.array(hubs_with[CATEGORY])

print(z2)

# set axis ticks
xi1 = np.linspace(min(x1), max(x1), 100)
yi1 = np.linspace(min(y1), max(y1), 100)
xi1, yi1 = np.meshgrid(xi1, yi1)

xi2 = np.linspace(min(x2), max(x2), 100)
yi2 = np.linspace(min(y2), max(y2), 100)
xi2, yi2 = np.meshgrid(xi2, yi2)


zi1 = griddata((x1, y1), z1, (xi1, yi1), method="cubic")
zi2 = griddata((x2, y2), z2, (xi2, yi2), method="cubic")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# change order of colors to alter gradient
cool_warm = mcolors.LinearSegmentedColormap.from_list('cool_warm', ["blue", "white", "red"])

surf1 = ax.plot_surface(xi1, yi1, zi1, cmap=cool_warm, linewidth=0, antialiased=False)
blue = mcolors.LinearSegmentedColormap.from_list('my_colormap', ['darkblue', 'blue'])
surf2 = ax.plot_surface(xi2, yi2, zi2, cmap=blue, linewidth=0, antialiased=False)

# set axis labels
ax.set_xlabel("Vehicles per Hour")
ax.set_ylabel("Proportion of Deliverers")
ax.set_zlabel("Deliverer Cruising Time")


fig.colorbar(surf1, shrink=0.5, aspect=5)
plt.title("Vehicle Flow Rate vs. Delivery Vehicle Speed")

plt.show()

