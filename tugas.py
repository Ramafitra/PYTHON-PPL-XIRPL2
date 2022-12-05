from functools import total_ordering


def garis():
      print("------------------")
print("---------Jualan hp----------")
print("------silahkan pilih HP----------")
print("------1--Samsung S22 Ultra++--Rp.15.000.000/unit--")
print("------2--Iphone 14------Rp.30.000.000/unit--------")
print("------3--Poco x4pro++-----Rp.5.000.000/unit-------")
print("------4--Redmi note 10--Rp2.200.000/unit----------")
print("------PROMO!BELI IPHONE DAPET AKU----------")
print("----------------Warna--------------")
print("----------------1.item--------------")
print("----------------2.biru--------------")
print("----------------3.kuning--------------")
print("----------------4.putih--------------")

    #Input dari costumer
tipe =int(input("silahkan pilih tipe : "))
unit =int(input("Beli berape : "))
warna =int(input("Warna apa kak :"))
cust =input("masukkan nama anda:")

    #kalkulasi tipe kamr
if tipe == "item" :
    bang =("item")
elif tipe == "biru": 
    bang =("biru")
elif tipe == "kuning":
    bang =("kuning")
elif tipe == "putih": 
    bang =("putih")
else:
    bang = ("yang bener??")

#kalkulasi tipe reguler
if tipe == 1:
    total_harga =unit*15000000
#kalkulasi tipe VIP
if tipe == 2:
    total_harga =unit*30000000
#kalkulasi tipe VIIP
if tipe == 3:
    total_harga =unit*5000000
    #kalkulasi tipe Kingdom
if tipe == 4:
    total_harga =unit*2200000

#Outputnya

garis()
print("Terima kasih", cust ,"atas menggunakan layanan kami")
print("Warna yang anda pilih :", warna)
print("Hp yang anda pilih :", tipe)
print("Total Harga : RP", total_harga)
