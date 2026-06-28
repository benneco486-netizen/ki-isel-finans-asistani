#1. yol
import tkinter as tk
import random
pencere = tk.Tk()           # Pencere oluşturma
pencere.title("Benzersiz Rastgele Sayılar")

# benzersiz rastgele sayılar üreten fonksiyon
def benzersiz_rastgele_sayilar(n, alt_sinir, ust_sinir):
  rastgele_sayilar = []
  while len(rastgele_sayilar) < n:
    sayi = random.randint(alt_sinir, ust_sinir)
    if sayi not in rastgele_sayilar:
      rastgele_sayilar.append(sayi)
  return rastgele_sayilar

# Butona tıklandığında etiket içinin yenileneceği fonksiyon
def yenile():
  rastgele_sayilar = benzersiz_rastgele_sayilar(6, 1, 100)
  for i, sayi in enumerate(rastgele_sayilar):
    etiketler[i].config(text=sayi)

etiketler = []           # Etiketler oluşturma

for i in range(6):
  etiketler.append(tk.Label(pencere, text="...", font=("Arial", 12, "bold")))
  etiketler[i].grid(row=i, column=0, padx=10, pady=5)

yenile_butonu = tk.Button(pencere, text="Yenile", command=yenile)
yenile_butonu.grid(row=6, column=0, padx=10, pady=5)

pencere.mainloop()      # Pencereyi çalıştırma
