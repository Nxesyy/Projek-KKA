class Hero:
    def __init__(self, nama, hp):
        self.nama = nama
        self.__hp = hp

    def terima_damage(self, damage):
        self.__hp -= damage
        if self.__hp <= 0:
            self.__hp = 0
            print(f"{self.nama} telah gugur!")
        else:
            print(f"{self.nama} menerima {damage} damage. Sisa HP: {self.__hp}")

    def is_alive(self):
        return self.__hp > 0

player = Hero("Lancelot", 100)
boss_damage = 40

print("--- PERTARUNGAN DIMULAI ---")
while player.is_alive():
    print("Boss menyerang!")
    player.terima_damage(boss_damage)
print("--- PERTARUNGAN SELESAI ---")