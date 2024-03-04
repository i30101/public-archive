# Author: Andrew Kim
# Version: 1.0.2, 3 June 2023
# Helper class to calculate tournament metrics


import math


# list of rankings for 2023 VASO states tournament
tj_23 = [1, 1, 1, 3, 1, 3, 6, 3, 1, 1, 1, 4, 3, 5, 3, 1, 6, 1, 6, 11, 17, 14, 3]
langley_23 = [3, 3, 11, 2, 5, 2, 8, 2, 7, 3, 11, 14, 7, 2, 6, 12, 9, 2, 2, 6, 3, 12, 14]
fairfax_23 = [5, 13, 2, 6, 14, 1, 5, 6, 18, 22, 2, 17, 5, 6, 7, 3, 8, 3, 3, 1, 2, 1, 1]
woodson_23 = [14, 10, 8, 13, 7, 5, 2, 5, 9, 5, 16, 2, 4, 3, 1, 2, 3, 6, 8, 8, 7, 11, 6]
example = [9, 9, 3, 1, 1, 14, 1, 3, 2, 5, 4, 7, 6, 11, 5, 1, 15, 3, 2, 13, 9, 4, 9]

# rounds to two decimal points
def rnd(n) -> float:
    return round(n, 2)


# calculates mean of given data
def mean(data: list) -> float:
    return rnd(sum(data) / len(data))


# calculates standard deviation of given data
def stdev(data: list):
    m = mean(data)
    return rnd(math.sqrt(sum([(m - rank) ** 2 for rank in data]) / (len(data) - 1)))
