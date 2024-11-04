# Program penyeleksi shuttlecock berdasarkan standar SNI
print("==========Penyeleksi Mutu Shuttlecock Sesuai Standar==========")

# Fungsi untuk mengecek apakah shuttlecock sesuai standar SNI
def cek_shuttlecock(panjang, berat):
    if 62 <= panjang <= 70:
        if 4.74 <= berat <= 5.50: 
            print("Sesuai standar SNI")
        else:
            print("Tidak sesuai standar SNI")
    else:
        print("Tidak sesuai standar SNI")

# Input data shuttlecock
n = int(input("Masukkan jumlah shuttlecock      : "))

# Loop untuk mengecek setiap shuttlecock
for i in range(n):
    print(f"\nShuttlecock {i+1}:")
    panjang = float(input("Masukkan panjang shuttlecock (mm): "))
    berat = float(input("Masukkan berat shuttlecock (gram): "))
    cek_shuttlecock(panjang, berat)

print("==========Proses Seleksi Selesai==========")

