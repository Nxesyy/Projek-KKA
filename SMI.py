from abc import ABC, abstractmethod

# 1. ABSTRACTION: Class Induk tidak bisa di-init langsung
class Produk(ABC):
    def __init__(self, kategori, merk, harga_dasar, stok):
        self.kategori = kategori
        self.merk = merk
        self.harga_dasar = harga_dasar
        # 2. ENCAPSULATION: Stok di-private
        self.__stok = stok 

    # Setter Stok dengan Validasi
    def update_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.merk}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.merk}: {self.__stok} unit.")

    # Getter Stok
    def get_stok(self):
        return self.__stok

    # Method abstrak yang wajib di-override
    @abstractmethod
    def hitung_pajak(self):
        pass

# 3. INHERITANCE: Laptop mewarisi Produk
class Laptop(Produk):
    def __init__(self, merk, harga_dasar, stok, prosesor):
        super().__init__("LAPTOP", merk, harga_dasar, stok)
        self.prosesor = prosesor

    # 4. POLYMORPHISM: Pajak Laptop 10%
    def hitung_pajak(self):
        return self.harga_dasar * 0.10

# 3. INHERITANCE: Smartphone mewarisi Produk
class Smartphone(Produk):
    def __init__(self, merk, harga_dasar, stok, kamera):
        super().__init__("SMARTPHONE", merk, harga_dasar, stok)
        self.kamera = kamera

    # 4. POLYMORPHISM: Pajak Smartphone 5%
    def hitung_pajak(self):
        return self.harga_dasar * 0.05

# --- SKENARIO PROGRAM ---
print("--- SISTEM MANAJEMEN INVENTARIS TECHMASTER ---\n")

# Inisialisasi Produk
laptop1 = Laptop("ROG Zephyrus", 20000000, 10, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15000000, 0, "12MP")

# Tes Encapsulation (Validasi Stok)
hp1.update_stok(-5)
hp1.update_stok(20)
print()

# Proses Transaksi
beli_laptop = 2
beli_hp = 1

pajak_laptop = laptop1.hitung_pajak()
subtotal_laptop = (laptop1.harga_dasar + pajak_laptop) * beli_laptop

pajak_hp = hp1.hitung_pajak()
subtotal_hp = (hp1.harga_dasar + pajak_hp) * beli_hp

total_tagihan = subtotal_laptop + subtotal_hp

# Output Struk Transaksi sesuai Modul
print("STRUK TRANSAKSI ---")
print(f"\n1. [{laptop1.kategori}] {laptop1.merk} | Proc: {laptop1.prosesor}")
print(f"   Harga Dasar: Rp {laptop1.harga_dasar:,} | Pajak (10%): Rp {int(pajak_laptop):,}")
print(f"   Beli: {beli_laptop} unit | Subtotal: Rp {int(subtotal_laptop):,}")

print(f"\n2. [{hp1.kategori}] {hp1.merk} | Cam: {hp1.kamera}")
print(f"   Harga Dasar: Rp {hp1.harga_dasar:,} | Pajak (5%): Rp {int(pajak_hp):,}")
print(f"   Beli: {beli_hp} unit | Subtotal: Rp {int(subtotal_hp):,}")

print(f"\nTOTAL TAGIHAN: Rp {int(total_tagihan):,}")
