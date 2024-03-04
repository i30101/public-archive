import matplotlib.pyplot as plt
import numpy as np
import random

# Generate dummy data as lists
x = list(range(50))
default1 = [0, 0.82, 0.86, 0.87, 0.88]
y1 = np.array([num + random.random() * 0.05 for num in default1] + [0.9 + random.random() * 0.02 for i in range(45)])
default2 = [0, 0.5, 0.79, 0.82, 0.83]
y2 = np.array([num + random.random() * 0.05 for num in default2] + [0.82 + random.random() * 0.02 for i in range(45)])
      
default3 = [2.5, 1.5, 1, 0.75]
y3 = np.array([num + random.random() * 0.2 for num in default3] + [0.5 + random.random() * 0.05 for i in range(46)])
default4 = [2.5, 1.5, 1, 0.5]
y4 = np.array([num + random.random() * 0.2 for num in default4] + [0.5 + random.random() * 0.05 for i in range(46)])


# Create the figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the first graph on the left
ax1.plot(x, y1, label='Accuracy', color='blue')
ax1.plot(x, y2, label='Validation', color='green')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')
ax1.set_title('Model Accuracy')
ax1.legend()

# Plot the second graph on the right
ax2.plot(x, y3, label='Train', color='blue')
ax2.plot(x, y4, label='Validation', color='green')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.set_title('Model Loss')
ax2.legend()

# Display the figure
plt.show()
