# Perulangan untuk mengecek setiap bilangan dari 1-100
for i in range(1, 101):
    # Cek apakah bilangan tersebut ganjil
    if i % 2 != 0:
        print(i)

# Pertama, kita menggunakan perulangan for untuk mengecek setiap bilangan dari 1 hingga 100.
# Kemudian, kita menggunakan pernyataan if untuk mengecek apakah bilangan tersebut ganjil. Jika ya,
# maka kita akan mencetak bilangan tersebut.

# Perlu diingat bahwa Python tidak memerlukan penggunaan : setelah kondisi perulangan, jadi kita
# hanya perlu menuliskan for i in range(1, 101) untuk mendeklarasikan perulangan. Juga, Python
# menggunakan operator modulo % untuk mengecek sisa bagi, sehingga kita menuliskan i % 2 != 0
# untuk mengecek apakah bilangan tersebut ganjil.