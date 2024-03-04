import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


# extract data
hubs_without = pd.read_csv(r'hubs_without.csv')
hubs_with = pd.read_csv(r'hubs_with.csv')


# data without hubs
x1 = np.array(hubs_without["vh"])
y1 = np.array(hubs_without["perdel"])
z1 = np.array(hubs_without["deltime"])


# data with hubs
x2 = np.array(hubs_with["vh"])
y2 = np.array(hubs_with["perdel"])
z2 = np.array(hubs_with["deltime"])

# Define the grid
xi = np.linspace(min(x1), max(x1), 1000)
yi = np.linspace(min(y1), max(y1), 100)
xi, yi = np.meshgrid(xi, yi)
print(yi)

# Interpolate the data onto the grid
zi1 = griddata((x1, y1), z1, (xi, yi), method='linear')
zi2 = griddata((x2, y2), z2, (xi, yi), method='linear')

# Create a new 3D plot
fig = plt.figure()
ax = Axes3D(fig)

# Plot the interpolated surfaces
surf1 = ax.plot_surface(xi, yi, zi1, cmap='viridis', alpha=0.5)
surf2 = ax.plot_surface(xi, yi, zi2, cmap='plasma', alpha=0.5)

# Add a colorbar for each surface
fig.colorbar(surf1, ax=ax)
fig.colorbar(surf2, ax=ax)

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()