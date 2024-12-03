import tkinter as tk
from tkinter import ttk, messagebox
import json

class Konsultasi:
    def __init__(self, root):
        self.root = root
        self.selected_day = tk.StringVar()
        self.selected_time = tk.StringVar()
        self.selected_skin_type = tk.StringVar()
        self.selected_face_problem = tk.StringVar()
        self.selected_treatments = []  # To store selected treatments
        self.selected_additional_treatments = []  # To store selected additional treatments
        self.customer_name = ""

        # Load registered customers
        try:
            with open("users.json", "r") as file:
                self.registered_customers = json.load(file)
        except FileNotFoundError:
            self.registered_customers = {}

        self.schedule = {
            "Senin": ["11.00", "13.00", "16.00", "20.00"],
            "Selasa": ["11.00", "13.00", "16.00", "20.00"],
            "Rabu": ["11.00", "13.00", "16.00", "20.00"],
            "Kamis": ["11.00", "13.00", "16.00", "20.00"],
            "Jumat": ["13.00", "17.00", "20.00"],
        }

        # Data untuk treatment yang disarankan berdasarkan jenis kulit dan masalah wajah
        self.recommended_treatments = {
            ("kering", "normal"): {
                "Hydrating Facial": 300000,
                "Moisturizing Treatment": 250000,
                "Gentle Hydration": 400000,
                "Nourishing Treatment": 300000,
                "Vitamin C Infusion": 400000
            },
            ("kering", "berjerawat"): {
                "Gentle Exfoliation": 200000,
                "Salicylic Acid Treatment": 350000,
                "Soothing Facial": 350000,
                "Hydrating Facial": 300000
            },
            ("normal", "normal"): {
                "Balancing Facial": 250000,
                "Nourishing Treatment": 300000,
                "Hydrating Facial": 300000,
                "Vitamin C Infusion": 400000
            },
            ("normal", "berjerawat"): {
                "Oil Control Facial": 300000,
                "Gentle Exfoliation": 200000,
                "Salicylic Acid Treatment": 350000,
                "Soothing Facial": 350000
            },
            ("berminyak", "normal"): {
                "Oil Control Facial": 300000,
                "Balancing Facial": 250000,
                "Hydrating Facial": 300000,
                "Vitamin C Infusion": 400000
            },
            ("berminyak", "berjerawat"): {
                "Salicylic Acid Treatment": 350000,
                "Gentle Exfoliation": 200000,
                "Oil Control Facial": 300000,
                "Soothing Facial": 350000
            },
            ("kombinasi", "normal"): {
                "Balancing Facial": 250000,
                "Hydrating Facial": 300000,
                "Nourishing Treatment": 300000,
                "Gentle Exfoliation": 200000
            },
            ("kombinasi", "berjerawat"): {
                "Oil Control Facial": 300000,
                "Salicylic Acid Treatment": 350000,
                "Soothing Facial": 350000,
                "Mikrodermabrasi": 300000
            },
            ("sensitif", "normal"): {
                "Soothing Facial": 350000,
                "Gentle Hydration": 400000,
                "Nourishing Treatment": 300000,
                "Vitamin C Infusion": 400000
            },
            ("sensitif", "berjerawat"): {
                "Gentle Exfoliation": 200000,
                "Soothing Facial": 350000,
                "Salicylic Acid Treatment": 350000
            }
        }

        # Data untuk treatment tambahan
        self.additional_treatments = {
            "Treatment Muka Segar": 150000,
            "Treatment Pembersihan Mendalam": 200000,
            "Treatment Anti Aging": 300000,
            "Treatment Pencerah Kulit": 250000,
            "Treatment Relaksasi Wajah": 200000
        }

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def page_welcome(self):
        self.clear_window()
        tk.Label(self.root, text="SELAMAT DATANG DI KLINIK KECANTIKAN GALIYA", font=("Arial", 18)).pack(pady=20)
        tk.Button(self.root, text="Login", command=self.page_login, bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Registrasi", command=self.page_registration, bg="#990066", fg="#FFFFFF").pack(pady=20)

    def page_registration(self):
        self.clear_window()
        tk.Label(self.root, text="Masukkan Username dan Password Anda", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.root, text="Username").pack(pady=5)
        name_entry = tk.Entry(self.root, font=("Arial", 12))
        name_entry.pack(pady=10)

        tk.Label(self.root, text="Password").pack(pady=5)
        password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        password_entry.pack(pady=10)

        tk.Button(self.root, text="Registrasi", command=lambda: self.register_user(name_entry.get(), password_entry.get()), bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_welcome, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def register_user(self, name, password):
        if name and password:
            if name in self.registered_customers:
                messagebox.showerror("Error", "Username sudah terdaftar!")
            else:
                self.registered_customers[name] = {"password": password}
                with open("users.json", "w") as file:
                    json.dump(self.registered_customers, file)
                messagebox.showinfo("Registrasi Berhasil", "Registrasi berhasil, silahkan login")
                self.page_login()
        else:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong")

    def page_login(self):
        self.clear_window()
        tk.Label(self.root, text="Masukkan Username dan Password untuk Login", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.root, text="Username").pack(pady=5)
        name_entry = tk.Entry(self.root, font=("Arial", 12))
        name_entry.pack(pady=10)

        tk.Label(self.root, text="Password").pack(pady=5)
        password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        password_entry.pack(pady=10)

        tk.Button(self.root, text="Login", command=lambda: self.login_user(name_entry.get(), password_entry.get()), bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_welcome, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def login_user(self, name, password):
        """Memverifikasi login pengguna"""
        if not name or not password:
            messagebox.showerror("Error", "Username dan password wajib diisi!")
        elif name not in self.registered_customers:
            messagebox.showerror("Error", "Akun belum terdaftar, silakan registrasi dahulu.")
        elif self.registered_customers[name]["password"] != password:
            messagebox.showerror("Error", "Sandi salah, silakan periksa kembali.")
        else:
            self.customer_name = name
            messagebox.showinfo("Sukses", f"Selamat datang, {self.customer_name}!")
            self.page_skin_type()

    def page_skin_type(self):
        self.clear_window()
        tk.Label(self.root, text="Pilih Jenis Kulit Anda", font=("Arial", 14)).pack(pady=20)

        skin_types = ["Kering", "Normal", "Berminyak", "Kombinasi", "Sensitif", "Tidak Diketahui"]

        combobox = ttk.Combobox(self.root, textvariable=self.selected_skin_type, values=skin_types, state="readonly")
        combobox.pack(pady=10)

        def handle_skin_type_selection():
            if self.selected_skin_type.get() == "Tidak Diketahui":
                result = messagebox.showinfo("Informasi", "Silakan konsultasi untuk jenis kulit Anda terlebih dahulu kepada dokter.")
                if result:
                    self.page_schedule()
            elif not self.selected_skin_type.get():
                messagebox.showerror("Error", "Pilih jenis kulit terlebih dahulu!")
            else:
                self.page_face_problem()

        tk.Button(self.root, text="Selanjutnya", command=handle_skin_type_selection, bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_login, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def page_face_problem(self):
        self.clear_window()
        tk.Label(self.root, text="Pilih Masalah Wajah Anda", font=("Arial", 14)).pack(pady=20)

        face_problems = ["Normal", "Berjerawat"]

        combobox = ttk.Combobox(self.root, textvariable=self.selected_face_problem, values=face_problems, state="readonly")
        combobox.pack(pady=10)
        
        def handle_face_problem_selection():
            if not self.selected_face_problem.get():
                messagebox.showerror("Error", "Pilih masalah wajah terlebih dahulu!")
            else:
                self.page_treatments()

        tk.Button(self.root, text="Selanjutnya", command=handle_face_problem_selection, bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_skin_type, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def page_treatments(self):
        self.clear_window()
        tk.Label(self.root, text="Pilih Perawatan Wajah Anda", font=("Arial", 14)).pack(pady=20)

        # Get recommended treatments based on selected skin type and face problem
        skin_type = self.selected_skin_type.get().lower()
        face_problem = self.selected_face_problem.get().lower()

        available_treatments = self.recommended_treatments.get((skin_type, face_problem), {})

        # Menambahkan perawatan yang tersedia ke dalam daftar
        for treatment, price in available_treatments.items():
            var = tk.BooleanVar()
            # Memusatkan checkbutton secara horizontal
            tk.Checkbutton(self.root, text=f"{treatment} - Rp {price:,}", variable=var).pack(anchor="center", pady=5)
            # Menyimpan perawatan yang dipilih dalam selected_treatments
            self.selected_treatments.append((treatment, var, price))

        # Fungsi untuk menangani validasi perawatan yang dipilih
        def handle_treatments_selection():
        # Validasi: Pastikan pengguna memilih perawatan terlebih dahulu
            if not any(t[1].get() for t in self.selected_treatments):
                messagebox.showerror("Error", "Pilih perawatan terlebih dahulu!")
            else:
             self.page_additional_treatments()  # Lanjut ke halaman perawatan tambahan

        # Tombol "Selanjutnya" akan memanggil fungsi validasi
        tk.Button(self.root, text="Selanjutnya", command=handle_treatments_selection, bg="#990066", fg="#FFFFFF").pack(pady=20)
        # Tombol "Kembali" untuk kembali ke halaman sebelumnya
        tk.Button(self.root, text="Kembali", command=self.page_face_problem, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def page_additional_treatments(self):
        self.clear_window()
        tk.Label(self.root, text="Pilih Treatment Tambahan (Opsional)", font=("Arial", 14)).pack(pady=20)

        for treatment, price in self.additional_treatments.items():
            var = tk.BooleanVar()
            # Memusatkan checkbutton secara horizontal
            tk.Checkbutton(self.root, text=f"{treatment} - Rp {price:,}", variable=var).pack(anchor="center", pady=5)
            self.selected_additional_treatments.append((treatment, var, price))

        tk.Button(self.root, text="Selanjutnya", command=self.page_schedule, bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_treatments, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def page_schedule(self):
        self.clear_window()
        tk.Label(self.root, text="Pilih Jadwal Konsultasi", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Pilih Hari Konsultasi", font=("Arial", 14)).pack(pady=20)

        days = list(self.schedule.keys())
        combobox = ttk.Combobox(self.root, textvariable=self.selected_day, values=days, state="readonly")
        combobox.pack(pady=10)

        def handle_schedule_selection():
            if not self.selected_day.get():
                messagebox.showerror("Error", "Pilih hari terlebih dahulu!")
            else:
                self.page_time_selection()

        tk.Button(self.root, text="Selanjutnya", command=handle_schedule_selection, bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_additional_treatments, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def page_time_selection(self):
        self.clear_window()
        tk.Label(self.root, text="Pilih Jadwal Konsultasi", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Pilih Waktu Konsultasi", font=("Arial", 14)).pack(pady=20)

        times = self.schedule.get(self.selected_day.get(), [])
        combobox = ttk.Combobox(self.root, textvariable=self.selected_time, values=times, state="readonly")
        combobox.pack(pady=10)

        def handle_time_selection():
            if not self.selected_time.get():
                messagebox.showerror("Error", "Pilih waktu terlebih dahulu!")
            else:
                self.page_summary()

        tk.Button(self.root, text="Selanjutnya", command=handle_time_selection, bg="#990066", fg="#FFFFFF").pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_schedule, bg="#990066", fg="#FFFFFF").pack(pady=10)

    def page_summary(self):
        self.clear_window()
        tk.Label(self.root, text="Nota Konsultasi", font=("Arial", 14)).pack(pady=20)

        # Menghitung total harga perawatan yang dipilih
        total_treatment_price = sum([t[2] for t in self.selected_treatments if t[1].get()])

        # Menghitung total harga perawatan tambahan yang dipilih
        total_additional_price = sum([t[2] for t in self.selected_additional_treatments if t[1].get()])

        # Total harga keseluruhan (termasuk perawatan dan tambahan)
        total_price = total_treatment_price + total_additional_price

        # Menambahkan biaya konsultasi untuk pelanggan dengan jenis kulit 'konsultasi jenis kulit'
        if self.selected_skin_type.get() == 'Tidak Diketahui':  # Periksa apakah jenis kulit adalah 'konsultasi jenis kulit'
            total_price += 100000  # Menambahkan biaya konsultasi 100rb

        # Menampilkan summary text dengan total harga
        summary_text = f"Nama: {self.customer_name if self.customer_name else '-'}\n" \
                   f"Jenis Kulit: {self.selected_skin_type.get() if self.selected_skin_type.get() else '-'}\n" \
                   f"Masalah Wajah: {self.selected_face_problem.get() if self.selected_face_problem.get() else '-'}\n" \
                   f"Perawatan yang Dipilih: {', '.join([t[0] for t in self.selected_treatments if t[1].get()]) if any(t[1].get() for t in self.selected_treatments) else '-'}\n" \
                   f"Perawatan Tambahan: {', '.join([t[0] for t in self.selected_additional_treatments if t[1].get()]) if any(t[1].get() for t in self.selected_additional_treatments) else '-'}\n" \
                   f"Jadwal: {self.selected_day.get() if self.selected_day.get() else '-'} {self.selected_time.get() if self.selected_time.get() else '-'}\n" \
                   f"Total Harga: Rp {total_price:,}\n"

        tk.Label(self.root, text=summary_text).pack(pady=20)

        def finish_consultation():
            messagebox.showinfo("Selesai", "Konsultasi selesai! Terima kasih.")
            self.page_welcome()

        tk.Button(self.root, text="Selesai", command=finish_consultation, bg="#990066", fg="#FFFFFF").pack(pady=20)

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = Konsultasi(root)
    app.page_welcome()
    root.mainloop()