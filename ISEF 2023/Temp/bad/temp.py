import numpy as np
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


CATEGORY = "deltime"

# Load the data from CSV files
hubs_without = pd.read_csv("hubs_without.csv")
hubs_with = pd.read_csv("hubs_with.csv")



# Define the two datasets
x1 = np.sort(np.array(hubs_without["vh"]))
y1 = np.sort(np.array(hubs_without["perdel"]))
z1 = np.sort(np.array(hubs_without[CATEGORY]))

x2 = np.sort(np.array(hubs_with["vh"]))
y2 = np.sort(np.array(hubs_with["perdel"]))
z2 = np.sort(np.array(hubs_with[CATEGORY]))

# Interpolator functions
interp1 = RegularGridInterpolator((x1, y1, z1), hubs_without)
interp2 = RegularGridInterpolator((x2, y2, z2), hubs_with)

# Extrapolation points
x_new = np.linspace(-0.5, 1.5, 20)
y_new = np.linspace(-0.5, 1.5, 20)
z_new = np.linspace(-0.5, 1.5, 20)
X_new, Y_new, Z_new = np.meshgrid(x_new, y_new, z_new, indexing='ij')

# Extrapolate the data
points_new = np.array([X_new.ravel(), Y_new.ravel(), Z_new.ravel()]).T
data1_extrapolated = interp1(points_new, method='nearest').reshape(X_new.shape)
data2_extrapolated = interp2(points_new, method='nearest').reshape(X_new.shape)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first dataset extrapolation
ax.scatter(X_new, Y_new, Z_new, c=data1_extrapolated.ravel(), marker='o', alpha=0.5, label='Dataset 1 Extrapolation')

# Plot the second dataset extrapolation
ax.scatter(X_new, Y_new, Z_new, c=data2_extrapolated.ravel(), marker='^', alpha=0.5, label='Dataset 2 Extrapolation')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
