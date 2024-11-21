print("\n----- Celcius Ke Fahrenheit -----")
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print("\n----- Mencari Bilangan Genap -----")
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print("\n----- Keterangan Lulus atau Tidak Lulus -----")
#rata-rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 70:
        print("Lulus")
    else:
        print("Gagal")
skor(80)
skor(60)

print("\n----- Mencetak Bilangan Ganjil -----")
def bilangan_ganjil(ganjil):
    for r in range(1, ganjil+1, 2):
        print(r, end=" ")
bilangan_ganjil(20)