from animals import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'hewan ikan ini bewarna {self.warna_ikan} dan hewan ini jenisnya ikan {self.jenis_ikan}')

print('-------cetak burung-------')
print('-------objek 1-------')
mas = ikan ('ikan mas', 'krustasea', 'air', 'bertelur', 'jingga', 'air tawar' )
mas.cetak_ikan()

print('-------objek 2-------')
koki = ikan ('ikan koki', 'serangga kecil', 'air', 'bertelur', 'putih dan merah', 'air tawar' )
koki.cetak_ikan()