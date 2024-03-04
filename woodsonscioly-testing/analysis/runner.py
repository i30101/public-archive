# Author: Andrew Kim
# Version: 1.1.0, 3 June 2023
# Runner class to test estimators


# import external libraries
import numpy as np


# import custom libraries
import calc
from estimator import Estimator
from tournament import Tournament
from bimodal import Bimodal
from ideal import Ideal


# import estimators
from unified import Unified


# main method
def main(estimator, data):
    Estimator.set_print(False)
    
    print("Actual 2023 Team Ranking")
    states2023 = Tournament(data)
    states2023.summary()

    print("\nPredicted 2024 Team Rankings")
    unified = estimator(data)
    unified.simulate_tournaments(1000)
    unified.simulation_summaries()


if __name__ == "__main__":
    main(Bimodal, calc.woodson_23)
