#3. örnek
import tkinter as tk

# Pencere boyutları ve kare boyutu
PENCERE_GENISLIGI = 400
PENCERE_YUKSEKLIGI = 300
KARE_BOYUTU = 20
HAREKET_MESAFESI = 10

# Kare başlangıç pozisyonu
kare_x = (PENCERE_GENISLIGI // 2) - (KARE_BOYUTU // 2)
kare_y = (PENCERE_YUKSEKLIGI // 2) - (KARE_BOYUTU // 2)

def kareyi_ciz(): #Kareyi canvas üzerine çizer.
  canvas.coords(kare, kare_x, kare_y, kare_x + KARE_BOYUTU, kare_y + KARE_BOYUTU)

def sola_hareket(event):
  global kare_x
kare_x -= HAREKET_MESAFESI
if kare_x < 0:
  kare_x = 0
kareyi_ciz()

def saga_hareket(event):
  global kare_x
kare_x += HAREKET_MESAFESI
if kare_x > PENCERE_GENISLIGI - KARE_BOYUTU:
  kare_x = PENCERE_GENISLIGI - KARE_BOYUTU
kareyi_ciz()

def yukari_hareket(event):
  global kare_y
kare_y -= HAREKET_MESAFESI
if kare_y < 0:
  kare_y = 0
kareyi_ciz()

def asagi_hareket(event):
  global kare_y
kare_y += HAREKET_MESAFESI
if kare_y > PENCERE_YUKSEKLIGI - KARE_BOYUTU:
  kare_y = PENCERE_YUKSEKLIGI - KARE_BOYUTU
kareyi_ciz()

# Ana pencere oluşturma
root = tk.Tk()
root.title("Klavye ile Kare Hareketi Oyunu")

# Canvas oluşturma
canvas = tk.Canvas(root, width=PENCERE_GENISLIGI, height=PENCERE_YUKSEKLIGI, bg="#ffffcc")
canvas.pack()

# Kare oluşturma
kare = canvas.create_rectangle(kare_x, kare_y, kare_x + KARE_BOYUTU, kare_y + KARE_BOYUTU, fill="red")

# Klavyeden ok tuşlarına basıldığında hareket fonksiyonlarını bağlama
root.bind("<Left>", sola_hareket)
root.bind("<Right>", saga_hareket)
root.bind("<Up>", yukari_hareket)
root.bind("<Down>", asagi_hareket)

# Oyunun odaklanmasını sağlama (klavye olaylarını yakalayabilmek için)
canvas.focus_set()

root.mainloop()