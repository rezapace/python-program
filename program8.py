# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(r):
    pi = 3.14
    return pi * r * r

# Deklarasi variabel jari-jari
r = 7

# Hitung luas lingkaran
luas = hitung_luas_lingkaran(r)

# Tampilkan hasil
print("Luas lingkaran:", luas)

# Pertama, kita mendeklarasikan fungsi hitung_luas_lingkaran() yang digunakan untuk menghitung luas
# lingkaran. Kemudian, kita mendeklarasikan variabel r yang menyimpan jari-jari lingkaran. Setelah itu,
# kita menggunakan fungsi tersebut untuk menghitung luas lingkaran, dan mencetak hasilnya.

# Perlu diingat bahwa Python menggunakan tanda _ (underscore) untuk menggantikan tanda . (titik)
# pada nama fungsi dan variabel, jadi kita menuliskan hitung_luas_lingkaran() dan luas_lingkaran
# daripada hitungLuasLingkaran() dan luasLingkaran. Juga, Python menggunakan tanda : setelah nama
# fungsi untuk menunjukkan dimulainya blok kode, sehingga kita menuliskan def
# hitung_luas_lingkaran(r): daripada func hitungLuasLingkaran(r float64) float64.