# Menggunakan input untuk meminta nilai dari pengguna
nilai = int(input("Masukkan nilai Anda: "))

# Cek apakah nilai lebih besar atau sama dengan 50
if nilai >= 50:
    print("Nilai Anda:", nilai)
else:
    print("Maaf, Anda tidak lulus")

# Pertama, kita menggunakan input() untuk meminta nilai dari pengguna. Kemudian, kita menggunakan
# pernyataan if untuk mengecek apakah nilai lebih besar atau sama dengan 50. Jika ya, maka kita akan
# mencetak nilai pengguna. Jika tidak, kita akan mencetak pesan "Maaf, Anda tidak lulus".

# Perlu diingat bahwa Python tidak memerlukan penggunaan var untuk menyatakan variabel, jadi kita
# hanya perlu menuliskan nilai = int(input(...)) untuk mendeklarasikan variabel nilai dan menetapkan
# nilainya sesuai dengan input pengguna.