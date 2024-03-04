# Author: Andrew Kim
# Version: 1.1.0 3, June 2023
# Estimator using single / unified normal distribution


import random
import numpy as np
import calc
from estimator import Estimator


# mean team sum: 169
# mean number of medals: 12
# mean average ranking: 6.43
class Ideal(Estimator):
    # default constructor
    def __init__(self, data: list):
        super().__init__()
        
        # find medals and nonmedals
        self.medals = [ranking for ranking in data if ranking < 7]
        self.nons = [ranking for ranking in data if ranking > 6]
        
        
        # first distribution for medals
        self.medal_mean = calc.mean(self.medals)
        self.medal_stdev = calc.stdev(self.medals)
    

    
    # ranking generator:
    def random_ranking(self) -> int:
        num = int(np.random.normal(self.medal_mean, self.medal_stdev))
        return num if num > 1 else 1
