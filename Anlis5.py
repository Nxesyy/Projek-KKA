from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self):
        pass

class Assassin(GameUnit):
    def serang(self):
        print("Menusuk dari belakang! (Critical Damage)")

# unit = GameUnit() # <-- Ini akan error jika dijalankan (Abstraction berhasil)
ninja = Assassin()
ninja.serang()