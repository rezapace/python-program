#  percabangan Golang dengan kondisi if-else
#      - Jika mutu kurang dari sama dengan 40 maka nilai D,
#      - jika mutu kurang dari 61 maka nilai C,
#      - jika nilai kurang dari 81 maka nilai B,
#      - selain itu nilai A.

print("masukkan nilai mutu : " )
mutu = int(input())

if mutu <= 40:
    print("Nilai mutu D")
elif mutu < 61:
    print("Nilai mutu C")
elif mutu < 81:
    print("Nilai mutu B")
else:
    print("Nilai mutu A")

# Program ini menerima masukan berupa nilai mutu dari pengguna, kemudian mengevaluasi nilai
# tersebut dan mengeluarkan output berupa nilai huruf mutu sesuai kriteria yang telah ditentukan.
# Kriteria yang digunakan adalah sebagai berikut:

# Jika nilai mutu kurang dari atau sama dengan 40, maka nilai mutu adalah D.
# Jika nilai mutu lebih dari 40 dan kurang dari 61, maka nilai mutu adalah C.
# Jika nilai mutu lebih dari 61 dan kurang dari 81, maka nilai mutu adalah B.
# Jika nilai mutu lebih dari 81, maka nilai mutu adalah A.
# Program ini menggunakan percabangan if, elif, dan else untuk mengevaluasi nilai mutu dan
# mengeluarkan output sesuai dengan kriteria yang telah ditentukan.