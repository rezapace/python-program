# Membuat segitiga full dengan bintang

# Deklarasi variabel tinggi
tinggi = int(input("Masukkan tinggi segitiga: "))

# Perulangan untuk membuat segitiga
for brs in range(1, tinggi + 1):
    # Menampilkan spasi sebelum bintang
    for spasi in range(30, brs, -1):
        print(" ", end="")
    # Menampilkan bintang pada bagian kiri segitiga
    for klm in range(1, brs + 1):
        print("*", end="")
    # Menampilkan bintang pada bagian kanan segitiga
    for klm in range(brs - 1, 0, -1):
        print("*", end="")
    print()

# Pertama, kita mendeklarasikan variabel tinggi yang menyimpan tinggi segitiga yang ingin dibuat.
# Kemudian, kita menggunakan perulangan for untuk menampilkan segitiga full dengan bintang. Setiap
# iterasi, kita menggunakan perulangan for lain untuk menampilkan spasi sebelum bintang, bintang
# pada bagian kiri segitiga, dan bintang pada bagian kanan segitiga. Kita menggunakan fungsi end pada
# perintah print() dengan nilai "" untuk menghentikan penggunaan newline (enter) setelah
# menampilkan bintang, sehingga bintang-bintang tersebut ditampilkan pada satu baris.
# Perlu diingat bahwa Python menggunakan tanda : setelah perintah for untuk menunjukkan
# dimulainya blok kode, sehingga kita menuliskan for i in range(1, tinggi + 1): daripada for i := 1; i <=
# tinggi; i++ {. Juga, Python menggunakan tanda = untuk menetapkan nilai pada variabel, sehingga kita
# menuliskan tinggi = int(input("Masukkan tinggi segitiga: ")) daripada var tinggi int; fmt.Scan(&tinggi).