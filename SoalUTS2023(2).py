print("==================IPK Mahasiswa=======================") 
#membuat database 
mahasiswa = [ 
    {"nim": "Ti001", "nama": "Ali", "fisika": 80, "biologi": 80, "matematika": 85}, 
    {"nim": "Ti002", "nama": "Budi", "fisika": 70, "biologi": 60, "matematika": 70}, 
    {"nim": "Ti003", "nama": "Caca", "fisika": 75, "biologi": 80, "matematika": 75}, 
    {"nim": "Ti004", "nama": "Dodo", "fisika": 85, "biologi": 70, "matematika": 80}, 
    {"nim": "Ti005", "nama": "Eko", "fisika": 90, "biologi": 60, "matematika": 80}] 
 
 
#konversi nilai ke huruf dan skala 
def konversi_nilai(nilai): 
    if 80 <= nilai <=100: 
        return 'A', 4 
    elif 70 <= nilai <=79.9: 
        return 'B', 3 
    elif 60 <= nilai <=69.9: 
        return 'C', 2 
    elif 50 <= nilai <=59.9: 
        return 'D', 1 
    else: 
        return 'E', 0 
     
#Menghitung IPK 
def hitung_ipk(mahasiswa): 
    for mhs in mahasiswa: 
        total_sks = 3 
        total_nilai = 0 
        matkul = ["fisika", "biologi", "matematika"] 
         
        print(f"\nNIM: {mhs['nim']}, Nama: {mhs['nama']}") 
        for mat in matkul: 
            nilai_huruf, skala =  konversi_nilai(mhs[mat]) 
            total_nilai += skala 
            print(f"{mat.capitalize()}: {mhs[mat]} -> {nilai_huruf} (skala {skala})") 
         
        ipk =  total_nilai / total_sks 
        print(f"IPK sementara: {ipk: .2f}") 
         
#memanggil fungsi hitung IPK 
hitung_ipk(mahasiswa)