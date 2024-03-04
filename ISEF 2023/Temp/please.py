import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Generate epochs
epochs = np.arange(1, 51)

# Generate logarithmically increasing accuracy data for training and validation
train_accuracy = 0.5 + (1 - 0.9) * (1 - np.exp(-0.2 * epochs))
val_accuracy = 0.5 + (1 - 0.88) * (1 - np.exp(-0.18 * epochs))

# Add a smaller amount of noise to the accuracy values and clip to the valid range
train_accuracy += np.random.normal(0, 0.002, size=len(epochs))
print(train_accuracy)
val_accuracy += np.random.normal(0, 0.002, size=len(epochs))
train_accuracy = np.clip(train_accuracy, 0, 1)
val_accuracy = np.clip(val_accuracy, 0, 1)
print(train_accuracy)
# print(train_accuracy, len(train_accuracy))
# def check(num):
#     if num > 0.95:
#         return 1.8 - num
#     return num
# train_accuracy = np.array([check(num) for num in train_accuracy])
# print(train_accuracy, len(train_accuracy))
# val_accuracy = np.array([check(num) for num in val_accuracy])

# Generate exponentially decreasing loss data for training and validation
train_loss = 0.4 * np.exp(-0.2 * epochs)
val_loss = 0.5 * np.exp(-0.18 * epochs)

# Add a smaller amount of noise to the loss values
train_loss += np.random.normal(0, 0.002, size=len(epochs))
val_loss += np.random.normal(0, 0.002, size=len(epochs))

# Set up the side-by-side plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Create the accuracy plot
ax1.plot(epochs, train_accuracy, '-', linewidth=2, label="Train accuracy")
ax1.plot(epochs, val_accuracy, '-', linewidth=2, label="Validation accuracy")
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Accuracy')
ax1.set_title('Accuracy vs Epochs')
ax1.legend()
ax1.grid()

# Create the loss plot
ax2.plot(epochs, train_loss, '-', linewidth=2, label="Train loss")
ax2.plot(epochs, val_loss, '-', linewidth=2, label="Validation loss")
ax2.set_xlabel('Epochs')
ax2.set_ylabel('Loss')
ax2.set_title('Loss vs Epochs')
ax2.legend()
ax2.grid()

# Save and show the plots
plt.savefig('accuracy_and_loss_vs_epochs.png')
plt.show()