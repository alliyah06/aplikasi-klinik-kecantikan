# membuat database
bunga = ["anggrek dendro", "anggrek bulan", "anggrek layu", "anggrek randy"]

# si Ali membuat program menu
def menu () :
    print ("===========")
    print ("[1] show data bunga")
    print ("[2] insert data bunga baru")

# si Banu membuat program show data 
def show_data() :
    print ("daftar bunga yang ada = ")
    if len (bunga) ==0:
        print ("belum ada daftar bunga")
    else:
        for indeks in range(len(bunga)):
            print ("no =", indeks, " ", bunga[indeks])

# si caca membuat program insert data
def insert_data():
    bunga_baru = (input ("masukan ID bunga yang dihapus : "))
    bunga.append(bunga_baru)
    show_data()

# si danang membuat program hapus data
def hapus_data():
    show_data()
    indeks = int(input("Masukan ID bunga yang dihapus :"))
    if ( indeks > len(bunga)):
        print("id salah")
    else :
        bunga.remove(bunga[indeks])
        show_data()

# program utama (ketua tim)
print ("=====selamat datang sistem informasi bunga=====")
print ("===========")
menu()
pilih = input (" masukan pilihan menu=")
print ("=========")
print ("yang dipilih =", pilih)

if pilih == ("1"):
    show_data()
elif pilih == ("2"):
    insert_data()
elif pilih == ("3"):
    hapus_data ()