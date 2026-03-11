class Karakter:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

class Warrior(Karakter):
    def __init__(self, nama, hp, armor):
        super().__init__(nama, hp)
        self.armor = armor # Atribut khusus Warrior

class Mage(Karakter):
    def __init__(self, nama, hp, mana):
        super().__init__(nama, hp)
        self.mana = mana # Atribut khusus Mage

ksatria = Warrior("Gatotkaca", 150, 50)
penyihir = Mage("Kadita", 80, 100)
print(f"{ksatria.nama} punya armor {ksatria.armor}, {penyihir.nama} punya mana {penyihir.mana}")