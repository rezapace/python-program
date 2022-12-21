# Kalkulator sederhana

# Pendeklarasian variabel
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

# Proses perhitungan
tambah = angka1 + angka2
kurang = angka1 - angka2
kali = angka1 * angka2
bagi = angka1 / angka2

# Output hasil
print(angka1, "+", angka2, " = ", tambah)
print(angka1, "-", angka2, " = ", kurang)
print(angka1, "*", angka2, " = ", kali)
print(angka1, "/", angka2, " = ", bagi)

# Pertama, kita mendeklarasikan variabel angka1 dan angka2 yang menyimpan angka-angka yang akan
# dioperasikan. Kemudian, kita melakukan perhitungan matematika dasar pada angka-angka tersebut
# dan menyimpan hasilnya pada variabel tambah, kurang, kali, dan bagi. Terakhir, kita menampilkan
# hasil perhitungan tersebut menggunakan perintah print().
# Perlu diingat bahwa Python menggunakan tanda : setelah perintah for untuk menunjukkan
# dimulainya blok kode, sehingga kita menuliskan for i in range(1, tinggi + 1): daripada for i := 1; i <=
# tinggi; i++ {. Juga, Python menggunakan tanda = untuk menetapkan nilai pada variabel, sehingga kita
# menuliskan `angka1 = int