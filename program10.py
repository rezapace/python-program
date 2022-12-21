# Membuat array dengan nama-nama hari
hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

# Perulangan untuk menampilkan nama hari
for i in range(len(hari)):
    print("Hari ke", i + 1, "adalah hari", hari[i])

# Pertama, kita mendeklarasikan array hari yang menyimpan nama-nama hari. Kemudian, kita
# menggunakan perulangan for untuk menampilkan nama hari, dengan menggunakan fungsi range()
# untuk menentukan jumlah iterasi yang diinginkan. Setiap iterasi, kita mencetak nomor hari dan nama
# hari sesuai dengan urutan pada array.

# Perlu diingat bahwa Python menggunakan tanda : setelah perintah for untuk menunjukkan
# dimulainya blok kode, sehingga kita menuliskan for i in range(len(hari)): daripada for i := 0; i <
# len(hari); i++ {. Juga, Python tidak menggunakan tanda := untuk mendeklarasikan variabel, sehingga
# kita menuliskan hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"] daripada hari :=
# []string{"senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"}.