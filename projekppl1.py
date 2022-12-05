from functools import total_ordering


def garis():
      print("------------------")
print("----JDOORS(layanan hotel berjedorjedor)--")
print("------silahkan pilih tipe kamar----------")
print("------1--Reguler--Rp.150.000/malam-------")
print("------2--VIP------Rp.300.000/malam-------")
print("------3--VVIP-----Rp.600.000/malam-------")
print("------4--Kingdom--Rp.1.200.000/malam-----")
print("---PROMO! NGINEP SEMINGGU GRATIS SEHARI--")

    #Input dari costumer
garis()
tipe =int(input("silahkan pilih tipe : "))
inap =int(input("Berapa malam menginap:"))
cust =input("masukkan nama anda:")

    #kalkulasi tipe kamr
if tipe == 1:
    tipe_kamar =("Reguler")
elif tipe == 2: 
    tipe_kamar =("VIP")
elif tipe == 3:
    tipe_kamar =("VVIP")
elif tipe == 4: 
    tipe_kamar =("Kingdom")
else:
    tipe_kamar = ("yang bener??")

#kalkulasi tipe reguler
if tipe == 1:
    total_harga =inap*150000
#kalkulasi tipe VIP
if tipe == 2:
    total_harga =inap*300000
#kalkulasi tipe VIIP
if tipe == 3:
    total_harga =inap*600000
    #kalkulasi tipe Kingdom
if tipe == 4:
    total_harga =inap*1200000

#Outputnya

garis()
print("Terima kasih", cust ,"atas menggunakan layanan kami")
print("Tipe yang anda pilih :", tipe)
print("Total Harga : RP", total_harga)

#Bonus Inap
if inap >= 7:
    print("SELAMAT ANDA MENDAPATKAN BONUS 1 HARI")
    print("Terima kasih telah menginap di Hotel JDoors!")
    total_inap = inap+1
elif inap < 7:
    print("Terima kasih telah menginap di Hotel JDoors!")
    total_inap = inap
print("Total Lama Menginap : ", total_inap, "Hari")