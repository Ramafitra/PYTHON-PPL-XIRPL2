buku = []

# fungsi untuk menampilkan menu
def show_menu():
    print("---MENU---")
    print("1. Show buku")
    print("2. Insert buku")
    print("3. Edit buku")
    print("4. Delete buku")
    print("5. Exit")

    menu = int(input("Pilih menu :")) 
    print("\n")  

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print("ente salah pilih")

# fungsi untuk meng-insert buku
def insert_buku():
    buku_baru = input("masukan judul :")
    buku.append(buku_baru)

# fungsi untuk menampilkan isi buku
def show_buku():
    if len(buku)<= 0:
        print ("Belum ada data")
    else:
        for indeks in range(len(buku)):
            print("[{}] {}".format(indeks,buku[indeks]))

# fungsi untuk mengahapus buku
def delete_buku():
    show_buku()
    indeks = int(input("Inputkan id buku:"))
    if indeks > len (buku):
        print ("Id salah")
    else:
        buku.remove(buku[indeks])

if __name__ == "__main__":
    while True:
        show_menu()