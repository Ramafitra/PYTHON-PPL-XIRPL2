# ada 3 kategori enkapsulasi yaitu : public, protected,private.

class segitiga:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

#buat instansiasinya
# segitiga_besar = segitiga(100,80)

# print(f'alas : {segitiga_besar.alas}')
# print(f'alas : {segitiga_besar.tinggi}')
# print(f'alas : {segitiga_besar.luas}')

#contoh class protacted
# class mobil:
#     def __init__(self,merk):
#         self.__merk = merk

# class mobilefwan(mobil):
#     def __init__(self, merk, total_gear):
#         super().__init__(merk)
#         self.__total_gear =total_gear

#     # Akses _merk dari subclass(kelas turunan)
#     def pamer(Self):
#         print(f'mobil{self.__merk} dengan total gear {self.__total_gear}')

# redbull = mobilefwan('Redbull Racing',8)
# redbull.pamer()

# sedan = mobil('toyota')

# #tampilan merk dari luar kelas
# print (f'merk mobil : {sedan._merk}')
        

#class private
class motor:
    def __init__(self,merk):
        self.__merk = merk
         
    def tampilkan_merk(self):
        print(f'Merk motornya : {self.__merk}')

ducati = motor ('Ducati')
ducati.tampilkan_merk()


