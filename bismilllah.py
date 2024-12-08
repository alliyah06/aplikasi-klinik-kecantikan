import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
import json
import os
import datetime


class Konsultasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Konsultasi Klinik Kecantikan")
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)
        self.selected_day = None
        self.selected_time = tk.StringVar()
        self.selected_skin_type = tk.StringVar()
        self.selected_face_problem = tk.StringVar()
        self.selected_treatments = []  # To store selected treatments
        self.selected_additional_treatments = []  # To store selected additional treatments
        self.customer_name = ""
        self.registered_customers = {}
        self.page_schedule()
        self.load_users()

        # Load registered customers
        try:
            with open("users.json", "r") as file:
                self.registered_customers = json.load(file)
        except FileNotFoundError:
            self.registered_customers = {}
 

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
    
    def exit_application(self):
        """Menampilkan dialog konfirmasi untuk keluar dari aplikasi."""
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
            self.root.destroy()

    def page_welcome(self):
        self.clear_window()

        # Memuat gambar sebagai background (ukuran seperti ppt)
        bg_image = Image.open(r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg welcome page fix.png") 
        bg_image = bg_image.resize((1280, 720))  
        self.bg_photo = ImageTk.PhotoImage(bg_image)  
        # Membuat canvas dan menampilkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=1280, height=720)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Membuat tombol login dan registrasi
        login_button = tk.Button(self.root, text="Login", font=("Arial", 15), command=self.page_login, bg="#990066", fg="#FFFFFF", width=12, height=1)
        reg_button = tk.Button(self.root, text="Registrasi", font=("Arial", 15), command=self.page_registration, bg="#990066", fg="#FFFFFF", width=15, height=1)

        # Menempatkan tombol di atas canvas
        canvas.create_window(625, 325, window=login_button)
        canvas.create_window(625, 400, window=reg_button)

    def page_registration(self):
        self.clear_window()

        # Ukuran window 1280x720
        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg input username pw fix.png"  # Ganti dengan path gambar Anda
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((window_width, window_height))  # Menyesuaikan gambar dengan ukuran window
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas dan menambahkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Username input
        canvas.create_text(500, 250, text="Username", font=("Garamond", 15), fill="#990066")
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        canvas.create_window(650, 250, window=self.name_entry)

        # Password input
        canvas.create_text(500, 300, text="Password", font=("Garamond", 15), fill="#990066")
        self.password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        canvas.create_window(650, 300, window=self.password_entry)

        # Eye button untuk menyembunyikan/menampilkan password
        self.eye_button = tk.Button(self.root, text="👁", command=self.toggle_password, font=("Arial", 12), bd=0)
        canvas.create_window(780, 300, window=self.eye_button)

        # Menambahkan tombol Registrasi dan Kembali
        register_button = tk.Button(self.root, text="Registrasi", font=("Arial", 13), command=self.register_user, bg="#990066", fg="#FFFFFF", width=10, height=1)
        back_button = tk.Button(self.root, text="Kembali", font=("Arial", 13), command=self.page_welcome, bg="#990066", fg="#FFFFFF", width=10, height=1)

        # Menempatkan tombol di atas canvas
        canvas.create_window(window_width // 1.98, 380, window=register_button)
        canvas.create_window(window_width // 1.98, 450, window=back_button)

    def toggle_password(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
            self.eye_button.config(text="🙈")
        else:
            self.password_entry.config(show="*")
            self.eye_button.config(text="👁")

    def register_user(self):
        username = self.name_entry.get()
        password = self.password_entry.get()

        if username and password:
            if username in self.registered_customers:
                messagebox.showerror("Error", "Username sudah terdaftar!")
            else:
                self.registered_customers[username] = {"password": password}
                # Menyimpan data pengguna ke file users.json
                folder_path = "data"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path, exist_ok=True)
                file_path = os.path.join(folder_path, "users.json")
                with open(file_path, "w") as file:
                    json.dump(self.registered_customers, file, indent=4)
                messagebox.showinfo("Registrasi Berhasil", "Registrasi berhasil, silahkan login")
                self.page_login()
        else:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong")


    def load_users(self):
        folder_path = "data"
        file_path = os.path.join(folder_path, "users.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                self.registered_customers = json.load(file)
        else:
            self.registered_customers = {}

 
    def page_login(self):
        self.clear_window()

        # Ukuran window 1280x720
        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg input login fix.png"  # Ganti dengan path gambar Anda
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((window_width, window_height))  # Menyesuaikan gambar dengan ukuran window
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas dan menambahkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Username input
        canvas.create_text(500, 250, text="Username", font=("Garamond", 15), fill="#990066")
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        canvas.create_window(650, 250, window=self.name_entry)

        # Password input
        canvas.create_text(500, 300, text="Password", font=("Garamond", 15), fill="#990066")
        self.password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        canvas.create_window(650, 300, window=self.password_entry)

        # Eye button untuk menyembunyikan/menampilkan password
        self.eye_button = tk.Button(self.root, text="👁", command=self.toggle_password, font=("Arial", 12), bd=0)
        canvas.create_window(780, 300, window=self.eye_button)

        # Menambahkan tombol Login dan Kembali
        login_button = tk.Button(self.root, text="Login", font=("Arial", 13), command=self.login_user, bg="#990066", fg="#FFFFFF", width=10, height=1)
        back_button = tk.Button(self.root, text="Kembali", font=("Arial", 13), command=self.page_welcome, bg="#990066", fg="#FFFFFF", width=10, height=1)

        # Menempatkan tombol di atas canvas
        canvas.create_window(window_width // 1.98, 380, window=login_button)
        canvas.create_window(window_width // 1.98, 450, window=back_button)
        
    def login_user(self):
        """Memverifikasi login pengguna"""
        # Ambil input dari Entry
        name = self.name_entry.get()
        password = self.password_entry.get()

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

        # Ukuran window 1280x720
        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg jenis kulit fix.png"  # Ganti dengan path gambar Anda
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((window_width, window_height))  # Menyesuaikan gambar dengan ukuran window
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas dan menambahkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Menambahkan combobox untuk memilih jenis kulit
        skin_types = ["Kering", "Normal", "Berminyak", "Kombinasi", "Sensitif", "Tidak Diketahui"]
        combobox = ttk.Combobox(self.root, textvariable=self.selected_skin_type, values=skin_types, state="readonly", font=("Arial", 12))
        canvas.create_window(window_width // 2, 275, window=combobox)

        def handle_skin_type_selection():
            if self.selected_skin_type.get() == "Tidak Diketahui":
                result = messagebox.showinfo("Informasi", "Silakan konsultasi untuk jenis kulit Anda terlebih dahulu kepada dokter.")
                if result:
                    self.page_schedule()
            elif not self.selected_skin_type.get():
                messagebox.showerror("Error", "Pilih jenis kulit terlebih dahulu!")
            else:
                self.page_face_problem()
        next_button = tk.Button(self.root, text="Selanjutnya", font=("Arial", 13), command=handle_skin_type_selection, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, 350, window=next_button)

        back_button = tk.Button(self.root, text="Kembali", font=("Arial", 13), command=self.page_login, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, 400, window=back_button)

    def page_face_problem(self):
        self.clear_window()

        # Ukuran window 1280x720
        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg face problem fix.png"
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((window_width, window_height))  # Menyesuaikan gambar dengan ukuran window
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas dan menambahkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Menambahkan combobox untuk memilih masalah wajah
        face_problems = ["Normal", "Berjerawat"]
        combobox = ttk.Combobox(self.root, textvariable=self.selected_face_problem, values=face_problems, state="readonly", font=("Arial", 12))
        canvas.create_window(window_width // 2, 275, window=combobox)

        def handle_face_problem_selection():
            if not self.selected_face_problem.get():
                messagebox.showerror("Error", "Pilih masalah wajah terlebih dahulu!")
            else:
                self.page_treatments()

        next_button = tk.Button(self.root, text="Selanjutnya", font=("Arial", 13), command=handle_face_problem_selection, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, 350, window=next_button)

        back_button = tk.Button(self.root, text="Kembali", font=("Arial", 13), command=self.page_skin_type, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, 400, window=back_button)
   
    def page_treatments(self):
        self.clear_window()

        # Ukuran window 1280x720
        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg perawatan wajah fix.png"  # Ganti dengan path gambar Anda
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((window_width, window_height))  # Menyesuaikan gambar dengan ukuran window
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas dan menambahkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Mendapatkan perawatan yang direkomendasikan berdasarkan jenis kulit dan masalah wajah
        skin_type = self.selected_skin_type.get().lower()
        face_problem = self.selected_face_problem.get().lower()

        available_treatments = self.recommended_treatments.get((skin_type, face_problem), {})
        self.selected_treatments.clear()  # Menghindari data duplikat

        # Menambahkan perawatan yang tersedia ke dalam daftar
        y_position = 240  # Posisi awal untuk checkbutton
        for index, (treatment, price) in enumerate(available_treatments.items()):
            var = tk.BooleanVar()
            treatment_text = f"{treatment} - Rp {price:,}"
            checkbutton = tk.Checkbutton(
                self.root, text=treatment_text, variable=var, font=("Garamond", 12), fg="#000000", anchor="w", bg="#FFFFFF")
            canvas.create_window(window_width // 2, y_position + (index * 40), window=checkbutton)
            self.selected_treatments.append((treatment, var, price))

        # Fungsi untuk menangani validasi perawatan yang dipilih
        def handle_treatments_selection():
            # Validasi: Pastikan pengguna memilih perawatan terlebih dahulu
            if not any(t[1].get() for t in self.selected_treatments):
                messagebox.showerror("Error", "Pilih perawatan terlebih dahulu!")
            else:
                self.page_additional_treatments()  # Lanjut ke halaman perawatan tambahan

        # Tombol "Selanjutnya"
        next_button = tk.Button(self.root, text="Selanjutnya", font=("Arial", 13), command=handle_treatments_selection, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, y_position + len(self.selected_treatments) * 40 + 50, window=next_button)

        # Tombol "Kembali"
        back_button = tk.Button(self.root, text="Kembali", font=("Arial", 13), command=self.page_face_problem, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, y_position + len(self.selected_treatments) * 40 + 100, window=back_button)

    def page_additional_treatments(self):
        self.clear_window()
        
        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg add treatment fix.png"
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((window_width, window_height)) 
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas dan menambahkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Menampilkan Checkbutton untuk treatment tambahan
        y_position = 240  # Posisi awal di canvas
        for treatment, price in self.additional_treatments.items():
            var = tk.BooleanVar()
            treatment_text = f"{treatment} - Rp {price:,}"
            checkbutton = tk.Checkbutton(self.root, text=treatment_text, variable=var, font=("Garamond", 12), bg="#FFFFFF", fg="#000000", anchor="w")
            canvas.create_window(window_width // 2, y_position, window=checkbutton)
            y_position += 40  # Jarak antar checkbutton
            self.selected_additional_treatments.append((treatment, var, price))

        # Tombol "Selanjutnya"
        next_button = tk.Button(self.root, text="Selanjutnya", font=("Arial", 13), command=self.page_schedule, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, y_position + 50, window=next_button)

        # Tombol "Kembali"
        back_button = tk.Button(self.root, text="Kembali", font=("Arial", 13), command=self.page_treatments, bg="#990066", fg="#FFFFFF", width=10, height=1)
        canvas.create_window(window_width // 2, y_position + 100, window=back_button)

    def read_schedule_db(self):
        try:
            with open('schedule_db.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def write_schedule_db(self, schedule_db):
        with open('schedule_db.json', 'w') as f:
            json.dump(schedule_db, f)

    def page_schedule(self):
        self.clear_window()

        # Ukuran window
        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg jadwal fix.png"
        bg_image = Image.open(bg_image_path).resize((window_width, window_height))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas untuk background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Pilihan Hari menggunakan kalender
        calendar = Calendar(self.root, selectmode="day", date_pattern="yyyy-MM-dd")
        canvas.create_window(window_width // 3.68, 350, window=calendar)

        # Pilihan Waktu
        self.selected_time = tk.StringVar()
        time_combobox = ttk.Combobox(self.root, textvariable=self.selected_time, state="readonly")
        canvas.create_window(window_width // 1.35, 300, window=time_combobox)

        def update_times(event):
            selected_day = calendar.get_date()
            if selected_day:
                # Menampilkan pesan konfirmasi tanggal
                date_obj = datetime.datetime.strptime(selected_day, "%Y-%m-%d")
                day_name = date_obj.strftime("%A")  # Nama hari, misalnya "Jumat"
                formatted_date = date_obj.strftime("%d %B %Y")  # Format tanggal, misalnya "06 Desember 2024"
                confirmation_message = f"Apakah Anda yakin memilih {day_name}, {formatted_date}?"
                
                # Menampilkan pesan konfirmasi
                confirmation = messagebox.askyesno("Konfirmasi Tanggal", confirmation_message)
                
                if confirmation:
                    # Jika ya, tampilkan pilihan waktu
                    schedule_db = self.read_schedule_db()
                    unavailable_times = schedule_db.get(selected_day, [])
                    all_times = ["10:00", "14:00", "17:00", "20:00"]  # Contoh waktu
                    available_times = [time for time in all_times if time not in unavailable_times]
                    time_combobox["values"] = available_times
                    self.selected_time.set("")
                else:
                    # Jika tidak, reset kalender dan combobox waktu
                    calendar.selection_clear()
                    time_combobox.set("")

        calendar.bind("<<CalendarSelected>>", update_times)

        # Tombol "Selanjutnya"
        def handle_schedule_selection():
            selected_day = calendar.get_date()
            selected_time = self.selected_time.get()

            if not selected_day:
                messagebox.showerror("Error", "Pilih hari terlebih dahulu!")
                return
            if not selected_time:
                messagebox.showerror("Error", "Pilih jam terlebih dahulu!")
                return

            schedule_db = self.read_schedule_db()
            if selected_day in schedule_db and selected_time in schedule_db[selected_day]:
                messagebox.showerror("Jadwal Sudah Terisi", f"Jadwal sudah penuh pada {selected_day} pukul {selected_time}.")
                return

            # Simpan jadwal
            if selected_day not in schedule_db:
                schedule_db[selected_day] = []
            schedule_db[selected_day].append(selected_time)
            self.write_schedule_db(schedule_db)

            # Simpan jadwal terpilih
            self.selected_day = selected_day
            self.selected_time.set(selected_time)

            self.page_summary()

        next_button = tk.Button(self.root, text="Selanjutnya", command=handle_schedule_selection, bg="#990066", fg="white")
        canvas.create_window(window_width // 2, 500, window=next_button)

        # Tombol "Kembali"
        back_button = tk.Button(self.root, text="Kembali", command=self.page_additional_treatments, bg="#990066", fg="white")
        canvas.create_window(window_width // 2, 550, window=back_button)

    def page_summary(self):
        self.clear_window()

        window_width = 1280
        window_height = 720
        self.root.geometry(f"{window_width}x{window_height}")

        # Menambahkan gambar sebagai background
        bg_image_path = r"C:\Users\Latian\Documents\aplikasi-klinik-kecantikan\bg nota fix.png"
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((window_width, window_height))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Membuat canvas dan menambahkan gambar sebagai background
        canvas = tk.Canvas(self.root, width=window_width, height=window_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Menghitung total harga
        total_treatment_price = sum([t[2] for t in self.selected_treatments if t[1].get()])
        total_additional_price = sum([t[2] for t in self.selected_additional_treatments if t[1].get()])
        total_price = total_treatment_price + total_additional_price
        if self.selected_skin_type.get() == "Tidak Diketahui":
            total_price += 100000  # Biaya konsultasi

        # Menentukan nama hari dan tanggal yang dipilih
        if self.selected_day:
            # Mengonversi tanggal menjadi objek datetime
            date_obj = datetime.datetime.strptime(self.selected_day, "%Y-%m-%d")
            day_name = date_obj.strftime("%A")  # Mendapatkan nama hari, misalnya "Monday"
            formatted_date = date_obj.strftime("%d %B %Y")  # Format tanggal, misalnya "06 Desember 2024"
        else:
            day_name = '-'
            formatted_date = '-'

        # Menampilkan summary text
        summary_text = f"""
    Nama: {self.customer_name if self.customer_name else '-'}
    Jenis Kulit: {self.selected_skin_type.get() if self.selected_skin_type.get() else '-'}
    Masalah Wajah: {self.selected_face_problem.get() if self.selected_face_problem.get() else '-'}
    Treatment: {', '.join([t[0] for t in self.selected_treatments if t[1].get()]) if any(t[1].get() for t in self.selected_treatments) else '-'}
    Treatment Tambahan: {', '.join([t[0] for t in self.selected_additional_treatments if t[1].get()]) if any(t[1].get() for t in self.selected_additional_treatments) else '-'}
    Jadwal Treatment: {day_name}, {formatted_date}, Pukul {self.selected_time.get() if self.selected_time.get() else '-'}
    Total Harga: Rp {total_price:,}
        """

        canvas.create_text(window_width // 2, 300, text=summary_text.strip(), fill="black", font=("Arial", 14), justify="center")

        # Tombol "Selesai"
        finish_button = tk.Button(self.root, text="Selesai", font=("Arial", 13), command=self.finish_consultation, bg="#990066", fg="#FFFFFF", width=15, height=1)
        canvas.create_window(window_width // 2, 500, window=finish_button)

    def finish_consultation(self):
        # Menampilkan pesan selesai dengan opsi Yes/No
        response = messagebox.askyesno("Selesai", "Konsultasi selesai! Terima kasih.\nApakah Anda ingin keluar?")
        if response:  # Jika memilih Yes
            self.exit_application()  # Keluar dari aplikasi
        else:  # Jika memilih No
            self.page_welcome()  # Kembali ke halaman utama


if __name__== "__main__":
    root = tk.Tk()
    app = Konsultasi(root)  # Pastikan konstruktor kelas Konsultasi adalah init
    app.page_welcome()      # Menampilkan halaman selamat datang
    root.mainloop()         # Memulai loop utama tkinter