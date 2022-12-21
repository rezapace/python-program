# Menghitung sin, cos, dan tan sudut

import math

sudut = float(input("Masukkan sudut: "))

sin = math.sin(sudut)
cos = math.cos(sudut)
tan = math.tan(sudut)

print("Nilai sin adalah", sin)
print("Nilai cos adalah", cos)
print("Nilai tan adalah", tan)

# Pertama, kita import module math yang akan kita gunakan untuk menghitung nilai sin, cos, dan tan.
# Kita mendeklarasikan variabel sudut yang menyimpan sudut yang ingin dikonversi menjadi nilai sin,
# cos, dan tan. Kita menggunakan fungsi float() untuk mengkonversi inputan dari tipe data string
# menjadi tipe data float. Kemudian, kita menghitung nilai sin, cos, dan tan dari sudut yang diberikan
# dan menyimpannya pada variabel sin, cos, dan tan. Terakhir, kita menampilkan hasil perhitungan
# tersebut menggunakan perintah print().