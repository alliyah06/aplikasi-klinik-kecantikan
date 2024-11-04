#Nilai IP Mahasiswa Ali
print ("=================Nilai IP Mahasiswa Ali===============")

print("Nama = Ali")
print("NIM = TI001")

#Data Nilai Ali
NilaiFisika = 80
NilaiBiologi = 80
NilaiMatematika = 85
NilaiKimia = 75
NilaiBahasa = 80
    
def konversi_nilai(nilai):
    if 80 <= nilai <= 100:
        return 'A', 4
    elif 70 <= nilai < 80:
        return 'B', 3
    elif 60 <= nilai < 70:
        return 'C', 2
    elif 50 <= nilai < 60:
        return 'D', 1
    else:
        return 'E', 0
    
#Konversi Nilai Setiap Matkul ke huruf dan bobot
FisikaHuruf, BobotFisika = konversi_nilai(NilaiFisika)
BiologiHuruf, BobotBiologi = konversi_nilai(NilaiBiologi)
MatematikaHuruf, BobotMatematika = konversi_nilai(NilaiMatematika)
KimiaHuruf, BobotKimia = konversi_nilai(NilaiKimia)
BahasaHuruf, BobotBahasa = konversi_nilai(NilaiBahasa)

#Menghitung Nilai IPK Ali
TotalBobot = BobotFisika + BobotBiologi + BobotMatematika + BobotKimia + BobotBahasa
JumlahMatkul = 5
NilaiIPK = TotalBobot / JumlahMatkul

#Output
print(f"Fisika: {NilaiFisika} = {FisikaHuruf}")
print(f"Biologi: {NilaiBiologi} = {BiologiHuruf}")
print(f"Matematika: {NilaiMatematika} = {MatematikaHuruf}")
print(f"kimia: {NilaiKimia} = {KimiaHuruf}")
print(f"Bahasa: {NilaiBahasa} = {BahasaHuruf}")
print(f"IPK = {NilaiIPK}")

print ("=================Selesai===============")