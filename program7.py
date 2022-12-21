# Fungsi untuk menghitung luas persegi
def hitung_luas_persegi(panjang, lebar):
    return panjang * lebar

# Menggunakan input untuk meminta panjang dan lebar persegi dari pengguna
panjang = float(input("Masukkan panjang persegi: "))
lebar = float(input("Masukkan lebar persegi: "))

# Hitung luas persegi
luas = hitung_luas_persegi(panjang, lebar)

# Tampilkan hasil
print("Luas persegi:", luas)

# Pertama, kita mendeklarasikan fungsi hitung_luas_persegi() yang digunakan untuk menghitung luas
# persegi. Kemudian, kita menggunakan input() untuk meminta panjang dan lebar persegi dari
# pengguna. Setelah itu, kita menggunakan fungsi tersebut untuk menghitung luas persegi, dan
# mencetak hasilnya.

# Perlu diingat bahwa Python menggunakan tanda _ (underscore) untuk menggantikan tanda . (titik)
# pada nama fungsi dan variabel, jadi kita menuliskan hitung_luas_persegi() dan luas_persegi daripada
# hitungLuasPersegi() dan luasPersegi. Juga, Python menggunakan tanda : setelah nama fungsi untuk
# menunjukkan dimulainya blok kode, sehingga kita menuliskan def hitung_luas_persegi(panjang, lebar):
# daripada func hitungLuasPersegi(panjang, lebar float64) float64.