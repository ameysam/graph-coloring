from ICA import Ica


if __name__ == "__main__":

    ica = Ica()

    ica.createCountries()

    ica.createEmpires()

    ica.absorb()

    for empire in ica.empires:
        print(empire.name, empire.cost)
        print(empire.getImperialist().colorFa)
        for colony in empire.getColonies():
            print(colony.colorFa, colony.cost)

    print()



    empire = ica.competition()

    print()
    print("Result {}" . format(empire.name))
    print(empire.getImperialist().colorFa)
    for colony in empire.getColonies():
        print(colony.colorFa)


    print("Here graph coloring...")
