class Karakter:
    def __init__(self, nama, hp, attack_power):
        self.nama = nama
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Karakter: {self.nama} | HP: {self.hp} | Power: {self.attack_power}")

# Membuat objek
hero1 = Karakter("Arthur", 500, 20)
hero2 = Karakter("Lancelot", 80, 25)

hero1.info()
hero2.info()

print(hero1.hp)