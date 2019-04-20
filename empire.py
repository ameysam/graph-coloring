from constants import Constant
import string
import random
import numpy as np


class Empire:
    def __init__(self, imperialist):
        self.imperialist = imperialist
        self.costs = [0, 0, 0, 0, 0]
        self.cost = 0
        self.countries = []
        self.colonies = []
        self.name = 'Empire_{}'.format(random.choices(string.ascii_uppercase, k=1))

    def calcCost(self):
        self.costs = [0, 0, 0, 0, 0]
        self.countries = self.getCountries()

        for i in range(len(self.countries)):
            conflicts = Constant.RULE_MATRIX[i]
            for j in range(len(conflicts)):
                if conflicts[j] == 1:
                    if self.countries[i].color == self.countries[j].color:
                        self.costs[i] += 1
            self.countries[i].updateCost(self.costs[i])

        self.cost = sum(self.costs)
        return self.cost

    def getCheapestColony(self):
        empiresTotalCost = np.array([colony.getCost() for colony in self.colonies])
        return np.argmin(empiresTotalCost)

    def getColonies(self):
        return self.colonies

    def addColony(self, colony):
        self.colonies.append(colony)
        # self.cost = self.calcCost()

    def replaceColony(self, colony, index):
        old_colony = self.colonies[index]
        self.colonies[index] = colony
        self.cost = self.calcCost()
        return old_colony

    def getColony(self, index):
        return self.colonies[index]

    def deleteColony(self, index):
        del self.colonies[index]
        # self.cost = self.calcCost()
        return self.colonies

    def coloniesCount(self):
        return len(self.colonies)

    def getImperialist(self):
        return self.imperialist

    def getCountries(self):
        countries = [self.imperialist]
        for colony in self.colonies:
            countries.append(colony)

        return countries
