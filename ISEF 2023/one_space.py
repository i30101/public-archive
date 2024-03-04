import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Data
salt_types = ['NaCl', 'KCl', 'CaCl2', 'MgCl2']
salt_amounts = [10, 15, 20, 30]
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

# Plot data points and regression lines in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i, salt_type in enumerate(salt_types):
    x = [i] * len(salt_amounts)
    y = salt_amounts
    z = times[i]
    ax.scatter(x, y, z, s=50)
    model = LinearRegression().fit(np.array([x, y]).T, np.array(z))
    r_squared = model.score(np.array([x, y]).T, np.array(z))
    intercept = model.intercept_
    slopes = model.coef_
    xs = np.linspace(min(x), max(x), 100)
    ys = np.linspace(min(y), max(y), 100)
    zs = intercept + slopes[0]*xs + slopes[1]*ys
    ax.plot(xs, [i]*100, zs, color='r', label=f'{salt_type}: z = {intercept:.2f} + {slopes[0]:.2f}*x + {slopes[1]:.2f}*y\nR^2 = {r_squared:.2f}')
ax.set_xlabel('Salt type')
ax.set_ylabel('Salt (grams per 200mL water)')
ax.set_zlabel('Time to melt (hrs)')
plt.legend()
plt.show()
