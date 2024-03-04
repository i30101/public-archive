# Author: Andrew Kim
# Version: 1.0.0, 3 June 2023
# Tournament result manager class


import calc
from colorama import init, Fore, Style


# initalize colorama
init()


# class for managing data simulated tournaments
class Tournament:
    def __init__(self, data = None, func = None):
        # data is not given, use function to generate values
        if data is None and func != None:
            self.rankings = [func() for i in range(23)]
        # data is given 
        elif data is not None and func == None:
            self.rankings = data
        else:
            print("Parameter type error")
        self.process_data()
        
    
    # calculate tournament metrics
    def process_data(self):
        self.medals = len([ranking for ranking in self.rankings if ranking < 7])
        self.mean = calc.mean(self.rankings)
        self.summed = sum(self.rankings)
        self.mean = calc.mean(self.rankings)
        self.stdev = calc.stdev(self.rankings)


    # print tournament summary
    def summary(self):
        print(f"{self.summed}\t{self.medals}\t{self.mean}\t", end="")
        
        # print formattted rankings
        for ranking in self.rankings:
            ranking_string = str(ranking) + ("  " if ranking < 10 else " ")
            match(ranking):
                case 1:
                    print(Fore.YELLOW + ranking_string, end="")
                case 2:
                    print(Style.RESET_ALL + ranking_string, end="")
                case 3:
                    print(Fore.LIGHTRED_EX + ranking_string, end="")
                case 4:
                    print(Fore.LIGHTWHITE_EX + ranking_string, end="")
                case 5:
                    print(Fore.LIGHTGREEN_EX + ranking_string, end="")
                case 6:
                    print(Fore.LIGHTMAGENTA_EX + ranking_string, end="")
                case _:
                    print(Fore.LIGHTBLACK_EX + ranking_string, end="")
        print(Style.RESET_ALL)