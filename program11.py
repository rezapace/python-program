# Deklarasi suku pertama dan suku kedua
suku1 = 6
suku2 = 9

# Tampilkan suku pertama dan kedua
print(suku1)
print(suku2)

# Perulangan untuk menghitung bilangan fibonacci selanjutnya
for i in range(1, 4):
    # Hitung suku selanjutnya
    suku_selanjutnya = suku1 + suku2

    # Tampilkan suku selanjutnya
    print(suku_selanjutnya)

    # Set suku1 menjadi suku2 dan suku2 menjadi suku selanjutnya
    suku1 = suku2
    suku2 = suku_selanjutnya

# Pertama, kita mendeklarasikan variabel suku1 dan suku2 yang menyimpan suku pertama dan kedua
# dari deret bilangan fibonacci. Kemudian, kita menggunakan perulangan for untuk menghitung dan
# menampilkan suku selanjutnya dari deret bilangan fibonacci,