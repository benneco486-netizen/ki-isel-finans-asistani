import tkinter as tk
from tkinter import ttk
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

bilesenler = ttk.Notebook(pencere,
width=550,
height=400)
bilesenler.place(x = 25, y = 25)

bilesen1 = ttk.Frame(bilesenler,
width=50,
height=50)

bilesen2 = ttk.Frame(bilesenler,
width=50,
height=50)

bilesen3 = ttk.Frame(bilesenler,
width=50,
height=50)

grafik = tk.Label(bilesen1,
text="Grafik Sekmesi")
grafik.pack()

tablo = tk.Label(bilesen2,
text="Tablo Sekmesi")
tablo.pack()

buton = tk.Button(bilesen3,
text="Tıkla",
bg="orange",
fg="black",
activebackground="red",
activeforeground="black",
font=24,
height=2,
width=10,
cursor="hand2",)
buton.place(relx=0.4,rely=0.1)

bilesenler.add(bilesen1,
text="Grafik")

bilesenler.add(bilesen2,
text="Tablo")

bilesenler.add(bilesen3,
text="Yazılım")

pencere.mainloop()