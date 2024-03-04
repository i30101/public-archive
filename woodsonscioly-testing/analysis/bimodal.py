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
class Bimodal(Estimator):
    # default constructor
    def __init__(self, data: list):
        super().__init__()
        
        # find medals and nonmedals
        self.medals = [ranking for ranking in data if ranking < 7]
        self.nons = [ranking for ranking in data if ranking > 6]
        
        
        # first distribution for medals
        self.medal_mean = calc.mean(self.medals)
        self.medal_stdev = calc.stdev(self.medals)
        
        
        # second distribution for nonmedals
        self.non_mean = calc.mean(self.nons)
        self.non_stdev = calc.mean(self.nons) - 1
    

    
    # ranking generator:
    def random_ranking(self) -> int:
        num = 0
        if random.uniform(1, 23) < 21:
            num = int(np.random.normal(self.medal_mean, self.medal_stdev))
        else:
            num = int(np.random.normal(self.non_mean, self.non_stdev))
        return num if num > 1 else 1
