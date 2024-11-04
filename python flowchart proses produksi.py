print ("===============")
jumlahMesin=int(input("jumlah mesin = "))
jumlahHari = int(input("jumlah hari = "))
kapasitasMesin = float(input("kapasitas mesin (unit/(jam_mesin)) = "))

#peoses perhitungan 

jumlahUnit= kapasitasMesin*jumlahHari*jumlahMesin

print ("===============")
print ("jumlah unit yang diproduksi", jumlahUnit, "unit")