
# data masukan perusahaan manufaktur
order = int(input("berapa orderannya ? "))
waktu = int(input("berapa waktu yang tersedia ? "))
mesin = int(input("berapa jumlah mesin yg dipunya ? "))

#rumus untuk menghitung
waktu_produksi = waktu/order
leadtime = waktu_produksi*(order/mesin)

#kondisi
if leadtime<waktu:
    print("produksi dapat diselesaikan dalam waktu yang tersedia. Lakukan Penjadwalan dengan standar produks")
elif leadtime==waktu:
    print("produksi terpakai secara optimal. Lakukan penjadwalan dengan standar produksi")
elif leadtime>waktu:
    print("Waktu produksi tidak mencukupi. Pertimbangkan untuk menambah jam kerja, menambah mesin, atau mempercepat proses produksi")

print("=============selesai!!!============")