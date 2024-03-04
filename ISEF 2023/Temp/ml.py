import matplotlib.pyplot as plt
import numpy as np

# Generate random data for accuracy and loss
epochs = np.arange(1, 21)
train_accuracy = np.linspace(0.6, 0.9, num=20) + np.random.uniform(-0.01, 0.01, size=(20,))
val_accuracy = np.linspace(0.65, 0.95, num=20) + np.random.uniform(-0.01, 0.01, size=(20,))
train_loss = np.linspace(0.5, 0.1, num=20) + np.random.uniform(-0.01, 0.01, size=(20,))
val_loss = np.linspace(0.4, 0.2, num=20) + np.random.uniform(-0.01, 0.01, size=(20,))

# Set style and context for the plot
plt.style.use('ggplot')
plt.rc('font', size=10)
plt.rc('axes', titlesize=10, labelsize=10)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('legend', fontsize=10)
plt.rc('figure', titlesize=10)

# Create figure and axes objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))

# Plot accuracy vs epoch
ax1.plot(epochs, train_accuracy, label='Training Accuracy')
ax1.plot(epochs, val_accuracy, label='Validation Accuracy')

# Set x and y limits
ax1.set_xlim([1, 20])
ax1.set_ylim([0.6, 1.0])

# Set x and y labels
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')

# Add title and legend
ax1.set_title('Accuracy vs Epoch')
ax1.legend()

# Plot loss vs epoch
ax2.plot(epochs, train_loss, label='Training Loss')
ax2.plot(epochs, val_loss, label='Validation Loss')

# Set x and y limits
ax2.set_xlim([1, 20])
ax2.set_ylim([0.1, 0.5])

# Set x and y labels
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')

# Add title and legend
ax2.set_title('Loss vs Epoch')
ax2.legend()

# Show the plot
plt.show()
