from animals import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, cara_menyerang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ular = warna_ular
        self.cara_menyerang = cara_menyerang

    def cetak_ikan(self):
        super().cetak()
        print(f'hewan ular ini bewarna {self.warna_ular} dan hewan ini menyerang dengan cara {self.cara_menyerang}')

print('-------cetak ular-------')
print('-------objek 1-------')
sanca = ular ('ular sanca', 'mamalia kecil', 'darat', 'bertelur', 'hijau', 'melilit' )
sanca.cetak_ikan()

print('-------objek 2-------')
aniliidae = ular ('ular pipa/aniliidae', 'ular kecil', 'darat', 'bertelur', 'belang-belang hitam merah', 'melingkar/melilit' )
aniliidae.cetak_ikan()