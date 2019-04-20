from constants import Constant

class Empire:
    def __init__(self, imperialist):
        self.imperialist = imperialist
        self.costs = [0, 0, 0, 0, 0]
        self.cost = 0
        self.countries = []
        self.colonies = []



    def calcCost(self):
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


    def getColonies(self):
        return self.colonies


    def addColony(self, colony):
        self.colonies.append(colony)
        # self.cost = self.calcCost()


    def coloniesCount(self):
        return len(self.colonies)


    def getCountries(self):
        countries = [self.imperialist]
        for colony in self.colonies:
            countries.append(colony)

        return countries


