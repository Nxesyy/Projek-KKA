class Karakter:
    def serang(self):
        pass

class Warrior(Karakter):
    def serang(self):
        print("Menebas dengan pedang! (Physical Damage)")

class Mage(Karakter):
    def serang(self):
        print("Menembakkan bola api! (Magic Damage)")

pasukan = [Warrior(), Mage()]
for prajurit in pasukan:
    prajurit.serang() # Output berbeda meski nama method sama