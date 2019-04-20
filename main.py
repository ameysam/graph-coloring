# from constants import Constant
from ICA import Ica
from constants import Constant
import numpy as np

if __name__ == "__main__":

    ica = Ica()

    countries = ica.createCountries()

    # for i in countries:
    #     print(i.color)

    ica.createEmpires()

    print(ica.empires)
    for empire in ica.empires:
        (empire.calcCost())
        print(empire.cost)
    # print(len(ica.colonies))


    print("Here graph coloring...")
