import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import pandas as pd



# Load the data from CSV files
hubs_with = pd.read_csv("hubs_with.csv")
hubs_without = pd.read_csv("hubs_without.csv")


# creates heatmap of linear extrapolation
def create_heatmap(category, with_hubs: bool):
    dataframe = hubs_with if with_hubs else hubs_without
    
    # Extract x, y, and z data from the dataframes
    x = np.array(dataframe["vh"])
    y = np.array(dataframe["perdel"])
    z = np.array(dataframe[category])


    # Define grid for interpolation
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')


    # Plot heatmap
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(zi, cmap='viridis', origin='lower', extent=[0, 1, 0, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.colorbar(im)
    plt.show()
    
    
# def automated():
#     categories = ["bgtime" ,"deltime", "speed", "dist", "occ", "carpop"]
#     for category in categories:
#         print(f"{category.capitalize()} without microhubs")
#         create_heatmap(category, False)
#         print(f"{category.capitalize()} with microhubs")
#         create_heatmap(category, True)

