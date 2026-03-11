class Karakter:
    def __init__(self, nama, hp):
        self.nama = nama
        self.__hp = hp # Private attribute

    # Getter
    def get_hp(self):
        return self.__hp

    # Setter dengan validasi
    def set_hp(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

hero = Karakter("Arthur", 100)
hero.set_hp(30)
print(f"HP {hero.nama} tersisa: {hero.get_hp()}")