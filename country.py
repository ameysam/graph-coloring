from constants import Constant
import string
import random


class Country:
    def __init__(self, color):
        self.cost = 0
        self.color = color
        self.name = 'Colony_{}' . format(random.choices(string.ascii_uppercase, k=1))

    # def calcCost(self):
    #     conflicts = Constant.RULE_MATRIX
    #     pass


    def updateCost(self, cost):
        self.cost = cost

    def getCost(self):
        return self.cost
