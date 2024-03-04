import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata


# Set the global variable for the category
CATEGORY = "bgtime"

from scipy.interpolate import LinearNDInterpolator

def linear_interpolation():
    # Load the data from CSV files
    hubs_with = pd.read_csv("hubs_with.csv")
    hubs_without = pd.read_csv("hubs_without.csv")

    # Extract x, y, and z data from the dataframes
    x_with = np.array(hubs_with["vh"])
    y_with = np.array(hubs_with["perdel"])
    z_with = np.array(hubs_with[CATEGORY])
    x_without = np.array(hubs_without["vh"])
    y_without = np.array(hubs_without["perdel"])
    z_without = np.array(hubs_without[CATEGORY])

    # Create a meshgrid
    xi = np.linspace(min(x_with.min(), x_without.min()), max(x_with.max(), x_without.max()), 100)
    yi = np.linspace(min(y_with.min(), y_without.min()), max(y_with.max(), y_without.max()), 100)
    xi_mesh, yi_mesh = np.meshgrid(xi, yi)

    # Fill in the gaps in the data
    interp_with = LinearNDInterpolator(list(zip(x_with, y_with)), z_with)
    interp_without = LinearNDInterpolator(list(zip(x_without, y_without)), z_without)
    zi_with = interp_with(xi_mesh, yi_mesh)
    zi_without = interp_without(xi_mesh, yi_mesh)

    # Create the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surf_with = ax.plot_surface(xi_mesh, yi_mesh, zi_with, cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)
    surf_without = ax.plot_surface(xi_mesh, yi_mesh, zi_without, cmap=plt.cm.coolwarm, linewidth=0, antialiased=False, alpha=0.5)

    # Add labels to the axes
    ax.set_xlabel("Vehicles per Hour")
    ax.set_ylabel("Percent Deliverers")
    ax.set_zlabel(CATEGORY.capitalize())

    # Add a color bar to the plot
    fig.colorbar(surf_with, shrink=0.5, aspect=5)

    # Add a legend to the plot
    handles, labels = ax.get_legend_handles_labels()
    colors = [h.get_facecolor()[:3] for h in handles]
    ax.legend(handles, labels, facecolor=colors, edgecolor=colors)

    # Set the plot title
    plt.title(f"Vehicle Flow Rate vs. {CATEGORY.capitalize()} with and without Microhubs")

    # Display the plot
    plt.show()


# Call the function with and without hubs
linear_interpolation()
