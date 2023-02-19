pojistenci = []


class Pojistenec:
    def __init__(self, jmeno, prijmeni, datum_narozeni, tel_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.datum_narozeni = datum_narozeni
        self.tel_cislo = tel_cislo
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni},{self.datum_narozeni}, {self.tel_cislo},věk {self.vek} let."

    def zobraz_databazi(self):  # metoda pro výpis pojištěnců ze seznamu
        for pojistenec in pojistenci:
            print(pojistenec)

    def pridej_pojistence(self):  # metoda přidá nového pojištěného, zobrazí a ošetří chybná zadání
        import datetime
        pojistenec_jmeno = str(input("Zadejte jméno pojištěného:\n"))
        pojistenec_prijmeni = str(input("Zadejte přijmení pojištěného:\n"))
        pojistenec_datum_narozeni = input("Zadejte datum narození: (dd.mm.rrrr)\n") # zadání data narození a kontrola formátu, výpočet věku
        datum_dnes = datetime.datetime.today()
        while True:
            datum = pojistenec_datum_narozeni
            try:
                datum_narozeni = datetime.datetime.strptime(datum, "%d.%m.%Y")
                break
            except ValueError:
                print("Špatně zadaný formát data narození!\n")
                pojistenec_datum_narozeni = input("Zadejte znovu datum narození: (dd.mm.rrrr)\n")
        d = datum_narozeni
        roky = 0
        while d <= datum_dnes:
            if d.day == datum_narozeni.day and d.month == datum_narozeni.month:
                roky += 1
            d += datetime.timedelta(1)
        roky -= 1
        vek = roky
        pojistenec_tel_cislo = str(input("Zadejte telefonní číslo pojištěného:\n"))
        while len(str(pojistenec_tel_cislo)) != 9:  # kontrola formátu tel.čísla
            print("Špatný formát telefonního čísla!")
            pojistenec_tel_cislo = str(input("Zadejte znovu telefonní číslo:\n"))
        novy_pojistenec = Pojistenec(pojistenec_jmeno, pojistenec_prijmeni, pojistenec_datum_narozeni, pojistenec_tel_cislo, vek)
        pojistenci.append(novy_pojistenec)
        print(novy_pojistenec)

    def vyhledej_pojisteneho(self):  # metoda pro vyhledání pojištěnce v seznamu
        zadane_jmeno = input("Zadejte jméno:\n")
        zadane_prijmeni = input("Zadejte přijmení:\n")
        nalezeni_pojistenci = []
        for pojistenec in pojistenci:
            if pojistenec.jmeno == zadane_jmeno and pojistenec.prijmeni == zadane_prijmeni:
                nalezeni_pojistenci.append(pojistenec)
        return nalezeni_pojistenci

petr = Pojistenec("Petr", "Procházka", "21.6.2000", "792347201", 22)  # naplnění seznamu pojištěnců
josef = Pojistenec("Josef", "Pekař", "2.1.1998","602289741", 25)
renata = Pojistenec("Renata", "Novotná","14.5.1995", "603167212", 27)
magdalena = Pojistenec("Magdaléna", "Tichá","30.6.2001", "608787054", 22)
pojistenci.append(petr)
pojistenci.append(josef)
pojistenci.append(renata)
pojistenci.append(magdalena)