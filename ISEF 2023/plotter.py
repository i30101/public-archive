import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class Plotter:
    dMin = 0
    dMax = 1000
    tickInterval = dMax / 10
    colors = ["coral", "cornflowerblue", "crimson", "darkmagenta", "darkseagreen", "gold", "brown", "darkblue", "darkolivegreen"]


    # graphs points
    # d: dictionary of situation data
    @staticmethod
    def plotPoints(d):
        points = d["points"]        
        fig, ax = plt.subplots(figsize = (6, 6))
        ax.set_xlim(Plotter.dMin, Plotter.dMax)
        ax.set_ylim(Plotter.dMin, Plotter.dMax)
        ax.xaxis.set_major_locator(MultipleLocator(Plotter.tickInterval))
        ax.yaxis.set_major_locator(MultipleLocator(Plotter.tickInterval))
        ax.xaxis.set_ticklabels([])
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticklabels([])
        ax.yaxis.set_ticks_position('none')
        for i, point in enumerate(points):
            plt.text(point[0], point[1], i)
            plt.plot(point[0], point[1], "o", color = "black")
        plt.tight_layout(pad = 1, w_pad = 1, h_pad = 1)
        plt.grid()
        plt.show()


    @staticmethod
    def plotGroups(d):
        fig, ax = plt.subplots(figsize = (6, 6))
        ax.set_xlim(Plotter.dMin, Plotter.dMax)
        ax.set_ylim(Plotter.dMin, Plotter.dMax)
        ax.xaxis.set_major_locator(MultipleLocator(Plotter.tickInterval))
        ax.yaxis.set_major_locator(MultipleLocator(Plotter.tickInterval))
        ax.xaxis.set_ticklabels([])
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticklabels([])
        ax.yaxis.set_ticks_position('none')
        count = 1
        for c, group in enumerate(d):
            color = Plotter.colors[c]
            for i, point in enumerate(group):
                plt.text(point[0], point[1], count)
                plt.plot(point[0], point[1], "o", color = color)
                count += 1
        plt.tight_layout(pad = 1, w_pad = 1, h_pad = 1)
        plt.grid()
        plt.show()
            



    # graphs paths
    # d: dictionary of situation data
    @staticmethod
    def plotPaths(d):
        points = d["points"]
        paths = d["paths"]
        fig, ax = plt.subplots(figsize = (6, 6))
        ax.set_xlim(Plotter.dMin, Plotter.dMax)
        ax.set_ylim(Plotter.dMin, Plotter.dMax)
        ax.xaxis.set_major_locator(MultipleLocator(Plotter.tickInterval))
        ax.yaxis.set_major_locator(MultipleLocator(Plotter.tickInterval))
        ax.xaxis.set_ticklabels([])
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticklabels([])
        ax.yaxis.set_ticks_position('none')
        for c, path in enumerate(paths):
            fullPath = [0] + path
            color = Plotter.colors[c]
            for i, pointID in enumerate(fullPath):
                point = points[pointID]
                pointX = point[0]
                pointY = point[1]
                nextPoint = points[fullPath[i + 1] if i < len(fullPath) - 1 else 0]
                nextX = nextPoint[0]
                nextY = nextPoint[1]
                m = (nextY - pointY) / (nextX - pointX) if nextX - pointX != 0 else 0
                f = lambda x : m * (x - pointX) + pointY
                midX = (pointX + nextX) / 2
                midY = f(midX)
                dX = 0.01 if pointX <= nextX else -0.01
                dY = f(midX + dX) - midY
                plt.arrow(midX, midY, dX, dY, shape = "full", lw = 5, length_includes_head = True, head_width = 2, color = color)
                plt.plot([point[0], nextPoint[0]], [point[1], nextPoint[1]], color = color, marker = "o", markersize = 8)
        plt.tight_layout(pad = 1, w_pad = 1, h_pad = 1)
        plt.grid(True)
        plt.show()
