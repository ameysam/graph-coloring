from country import Country
from empire import Empire
from constants import Constant
import numpy as np


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
            if empire.coloniesCount() < 4:
                empire.addColony(colony)
                i += 1


        return self.empires


    def absorb(self):
        pass