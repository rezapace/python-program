# Fungsi untuk menghitung luas segitiga
def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2

# Menggunakan input untuk meminta alas dan tinggi segitiga dari pengguna
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Hitung luas segitiga
luas = hitung_luas_segitiga(alas, tinggi)

# Tampilkan hasil
print("Luas segitiga:", luas)

# Pertama, kita mendeklarasikan fungsi hitung_luas_segitiga() yang digunakan untuk menghitung luas
# segitiga. Kemudian, kita menggunakan input() untuk meminta alas dan tinggi segitiga dari pengguna.
# Setelah itu, kita menggunakan fungsi tersebut untuk menghitung luas segitiga, dan mencetak hasilnya.

# Perlu diingat bahwa Python menggunakan tanda _ (underscore) untuk menggantikan tanda . (titik)
# pada nama fungsi dan variabel, jadi kita menuliskan hitung_luas_segitiga() dan luas_segitiga daripada
# hitungLuasSegitiga() dan luasSegitiga. Juga, Python menggunakan tanda : setelah nama fungsi untuk
# menunjukkan dimulainya blok kode, sehingga kita menuliskan def hitung_luas_segitiga(alas, tinggi):
# daripada func hitungLuasSegitiga(alas, tinggi float64) float64.