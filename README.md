## 🧠 Analisis Praktikum

### 1. Dasar Class & Object
Membangun cetak biru (`class Karakter`) yang memiliki atribut `nama`, `hp`, dan `attack_power`. Objek nyata (seperti `hero1` dan `hero2`) diinstansiasi dari kelas ini untuk menyimpan data yang berbeda-beda.

### 2. Encapsulation (Enkapsulasi)
Mengamankan data sensitif agar tidak bisa diubah sembarangan dari luar. Atribut HP dijadikan *private* (`__hp`). Perubahan nilai HP wajib melalui *setter* (`set_hp()`) yang sudah dilengkapi dengan validasi agar HP tidak menjadi negatif.

### 3. Inheritance (Pewarisan)
Mencegah penulisan kode berulang dengan mewariskan sifat kelas induk. Kelas `Warrior` dan `Mage` mewarisi atribut dasar dari kelas `Karakter`, namun bisa menambahkan atribut unik mereka sendiri (seperti `armor` untuk Warrior dan `mana` untuk Mage).

### 4. Polymorphism (Polimorfisme)
Menerapkan perilaku yang berbeda pada antarmuka yang sama. *Method* `serang()` dipanggil pada *looping* pasukan, namun menghasilkan *output* yang berbeda tergantung tipe prajuritnya (pedang untuk Warrior, bola api untuk Mage).

### 5. Abstraction (Abstraksi)
Membuat kerangka standar menggunakan modul `ABC`. Kelas `GameUnit` dijadikan *abstract class* sehingga tidak bisa diinisialisasi secara langsung. Kelas turunannya (seperti `Assassin`) *wajib* melakukan *override* pada *method* `serang()`.

### 6. Simulasi Pertarungan
Menggabungkan konsep OOP ke dalam sebuah simulasi sederhana menggunakan *looping* `while`. Objek menerima *damage*, HP berkurang melalui *method* internal, dan program otomatis berhenti ketika pengecekan `is_alive()` bernilai *False*.

---

## 💻 Hasil Output Program

*(Tambahkan screenshot output terminal kamu di bawah ini untuk hasil yang lebih maksimal)*
`![Screenshot Output Praktikum](link_gambar_kamu_di_sini.png)`

**Log Output Teks:**

Karakter: Arthur | HP: 500 | Power: 20
Karakter: Lancelot | HP: 80 | Power: 25
500
HP Arthur tersisa: 70
Gatotkaca punya armor 50, Kadita punya mana 100
Menebas dengan pedang! (Physical Damage)
Menembakkan bola api! (Magic Damage)
Menusuk dari belakang! (Critical Damage)

--- PERTARUNGAN DIMULAI ---
Boss menyerang!
Lancelot menerima 40 damage. Sisa HP: 60
Boss menyerang!
Lancelot menerima 40 damage. Sisa HP: 20
Boss menyerang!
Lancelot telah gugur!
--- PERTARUNGAN SELESAI ---


### 1. Abstraksi
*Fokus pada apa yang dilakukan objek, bukan bagaimana cara melakukannya.*
* **Penerapan:** Kelas `Produk` diatur sebagai kelas abstrak (menggunakan modul `abc`) yang memiliki *abstract method* `hitung_pajak()`.
* **Dampak:** Kita tidak bisa membuat objek langsung dari `Produk`. Kelas ini bertindak sebagai "kontrak" wajib bahwa setiap barang di inventaris (seperti Laptop atau Smartphone) **harus** memiliki cara untuk menghitung pajaknya sendiri.

### 2. Enkapsulasi
*Melindungi data sensitif dari modifikasi sembarangan dari luar.*
* **Penerapan:** Atribut stok diubah menjadi *private* (`__stok`).
* **Dampak:** Stok barang tidak bisa dimanipulasi secara langsung (misal: diubah jadi minus oleh *bug* atau *user*). Perubahan stok wajib melewati "pintu resmi" yaitu *method* `update_stok()` yang sudah dilengkapi dengan logika **validasi** (menolak nilai negatif).

### 3. Pewarisan
*Menghindari penulisan kode berulang dengan mewariskan sifat kelas induk.*
* **Penerapan:** Kelas `Laptop` dan `Smartphone` adalah "anak" dari kelas `Produk`.
* **Dampak:** Kode menjadi sangat efisien (*DRY - Don't Repeat Yourself*). Kelas anak otomatis mewarisi atribut dasar seperti `kategori`, `merk`, dan `harga_dasar`, sekaligus bisa memiliki keunikannya sendiri (Laptop punya `prosesor`, Smartphone punya `kamera`).

### 4. Polimorfisme
*Satu antarmuka, banyak bentuk implementasi.*
* **Penerapan:** *Method* `hitung_pajak()` diimplementasikan secara berbeda pada masing-masing kelas turunan.
* **Dampak:** Saat sistem menghitung total tagihan, sistem cukup memanggil perintah `hitung_pajak()`. Secara otomatis, Laptop akan dikenakan pajak 10%, dan Smartphone dikenakan pajak 5% sesuai dengan wujud objeknya.

---

## Hasil Simulasi & Output Program

Saat dijalankan, program akan melakukan simulasi mulai dari validasi stok hingga pencetakan struk transaksi otomatis. 

> 💡 *Tip: Lihat bagaimana program dengan cerdas menolak input stok negatif di baris pertama output!*


--- SISTEM MANAJEMEN INVENTARIS TECHMASTER ---

Gagal update stok iPhone 13! Stok tidak boleh negatif (-5).
Berhasil menambahkan stok iPhone 13: 20 unit.

STRUK TRANSAKSI ---

1. [LAPTOP] ROG Zephyrus | Proc: Ryzen 9
   Harga Dasar: Rp 20,000,000 | Pajak (10%): Rp 2,000,000
   Beli: 2 unit | Subtotal: Rp 44,000,000

2. [SMARTPHONE] iPhone 13 | Cam: 12MP
   Harga Dasar: Rp 15,000,000 | Pajak (5%): Rp 750,000
   Beli: 1 unit | Subtotal: Rp 15,750,000

TOTAL TAGIHAN: Rp 59,750,000
