class Menu:
    def uvodnik(self):
        return f"-------------------------\nEvidence pojištěných osob\n-------------------------\n"

    def menu(self):
        return f"Vybrat akci:\n1 - Přidat nového pojištěného\n2 - Vypsat všechny pojištěné\n3 - Vyhledat " \
               f"pojištěného\n4 - Konec"

    def vycisti_obrazovku(self):  # vyčištění přebytečného textu z konzole
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])