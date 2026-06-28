import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

def secilenTarih():
    secilen_tarih = tarih.get_date() #Takvim widget'ından seçilen tarihi alır.
    print(f"Seçilen tarih: {secilen_tarih}")

tarih = Calendar(pencere,
    selectmode="day",   #Sadece gün seçimine izin verir.
    date_pattern="dd/MM/yyyy")  #Tarih biçimini gün/ay/yıl olarak ayarlar.
tarih.pack()

button = tk.Button(pencere, text="Tarih Seç", command=secilenTarih,
                   bg="#4CAF50", fg="white", font=("Arial", 12))
button.pack()
pencere.mainloop()