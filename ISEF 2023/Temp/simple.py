import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.interpolate import griddata


CATEGORY = "availability"

# extract data from csv
hubs_without = pd.read_csv(r'hubs_without.csv')
# print(hubs_without)
hubs_with = pd.read_csv(r'hubs_with.csv')
# print(hubs_with)


# creates graphic of 3-dimensional interploated graph
def linear_interpolation(dataframe):
    x = np.array(dataframe["bikes"])
    y = np.array(dataframe["stations"])
    z = np.array(dataframe[CATEGORY])
    
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)

    zi = griddata((x, y), z, (xi, yi), method="cubic")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    cool_warm = mcolors.LinearSegmentedColormap.from_list('cool_warm', ["red", "white", "blue"])
    
    surf = ax.plot_surface(xi, yi, zi, cmap=cool_warm, linewidth=0, antialiased=False)

    ax.set_xlabel("Number of Electric Bicycle")
    ax.set_ylabel("Number of Electric Bicycle Stations")
    ax.set_zlabel("Parking Space Availability")

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.title(f"Electric Bicycle Deployment vs. Parking Space Availability")
    plt.show()

data = pd.read_csv(r'generated_lagos.csv')
linear_interpolation(data)