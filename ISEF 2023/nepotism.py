import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Data
salt_types = ['NaCl', 'KCl', 'CaCl2', 'MgCl2']
salt_amounts = [0.5, 1.0, 1.5, 2.0]
times = [
    [0.948, 0.856, 0.732, 0.588],
    [1.042, 0.978, 0.758, 0.716],
    [0.754, 0.715, 0.603, 0.484],
    [1.146, 0.986, 0.804, 0.703]
]

nacl = ["0:56:58",	"0:51:22",	"0:43:49",	"0:35:28"]
kcl = ["1:02:35",	"0:58:43",	"0:45:31",	"0:42:57"]
cacl2 = ["0:45:16",	"0:42:54",	"0:36:15",	"0:29:03"]
mgcl2 = ["1:08:45",	"0:59:11",	"0:48:12",	"0:42:15"]

times[0] = nacl
times[1] = kcl
times[2] = cacl2
times[3] = mgcl2

# Convert time data to decimal format
def to_decimal_time(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h + m/60 + s/3600

times = [[to_decimal_time(t) for t in lst] for lst in times]

# # Plot data points on a 3D plane
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for i, salt_type in enumerate(salt_types):
#     xs = [i] * len(salt_amounts)
#     ys = salt_amounts
#     zs = times[i]
#     ax.scatter(xs, ys, zs, s=50)
# ax.set_xticks(range(len(salt_types)))
# ax.set_xticklabels(salt_types)
# ax.set_xlabel('Salt type')
# ax.set_ylabel('Salt (grams per 200mL water)')
# ax.set_zlabel('Time to melt (hrs)')
# plt.show()

# # Perform linear regression
# X = np.array([[i]*len(salt_amounts) for i in range(len(salt_types))]).flatten().reshape(-1, 1)
# y = np.array(times).flatten()
# model = LinearRegression().fit(X, y)
# r_squared = model.score(X, y)
# print(f'Time to melt = {model.intercept_:.2f} + {model.coef_[0]:.2f}*Salt type + {model.coef_[1]:.2f}*Salt (R^2 = {r_squared:.2f})')

# Plot data points and regression lines
fig, axs = plt.subplots(1, 4, figsize=(12, 4), sharey=True)
colors = ['b', 'g', 'r', 'c']
for i, salt_type in enumerate(salt_types):
    x = salt_amounts
    y = times[i]
    axs[i].scatter(x, y, s=50, color=colors[i])
    model = LinearRegression().fit(np.array(x).reshape(-1, 1), np.array(y))
    r_squared = model.score(np.array(x).reshape(-1, 1), np.array(y))
    intercept = model.intercept_
    slope = model.coef_[0]
    xs = np.linspace(min(x), max(x), 100)
    ys = intercept + slope * xs
    axs[i].plot(xs, ys, color=colors[i], label=f'y = {slope:.2f}x + {intercept:.2f}\nR^2 = {r_squared:.2f}')
    # axs[i].set_title(salt_type)
    axs[i].set_xlabel(f"Concentration of {salt_type} (M)")
    axs[i].legend()
fig.suptitle('Concetrations of Salts vs. Melting Duration')
axs[0].set_ylabel('Time to melt (hrs)')
plt.show()
