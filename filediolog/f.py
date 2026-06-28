import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

etiket = None  # Önceki resmi saklayacağımız değişken

def dosyaAc():
    global etiket
    dosya = filedialog.askopenfilename(
        initialdir="C:/Users/Vektorel/Desktop/filediolog",
        title="Bir dosya seç...",
        filetypes=[("Resim Dosyaları", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    if not dosya:
        return  # Dosya seçilmemişse çık

    try:
        resim = Image.open(dosya)
        maks_boyut = (800, 600) # Maksimum boyut (800x600)
        resim.thumbnail(maks_boyut, Image.LANCZOS)  # Oranı koruyarak küçült
        resim_genislik, resim_yukseklik = resim.size
        # Pencereyi yeni boyuta göre ayarla (biraz boşluk ekleyerek)
        pencere.geometry(f"{resim_genislik + 40}x{resim_yukseklik + 80}")

        # Görseli tkinter'e uygun hale getir
        resim = ImageTk.PhotoImage(resim)

        if etiket:
            etiket.destroy()

        etiket = tk.Label(pencere, image=resim)
        etiket.image = resim
        etiket.pack(padx=20, pady=20)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

buton = tk.Button(pencere, text="📂 Resim Dosyası Aç", command=dosyaAc, bg="#4CAF50", fg="white", font=("Arial", 12))
buton.pack(pady=10)

pencere.mainloop()
