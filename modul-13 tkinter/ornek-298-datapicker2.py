import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Ana pencere
pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

# Tema stili
style = ttk.Style()
style.theme_use("xpnative")  # Modern tema seçimi (alternatifler: 'default', 'alt', 'clam', 'vista', 'xpnative')

# Başlık etiketi
baslik = ttk.Label(pencere, text="Lütfen bir tarih seçiniz:", font=("Segoe UI", 14, "bold"), padding=10)
baslik.pack(pady=(20, 10))

# Takvim
tarih = Calendar(pencere,
                 selectmode="day",
                 date_pattern="dd/MM/yyyy",
                 locale='tr_TR',
                 font=("Segoe UI", 10),
                 background="lightblue",
                 foreground="black",
                 headersbackground="lightgray",
                 headersforeground="black")
tarih.pack(pady=10)

# Seçilen tarihi gösterecek etiket
sonuc_label = ttk.Label(pencere, text="", font=("Segoe UI", 12), padding=10)
sonuc_label.pack(pady=(10, 20))

# Buton işlevi
def secilenTarih():
    secilen_tarih = tarih.get_date()
    sonuc_label.config(text=f"Seçilen tarih: {secilen_tarih}")

# Buton (ttk ile)
button = ttk.Button(pencere, text="Tarihi Göster", command=secilenTarih)
button.pack(pady=5)

pencere.mainloop()

