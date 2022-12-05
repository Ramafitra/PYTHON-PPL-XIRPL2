#contoh overloading
#mendefinisikan atau mengfusikan operator sesuai kemauan kita(+)

#membuat class angka
class angka:
    def __init__(self,angka):
        self.angka = angka

    def __add__(self,object):
        return angka (
            self.angka + object.angka
            )


#membuat objek
x1 = angka(10)
x2 = angka(20)
print (x1 + x2)
x3 = x1 + x2
print(x3.angka)        