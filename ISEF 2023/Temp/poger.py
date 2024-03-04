import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(num_points):
    return np.linspace(0, 1, num_points), np.random.rand(num_points)

def plot_graph(x, train_data, val_data, ylabel, title):
    plt.plot(x, train_data, label='Training')
    plt.plot(x, val_data, label='Validation')
    plt.xlabel('Epochs')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

# Generate random data for accuracy and loss
epochs = 50
x = np.arange(1, epochs + 1)

train_accuracy, val_accuracy = generate_random_data(epochs)
train_loss, val_loss = generate_random_data(epochs)

# Plot accuracy graph
plot_graph(x, train_accuracy, val_accuracy, 'Accuracy', 'Sample Model Accuracy')

# Plot loss graph
plot_graph(x, train_loss, val_loss, 'Loss', 'Sample Model Loss')
