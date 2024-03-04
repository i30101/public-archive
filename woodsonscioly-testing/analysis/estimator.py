# Author: Andrew Kim
# Version: 1.0.0, 3 June 2023
# Tempalte class for estimators


import numpy as np
import calc
from tournament import Tournament


class Estimator:
    print_results = False
    
    # default constructor
    def __init__(self):
        # list for storing tournament results
        self.tournaments = []
    
    
    # ranking generator
    def random_ranking(self):
        return 1
    
    # simulate tournamnets
    def simulate_tournaments(self, n: int):
        for i in range(n):
            self.tournaments.append(Tournament(None, self.random_ranking))
            
            
    # output results
    def simulation_summaries(self):
        means = []
        stdevs = []
        medals = []
        sums = []
        
        # iterate through all tournaments
        for tournament in self.tournaments:
            means.append(tournament.mean)
            stdevs.append(tournament.stdev)
            medals.append(tournament.medals)
            sums.append(tournament.summed)
            
            # print tournament results if desired
            if Estimator.print_results:
                tournament.summary()
            
        # print final results
        print(f"{calc.mean(sums)}\t{calc.mean(medals)}\t{calc.mean(means)}\t{calc.stdev(stdevs)}")
        
        
    @classmethod
    def set_print(cls, b: bool):
        Estimator.print_results = b