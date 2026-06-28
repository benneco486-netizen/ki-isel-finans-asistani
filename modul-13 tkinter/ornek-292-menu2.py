import tkinter as tk
from tkinter import messagebox

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

kaydedildi_mi = False  # dosya kaydedildi mi?

def dosyaFonksiyonu():
    global kaydedildi_mi
    kaydedildi_mi = False
    print("Yeni Dosya")

def dosyaAc():
    global kaydedildi_mi
    kaydedildi_mi = False
    print("Dosya Aç")

def kaydet():
    global kaydedildi_mi
    kaydedildi_mi = True
    print("Kaydedildi")

def cikis():
    global kaydedildi_mi

    # Dosya kaydedilmediyse uyar
    if not kaydedildi_mi:
        cevap = messagebox.askyesno(
            "Uyarı",
            "Dosya kaydedilmedi!\nKaydetmeden çıkmak istiyor musunuz?"
        )
        if not cevap:
            return

    # Çıkış onayı
    cevap = messagebox.askyesno(
        "Çıkış",
        "Çıkmak istiyor musunuz?"
    )
    if cevap:
        pencere.destroy()

menu_cubugu = tk.Menu(pencere)
pencere.config(menu=menu_cubugu)

dosya = tk.Menu(menu_cubugu, tearoff=False)
menu_cubugu.add_cascade(label="Dosya", menu=dosya)

dosya.add_command(label="Yeni Dosya", command=dosyaFonksiyonu)
dosya.add_command(label="Aç", command=dosyaAc)
dosya.add_command(label="Kaydet", command=kaydet)
dosya.add_separator()
dosya.add_command(label="Çıkış", command=cikis)

pencere.mainloop()
