#Belajar pewarisan (inheritance)
#3 objek = orang,pelajar,pekerja
# MAsing" mempunyai nama,asal,kemampuan untuk introduce ur self
#Pelajar disekolah,pekerja di kantor

class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print("perkenalkan nama saya", self.nama, "dari", self.asal)

class pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah = sekolah

class pekerja (Orang):
    def __init__(self, nama, asal, kerja):
        Orang.__init__(self, nama, asal)
        self.kerja = kerja

dani = Orang('Dani','Zimbabwe')
dani.perkenalan()

rahma = pelajar('rahma','jawa','SMK JP 1')
rahma.perkenalan()
print("saya bersekolah di", rahma.sekolah,"\n")

arya = pekerja('arya','pakistan','SMK JP 1')
arya.perkenalan()
print("saya bekerja di", arya.kerja,"\n")
