def main():
    print("Selamat datang di layanan konsultasi perawatan kulit!")

    # Registrasi
    nama = input("Masukkan nama Anda: ")
    password = input("Buat kata sandi: ")

    # Memilih jenis kulit (hanya satu)
    print("Masukkan jenis kulit Anda (kering/berminyak/normal/kombinasi/sensitif):")
    jenis_kulit = input("Contoh: kering: ").strip().lower()

    # Daftar masalah wajah dan saran treatment
    masalah_wajah = {
        "berjerawat": {
            "Gentle Exfoliation (GE)": 200000,
            "Salicylic Acid Treatment (SAT)": 350000,
            "Oil Control Facial (OCF)": 300000,
            "Soothing Facial (SF)": 350000,
            "Mikrodermabrasi (M)": 300000
        },
        "normal": {
            "Balancing Facial (BF)": 250000,
            "Gentle Exfoliation (GE)": 200000,
            "Nourishing Treatment (NT)": 300000,
            "Hydrating Facial (HF)": 300000,
            "Vitamin C Infusion (VCI)": 400000
        },
        "kering": {
            "Hydrating Facial (HF)": 300000,
            "Moisturizing Treatment (MT)": 250000,
            "Gentle Hydration (GH)": 400000,
            "Nourishing Treatment (NT)": 300000,
            "Vitamin C Infusion (VCI)": 400000
        }
    }

    # Menentukan masalah wajah yang akan ditangani
    print("Masukkan masalah wajah Anda (berjerawat/normal):")
    masalah = input("Contoh: berjerawat: ").strip().lower()

    treatment_terpilih = []
    biaya_treatment_total = 0

    if masalah in masalah_wajah:
        print(f"\nPilih treatment yang disarankan untuk kulit {jenis_kulit} dengan masalah {masalah}:")
        for treatment, harga in masalah_wajah[masalah].items():
            print(f"{treatment}: Rp {harga}")

        # Menentukan berapa banyak treatment yang ingin dipilih
        jumlah_treatment = int(input("Berapa treatment yang ingin Anda pilih dari yang disarankan? (maksimal 5): "))

        # Memastikan jumlah yang diminta tidak melebihi batas yang tersedia
        if jumlah_treatment > len(masalah_wajah[masalah]):
            print(f"Jumlah yang diminta melebihi batas. Anda hanya dapat memilih maksimal {len(masalah_wajah[masalah])}.")
            return

        for i in range(jumlah_treatment):
            treatment = input(f"Masukkan singkatan treatment yang dipilih (treatment {i + 1}): ").strip().upper()

            # Memeriksa pilihan treatment
            found = False
            for t, harga in masalah_wajah[masalah].items():
                if treatment == t.split(" ")[-1].strip("()"):  # Cek singkatan (yang terakhir di dalam tanda kurung)
                    biaya_treatment_total += harga
                    treatment_terpilih.append(t)
                    print(f"Treatment yang dipilih untuk kulit {jenis_kulit} dengan masalah {masalah}: {t}")
                    found = True
                    break

            if not found:
                print("Treatment tidak ditemukan. Silakan coba lagi.")
                return

    else:
        print(f"Masalah wajah '{masalah}' tidak ditemukan. Silakan coba lagi.")
        return

    # Menanyakan jadwal dokter
    print("\nJadwal dokter tersedia dari Senin hingga Jumat.")
    jadwal = {
        "senin": ["11.00", "16.00", "20.00"],
        "selasa": ["11.00", "16.00", "20.00"],
        "rabu": ["11.00", "16.00", "20.00"],
        "kamis": ["11.00", "16.00", "20.00"],
        "jumat": ["13.00", "17.00", "20.00"],
    }

    # Menampilkan jadwal
    for hari, jam in jadwal.items():
        print(f"{hari}: {', '.join(jam)}")

    # Memilih hari dan jam
    hari_dipilih = input("Pilih hari untuk konsultasi (senin/selasa/rabu/kamis/jumat): ").strip()
    jam_dipilih = input("Pilih jam untuk konsultasi (contoh: 20.00): ").strip()

    # Validasi pilihan jam
    if hari_dipilih in jadwal:
        if jam_dipilih in jadwal[hari_dipilih]:
            print(f"Jadwal konsultasi Anda telah dikonfirmasi pada {hari_dipilih} pukul {jam_dipilih}.")
        else:
            print("Jam yang Anda pilih tidak tersedia. Silakan coba lagi.")
            return
    else:
        print("Hari yang Anda pilih tidak valid. Silakan coba lagi.")
        return

    # Menanyakan apakah perlu treatment tambahan
    treatment_tambahan = input("Apakah Anda perlu treatment tambahan? (ya/tidak): ").lower()

    if treatment_tambahan == "ya":
        print("Treatment tambahan yang tersedia:")
        print("- Treatment Muka Segar (M): Rp 150000")
        print("- Treatment Pembersihan Mendalam (PM): Rp 200000")
        print("- Treatment Anti Aging (AA): Rp 300000")
        print("- Treatment Pencerah Kulit (PK): Rp 250000")
        print("- Treatment Relaksasi Wajah (RW): Rp 200000")

        # Memilih treatment tambahan
        jumlah_treatment_tambahan = int(input("Berapa treatment tambahan yang ingin Anda pilih? (maksimal 5): "))
        
        for i in range(jumlah_treatment_tambahan):
            treatment_lain = input(f"Masukkan singkatan treatment tambahan yang dipilih (treatment tambahan {i + 1}): ").strip().upper()

            # Memeriksa treatment tambahan
            if treatment_lain == "M":
                biaya_treatment_total += 150000
                print("Treatment Muka Segar telah ditambahkan.")
            elif treatment_lain == "PM":
                biaya_treatment_total += 200000
                print("Treatment Pembersihan Mendalam telah ditambahkan.")
            elif treatment_lain == "AA":
                biaya_treatment_total += 300000
                print("Treatment Anti Aging telah ditambahkan.")
            elif treatment_lain == "PK":
                biaya_treatment_total += 250000
                print("Treatment Pencerah Kulit telah ditambahkan.")
            elif treatment_lain == "RW":
                biaya_treatment_total += 200000
                print("Treatment Relaksasi Wajah telah ditambahkan.")
            else:
                print("Treatment tambahan tidak ditemukan.")

    # Menghitung total biaya
    total_biaya = biaya_treatment_total

    print("\nRincian biaya akhir treatment")
    print(f"Total biaya: Rp {total_biaya}")
    print("Terima kasih telah menggunakan layanan kami.")

# Menjalankan program
main()