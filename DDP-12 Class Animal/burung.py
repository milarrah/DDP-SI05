from animals import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'Hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

print('-------cetak burung-------')
print('-------objek 1-------')
beo = burung('Burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue dan orange', 'haloo')
beo.cetak_burung()

print('-------objek 2-------')
dara = burung('Burung Dara', 'sayuran hijau', 'uadara', 'bertelur', 'grey', 'huhuhu' )
dara.cetak_burung()