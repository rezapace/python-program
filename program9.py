# Perulangan untuk mengecek setiap bilangan dari 1-75
for i in range(1, 76):
    # Cek apakah bilangan tersebut genap
    if i % 2 == 0:
        print(i)

# Pertama, kita menggunakan perulangan for untuk mengecek setiap bilangan dari 1 sampai 75, dengan
# menggunakan fungsi range(1, 76). Kemudian, kita menggunakan kondisional if untuk mengecek
# apakah bilangan tersebut merupakan bilangan genap, dengan menggunakan operator modulus %
# untuk menghitung sisa pembagian bilangan tersebut dengan 2. Jika bilangan tersebut merupakan
# bilangan genap, maka kita mencetak bilangan tersebut.

# Perlu diingat bahwa Python tidak menggunakan tanda : setelah perintah for dan if, sehingga kita
# menuliskan for i in range(1, 76): dan if i % 2 == 0: daripada for i := 1; i <= 75; i++ { dan if i%2 == 0 {.
# Juga, Python menggunakan tanda : setelah nama fungsi untuk menunjukkan dimulainya blok kode,
# sehingga kita menuliskan def hitung_luas_lingkaran(r): daripada func hitungLuasLingkaran(r float64)
# float64.