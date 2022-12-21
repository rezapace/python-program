# Menghitung 1-1 juta dan menghitung berapa lama waktu yang dibutuhkan dalam satuan second

import time

start = time.time()
for i in range(1, 1000001):
    pass
end = time.time()
elapsed = end - start
print("Waktu yang dibutuhkan adalah", elapsed)

# Pertama, kita mengimport modul time untuk mengukur waktu yang dibutuhkan untuk menghitung 1
# hingga 1 juta. Kita menyimpan waktu saat program dimulai dalam variabel start dengan menggunakan
# fungsi time.time(). Kemudian, kita melakukan perulangan dari 1 hingga 1 juta menggunakan
# pernyataan for dan perintah pass untuk menghentikan perulangan tanpa melakukan apa pun. Setelah
# perulangan selesai, kita menyimpan waktu saat program selesai dalam variabel end dengan
# menggunakan fungsi time.time() kembali. Kemudian, kita menghitung selisih waktu antara waktu
# selesai dan waktu mulai dan menyimpannya dalam variabel elapsed dengan menggunakan operator
# pengurangan. Terakhir, kita menampilkan waktu yang dibutuhkan untuk menghitung 1 hingga 1 juta
# menggunakan perintah print().