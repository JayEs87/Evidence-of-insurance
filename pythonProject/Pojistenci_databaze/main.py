from pojistenci import Pojistenec  # import tříd Pojistenec, Menu
from menu import Menu
menu = Menu()
pokracovat = True

while pokracovat:  # cyklus pro vypsání aplikace
    print(menu.uvodnik())
    print(menu.menu())
    volba = int(input("Zadejte číslo požadované akce:\n"))

    if volba == 1:  # přidá nového pojištěnce
        Pojistenec.pridej_pojistence(Pojistenec)
        input("Data byla uložena. Pokračujte libovolnou klávesou...")
        menu.vycisti_obrazovku()  # vyčistí obrazovku

    elif volba == 2:  # vypíše pojištěné
        Pojistenec.zobraz_databazi(Pojistenec)  # vypíše všechny pojištěné ze seznamu

        input("Pro pokračování stiskněte libovolnou klávesu...")
        menu.vycisti_obrazovku()

    elif volba == 3:  # vyhledá pojištěného
        vyhledani = Pojistenec.vyhledej_pojisteneho(Pojistenec)
        if len(vyhledani) > 0:  # vypíše vyhledávaného
            for pojistenec in vyhledani:
                print(pojistenec)
        else:
            print("Osoba se nenachází v evidenci pojištěných osob.")
        input("Pro pokračování stiskněte libovolnou klávesu...")
        menu.vycisti_obrazovku()

    elif volba == 4:  # ukončení aplikace
        print("Děkujeme za použití naší aplikace.")
        pokracovat = False

    else:  # pokud je neplatná volba
        print("Neplatná volba, zadejte číslo od 1 do 4.")
        print(menu.uvodnik, menu.menu)
        volba = int(input("Zadejte číslo požadované akce: "))