print("======kelas A==========")
#deklarasikan variabel / input

stok        = int(input("mauskan stok awal barang = "))
demand      = int(input( "masukan permintaan harian = "))
PO          = int(input("masukan pemesanan kembali = "))
jumlahHari  = int(input("jumlah hari pengamatan = "))

print("hari   :   stok    :    demand     :    Pemesanankembali")
print("=======================")

print("0", "    ", stok, "        ", demand)


#proses looping 

for j in range (1,jumlahHari) :
    if (stok>=30) :
        stok=stok-demand
    print(j, "        ", stok, "        ", deman,d)
else:
    stok =stok + PO 
    print (j, "      ", stok, "      ", demand,"      ", PO)
print("=======================")




