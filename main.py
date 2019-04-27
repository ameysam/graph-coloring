from ICA import Ica


if __name__ == "__main__":

    ica = Ica()

    ica.createCountries()

    ica.createEmpires()

    ica.absorb()

    for empire in ica.empires:
        print("Empire_{}".format(empire.name), "Total cost: {}".format(empire.cost))
        print(empire.getImperialist().colorFa)
        for colony in empire.getColonies():
            print(colony.colorFa, "Cost: {}".format(colony.cost))
        print()

    print()
    print()



    empire = ica.competition()

    print()
    print("*" * 100)
    print("Winner ==========> Empire_{}" . format(empire.name))
    print(empire.getImperialist().colorFa)
    for colony in empire.getColonies():
        print(colony.colorFa)

