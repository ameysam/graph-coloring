from country import Country
from empire import Empire
from constants import Constant
import numpy as np
import random as rn

def randomSelection(P):
    r = rn.random()
    C = np.cumsum(P)
    index = [i for i, x in enumerate(C) if r <= x]
    return index[0]  # we only need the first entry that statisfies the check

iteration = 0

class Ica:
    def __init__(self):
        self.countries = []
        self.empires = []
        self.colonies = []

    def createCountries(self):
        count = Constant.COUNTRIES_COUNT
        for i in range(count):
            color = Constant.COUNTRY_COLORS[np.random.randint(0, 3, 1)[0]]
            self.countries.append(Country(color))

        return self.countries


    def createEmpires(self):
        countries = self.countries

        empires = countries[: Constant.EMPIRES_COUNT]
        colonies = countries[Constant.EMPIRES_COUNT: ]

        for imperialist in empires:
            self.empires.append(Empire(imperialist))

        i = 0
        while i < len(colonies):
            colony = colonies[i]
            imperialist = np.random.randint(0, Constant.EMPIRES_COUNT, 1)[0]
            empire = self.empires[imperialist]
            if empire.coloniesCount() < 9:
                empire.addColony(colony)
                i += 1

        return self.empires



    def absorb(self):
        for empire in self.empires:
            colonies = empire.getColonies()
            for i in range(len(colonies)):
                colony = colonies[i]
                if colony.cost < empire.imperialist.cost:
                    empire.colonies.append(empire.imperialist)
                    empire.imperialist = colony
                    del empire.colonies[i]


            empire.calcCost()



    def competition(self):


        empiresTotalCost = np.array([empire.calcCost() for empire in self.empires])


        minimum_index = np.argmin(empiresTotalCost)

        iter = 0

        while empiresTotalCost[minimum_index] > 0:
            self.iteration(minimum_index, empiresTotalCost)
            empiresTotalCost = np.array([empire.calcCost() for empire in self.empires])
            minimum_index = np.argmin(empiresTotalCost)
            iter += 1
            print(iter, empiresTotalCost[minimum_index])

        return self.empires[minimum_index]


    def iteration(self, minimum_index, empiresTotalCost):

        weakest_empire_index = minimum_index
        weakest_empire = self.empires[weakest_empire_index]

        P = np.divide(empiresTotalCost, empiresTotalCost.sum())
        P = np.flip(P, 0)

        weakest_empire_colonies_cost = np.array([colony.getCost() for colony in weakest_empire.getColonies()])

        weakest_colony_index = np.argmax(weakest_empire_colonies_cost)
        weakest_colony = weakest_empire.getColony(weakest_colony_index)

        winning_empire_index = randomSelection(P)
        winning_empire = self.empires[winning_empire_index]

        index = winning_empire.getCheapestColony()
        old_winning_empire_colony = winning_empire.replaceColony(weakest_colony, index)

        weakest_empire.replaceColony(old_winning_empire_colony, weakest_colony_index)
