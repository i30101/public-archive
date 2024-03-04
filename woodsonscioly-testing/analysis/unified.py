# Author: Andrew Kim
# Version: 1.1.0, 3 June 2023
# Estimator using single / unified normal distribution


import numpy as np
import calc
from estimator import Estimator


# mean team sum: 169
# mean number of medals: 12
# mean average ranking: 6.43
class Unified(Estimator):
    # default constructor
    def __init__(self, data: list):
        super().__init__()
        
        # calculate sampling distribution parameters
        self.mean = calc.mean(data) - 1
        self.stdev = calc.stdev(data)
                
        # list for storing competition results
    
    
    # ranking generator:
    def random_ranking(self) -> int:
        num = int(np.random.normal(self.mean, self.stdev) + 1)
        return num if num > 0 else 1
