from constants import Constant

class Country:
    def __init__(self, color):
        self.cost = 0
        self.color = color

    def calcCost(self):
        conflicts = Constant.RULE_MATRIX
        pass


    def updateCost(self, cost):
        self.cost = cost
