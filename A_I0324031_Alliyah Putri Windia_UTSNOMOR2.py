# Program Klasifikasi Pemasok Pengiriman Produk
print("======Klasifikasi Pemasok Pengiriman Produk======")

# Input jumlah pemasok
n = int(input("Masukkan jumlah pemasok                  : "))
i = 0

# Input bobot penilaian untuk masing-masing kriteria
bobot_kualitas  = 0.4  # 40%
bobot_harga     = 0.3  # 30%
bobot_keandalan = 0.3  # 30%

# Fungsi untuk mengklasifikasikan pemasok
def klasifikasi_pemasok(total_penilaian):
    if total_penilaian <= 1:
        return "Pemasok sangat kurang"
    elif 1.01 <= total_penilaian <= 2:
        return "Pemasok kurang"
    elif 2.01 <= total_penilaian <= 3: 
        return "Pemasok cukup"
    elif 3.01 <= total_penilaian <= 4:
        return "Pemasok baik"
    else: 
        return "Pemasok sangat baik"

# Loop untuk mengevaluasi setiap pemasok
while i <= n:
    print(f"\nEvaluasi pemasok ke-{i+1}")

    # Input skor untuk masing-masing kriteria dalam skala 1-5
    skor_kualitas   = float(input("Masukkan skor kualitas (1-5)             : "))
    skor_harga      = float(input("Masukkan skor harga (1-5)                : "))
    skor_keandalan  = float(input("Masukkan skor keandalan pengiriman (1-5) : "))

    # Perhitungan penilaian berdasarkan bobot
    penilaian_kualitas  = skor_kualitas * bobot_kualitas
    penilaian_harga     = skor_harga * bobot_harga
    penilaian_keandalan = skor_keandalan * bobot_keandalan

    # Menghitung total penilaian
    total_penilaian = penilaian_kualitas + penilaian_harga + penilaian_keandalan

    # Menampilkan hasil penilaian total untuk pemasok saat ini
    print(f"Total Penilaian untuk pemasok ke-{i+1}       : {total_penilaian : .1f}")
    print(f"Klasifikasi Pemasok ke-{i+1}                 : {klasifikasi_pemasok(total_penilaian)}")


    # Increment i untuk pemasok berikutnya
    i += 1

    print("======Proses Klasifikasi Selesai======")
