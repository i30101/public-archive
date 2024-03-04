import matplotlib.pyplot as plt
import numpy as np

class Graph:
    @staticmethod
    def histogram(t, xLabel, yLabel, b, d):
        fig, ax = plt.subplots(figsize = (10, 10))
        plt.title(t)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.hist(d, b)
        plt.show()

    
    @staticmethod
    def scatterplot(t, x, xLabel, y, yLabel):
        plt.title(t)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.scatter(x, y)
        plt.show()


    @staticmethod
    def bargraph(t, x, xLabel, y, yLabel):
        plt.title(t)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.bar(x, y)
        plt.show()


    @staticmethod
    def dotplot(d, t, xLabel, yLabel, **args):
        plt.figure(figsize = (6, 6))
        # Count how many times does each value occur
        unique_values, counts = np.unique(d, return_counts=True)
        
        # Convert 1D input into 2D array
        scatter_x = [] # x values 
        scatter_y = [] # corresponding y values
        for idx, value in enumerate(unique_values):
            for counter in range(1, counts[idx]+1):
                scatter_x.append(value)
                scatter_y.append(counter)

        # draw dot plot using scatter() 
        plt.scatter(scatter_x, scatter_y, **args)
        
        # Optional - show all unique values on x-axis. 
        # Matplotlib might hide some of them  
        plt.gca().set_xticks(unique_values)
        plt.title = t
        plt.xlabel = xLabel
        plt.ylabel = yLabel
        plt.show()