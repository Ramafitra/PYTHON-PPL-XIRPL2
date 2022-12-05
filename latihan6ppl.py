#kelas induk = kendaraan , kelas turunan = mobil
#kendaraan mempunyai sifat berjalan(),mobil mempunyai sifat berjalan() tapi lebih spesifik

class kendaraan:
    def berjalan(Self):
        print('berjalan')

class mobil(kendaraan):
    def berjalan(Self, kecepatan, satuan ='km/j'):
        print('Berjalan lebih ngebut {kecepatan} {satuan}')

#instansiasi(memanggil fungsi dan kelas)
sepeda = kendaraan()
sedan = mobil()

sepeda.berjalan()
sedan.berjalan(200)