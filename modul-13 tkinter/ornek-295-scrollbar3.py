#3.yol birlikte
import tkinter as tk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

# Scrollbar'lar ve metin kutusu için çerçeve
cerceve = tk.Frame(pencere)
cerceve.pack(fill=tk.BOTH, expand=True)

# Text alanı (hiçbir yönde otomatik kaydırma yok)
metin = tk.Text(cerceve, wrap=tk.NONE)
metin.grid(row=0, column=0, sticky="nsew")

# Dikey kaydırma çubuğu
dikey_scroll = tk.Scrollbar(cerceve, orient=tk.VERTICAL, command=metin.yview)
dikey_scroll.grid(row=0, column=1, sticky="ns")

# Yatay kaydırma çubuğu
yatay_scroll = tk.Scrollbar(cerceve, orient=tk.HORIZONTAL, command=metin.xview)
yatay_scroll.grid(row=1, column=0, sticky="ew")

# Scrollbar'ları text alanına bağlama
metin.config(yscrollcommand=dikey_scroll.set, xscrollcommand=yatay_scroll.set)

# Grid konfigürasyonu
cerceve.rowconfigure(0, weight=1)
cerceve.columnconfigure(0, weight=1)

# Buton işlevi
def metinFonksiyonu():
    print(metin.get(1.0, tk.END))

# Kaydet butonu
buton = tk.Button(pencere, text="Kaydet", command=metinFonksiyonu)
buton.pack(pady=10)

pencere.mainloop()
