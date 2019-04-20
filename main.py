from ICA import Ica
# from constants import Constant
# import numpy as np

if __name__ == "__main__":

    ica = Ica()

    ica.createCountries()

    ica.createEmpires()

    ica.absorb()

    for empire in ica.empires:
        print(empire.name, empire.cost)
        print(empire.getImperialist().color)
        for colony in empire.getColonies():
            print(colony.color, colony.cost)



    empire = ica.competition()
    print()
    print("Result {}" . format(empire.name))
    print(empire.getImperialist().color)
    for colony in empire.getColonies():
        print(colony.color)
    #
    # print(ica.iteration)


    # print("Here graph coloring...")
