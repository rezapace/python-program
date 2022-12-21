# Membuat segitiga siku-siku dengan bintang

# Deklarasi variabel tinggi
tinggi = int(input("Masukkan tinggi segitiga: "))

# Perulangan untuk membuat segitiga
for i in range(1, tinggi + 1):
    # Perulangan untuk menampilkan bintang
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Pertama, kita mendeklarasikan variabel tinggi yang menyimpan tinggi segitiga yang ingin dibuat.
# Kemudian, kita menggunakan perulangan for untuk menampilkan segitiga siku-siku dengan bintang.
# Setiap iterasi pertama, kita menggunakan perulangan for lain untuk menampilkan bintang sesuai
# dengan tinggi segitiga yang ingin dibuat. Kita menggunakan fungsi end pada perintah print() dengan
# nilai "" untuk menghentikan penggunaan newline (enter) setelah menampilkan bintang, sehingga
# bintang-bintang tersebut ditampilkan pada satu baris.