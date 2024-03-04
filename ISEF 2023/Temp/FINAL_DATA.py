import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.interpolate import griddata


X = "microhubs"
Y = "deliverers"
VARIABLE = "distance"

# extract data from csv
data = pd.read_csv(r'newer_final.csv')


# creates graphic of 3-dimensional interploated graph
def linear_interpolation(dataframe):
    x = np.array(dataframe[X])
    y = np.array(dataframe[Y])
    z = np.array(dataframe[VARIABLE])
    
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)

    zi = griddata((x, y), z, (xi, yi), method="cubic")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xticks(x)
    ax.set_yticks(y)

    coolWarm = mcolors.LinearSegmentedColormap.from_list('cool_warm', ["red", "white", "blue"])
    warmCool = mcolors.LinearSegmentedColormap.from_list('cool_warm', ["blue", "white", "red"])
    
    surf = ax.plot_surface(xi, yi, zi, cmap=warmCool, linewidth=0, antialiased=False)

    ax.set_xlabel("Number of Microhubs")
    ax.set_ylabel("Number of Deliverers")
    ax.set_zlabel(f"Distance (km)")

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.title(f"Food Delivery Factors vs. {VARIABLE.capitalize()}")
    plt.show()


linear_interpolation(data)