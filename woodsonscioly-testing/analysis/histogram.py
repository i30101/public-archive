import matplotlib.pyplot as plt
import calc
import numpy as np


def histogram(data):
    num_bins = max(data) - min(data) + 1

    hist_values, _ = np.histogram(data, bins=num_bins)

    plt.hist(data, bins=[x - 0.5 for x in range(min(data), max(data)+2)], edgecolor='black')

    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")

    plt.xticks(range(min(data), max(data)+1))
    plt.yticks(range(0, int(max(hist_values))+1))
    plt.show()
    
histogram(calc.example)