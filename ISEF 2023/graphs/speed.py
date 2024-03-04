# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df_no_hubs = pd.read_csv(r'./graphs\microhubs_sf_-_no_hubs_1.csv')
#print(df_no_hubs)

df_with_hubs = pd.read_csv(r'./graphs\microhubs_sf_-_yes_hubs.csv')
#print(df_yes_hubs)

# Creating dataset
z1 = df_no_hubs[df_no_hubs.columns[4:5]]
x1 = df_no_hubs[df_no_hubs.columns[0:1]]
y1 = df_no_hubs[df_no_hubs.columns[1:2]]

z2 = df_with_hubs[df_with_hubs.columns[4:5]]
x2 = df_with_hubs[df_with_hubs.columns[0:1]]
y2 = df_with_hubs[df_with_hubs.columns[1:2]]

def linReg(y1_data, z1_data, y2_data, z2_data, num_vehicles):
    model = LinearRegression()
    model.fit(y1_data, z1_data)

    y1_new = np.linspace(0, 0.1)
    z1_new = model.predict(y1_new[:, np.newaxis])

    ax.plot(y1_new, z1_new, zs = num_vehicles, zdir = 'x', linewidth = 0.5, color = 'red')
    
    model1 = LinearRegression()
    model1.fit(y2_data, z2_data)

    y2_new = np.linspace(0, 0.1)
    z2_new = model1.predict(y2_new[:, np.newaxis])

    ax.plot(y2_new, z2_new, zs = num_vehicles, zdir = 'x', linewidth = 0.5, color = 'blue')
    

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D(x1, y1, z1, color = "red", label = "No Microhubs")
ax.scatter3D(x2, y2, z2, color = "blue", label = "With Microhubs")

ax.set_xticks([5000, 6000, 7000, 8000, 9000])
#ax.set_yticks([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1])

# Plot Linear Regressions
linReg(y1[0:10], z1[0:10], y2[0:10], z2[0:10], 5000)
linReg(y1[10:20], z1[10:20], y2[10:20], z2[10:20], 6000)
linReg(y1[20:30], z1[20:30], y2[20:30], z2[20:30], 7000)
linReg(y1[30:40], z1[30:40], y2[30:40], z2[30:40], 8000)
linReg(y1[40:50], z1[40:50], y2[40:50], z2[40:50], 9000)

# Set label
ax.set_xlabel('Hourly Inflow of Vehicles', linespacing = 3)
ax.set_ylabel('Proportion of Delivery Vehicles')
ax.set_zlabel('Mean Vehicle Speed (mph)')

plt.title("Vehicle Flow Rate v.s. Mean Vehicle Speed")

# Set viewing angle
#ax.view_init(-140, 60)

plt.legend()
 
# show plot
plt.show()
