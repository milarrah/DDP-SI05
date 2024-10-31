#soal 1
data_transportasi = ["nama kendaraan", "jenis kendaraan", "cc kendaraan", "warna kendaraan", "roda kendaraan"]
print(data_transportasi)

data_transportasi.append("harga kendaraan")
print(data_transportasi)

data_transportasi.append("type kendaraan")
print(data_transportasi)

data_transportasi.insert(2, "merk kendaraan")
print(data_transportasi)

#soal 2
pilih = int(input("""selamat datang di aplikasi menghitung
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga 
                  
masukkan pilihan anda: """))

match pilih:
    case 1 :
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukkan sisi persegi: "))
        luas_persegi = sisi*sisi
        print("luas persegi yang sisinya ",sisi,"adalah", luas_persegi)
    case 2 :
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari_jari = int(input("masukkan jari-jari: "))
        luas_lingkaran = 3.14 * jari_jari * jari_jari
        print("luas lingkaran yang jari-jarinya ",jari_jari,"adalah", luas_lingkaran)
    case 3 :
        print("kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("masukkan alas segitiga: "))
        tinggi = int(input("masukkan tinggi segitiga: "))
        luas_segitiga = 0.5 * alas * tinggi
        print("luas segitiga dengan alas ",alas,"dan tinggi",tinggi, "adalah", luas_segitiga)
    case _ :
        print("anda salah pilih")