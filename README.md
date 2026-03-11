### 👻 1. Abstraksi
*Fokus pada apa yang dilakukan objek, bukan bagaimana cara melakukannya.*
* **Penerapan:** Kelas `Produk` diatur sebagai kelas abstrak (menggunakan modul `abc`) yang memiliki *abstract method* `hitung_pajak()`.
* **Dampak:** Kita tidak bisa membuat objek langsung dari `Produk`. Kelas ini bertindak sebagai "kontrak" wajib bahwa setiap barang di inventaris (seperti Laptop atau Smartphone) **harus** memiliki cara untuk menghitung pajaknya sendiri.

### 🛡️ 2. Enkapsulasi
*Melindungi data sensitif dari modifikasi sembarangan dari luar.*
* **Penerapan:** Atribut stok diubah menjadi *private* (`__stok`).
* **Dampak:** Stok barang tidak bisa dimanipulasi secara langsung (misal: diubah jadi minus oleh *bug* atau *user*). Perubahan stok wajib melewati "pintu resmi" yaitu *method* `update_stok()` yang sudah dilengkapi dengan logika **validasi** (menolak nilai negatif).

### 🧬 3. Pewarisan
*Menghindari penulisan kode berulang dengan mewariskan sifat kelas induk.*
* **Penerapan:** Kelas `Laptop` dan `Smartphone` adalah "anak" dari kelas `Produk`.
* **Dampak:** Kode menjadi sangat efisien (*DRY - Don't Repeat Yourself*). Kelas anak otomatis mewarisi atribut dasar seperti `kategori`, `merk`, dan `harga_dasar`, sekaligus bisa memiliki keunikannya sendiri (Laptop punya `prosesor`, Smartphone punya `kamera`).

### 🎭 4. Polimorfisme
*Satu antarmuka, banyak bentuk implementasi.*
* **Penerapan:** *Method* `hitung_pajak()` diimplementasikan secara berbeda pada masing-masing kelas turunan.
* **Dampak:** Saat sistem menghitung total tagihan, sistem cukup memanggil perintah `hitung_pajak()`. Secara otomatis, Laptop akan dikenakan pajak 10%, dan Smartphone dikenakan pajak 5% sesuai dengan wujud objeknya.

---

## 💻 Hasil Simulasi & Output Program

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
