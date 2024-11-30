import math

def kubus(sisi) :
    luas = 6 * sisi * sisi
    print(f'Luas Kubus {6} * {sisi} * {sisi} = {luas}')

def bola(jari_jari) :
    luas = 4 * 3.14 * jari_jari
    print(f'Luas Bola {4} * {3.14} * {jari_jari} = {luas}')

def tabung(jari_jari, tinggi) :
    luas = 2 * 3.14 * jari_jari * (tinggi + jari_jari)
    print(f'Luas Tabung {2} * {3.14} * {jari_jari} * {(tinggi+jari_jari)} = {luas}')

def balok(panjang, lebar, tinggi) :
    luas = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
    print(f'Luas Balok {2} * {(panjang*lebar + panjang*tinggi + lebar*tinggi)} = {luas}')

def prisma(luas_alas, keliling_alas, tinggi) :
    luas = (2 * luas_alas) + (keliling_alas * tinggi)
    print(f'Luas Prisma {(2 * luas_alas)} + {(keliling_alas * tinggi)} = {luas}')