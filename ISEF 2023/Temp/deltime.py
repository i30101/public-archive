import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


CATEGORY = "speed"

# extract data from csv
hubs_without = pd.read_csv(r'hubs_without.csv')
# print(hubs_without)
hubs_with = pd.read_csv(r'hubs_with.csv')
# print(hubs_with)


# creates graphic of 3-dimensional interploated graph
def linear_interpolation(with_hubs):
    dataframe = hubs_with if with_hubs else hubs_without
    x = np.array(dataframe["vh"])
    y = np.array(dataframe["perdel"])
    z = np.array(dataframe[CATEGORY])
    
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)

    zi = griddata((x, y), z, (xi, yi), method="cubic")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    
    surf = ax.plot_surface(xi, yi, zi, cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_xlabel("Vehicles per Hour")
    ax.set_ylabel("DSLs per 25 feet")
    ax.set_zlabel("Average Vehicle Speed")

    fig.colorbar(surf, shrink=0.5, aspect=5)

    with_without = "with" if with_hubs else "without"
    print(with_without)
    plt.title(f"Vehicle Flow Rate vs. {CATEGORY.capitalize()} {with_without} Microhubs")
    plt.show()

linear_interpolation(False)
linear_interpolation(True)