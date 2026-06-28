#frame ikinci örneği inceleyelim

import tkinter as tk
window = tk.Tk()
window.title("Uygulamaya Hoş geldiniz!")

sol_cerceve = tk.LabelFrame(window,
width=400,
height=250,
bg="gray",
text="Sol Çerçeve")
sol_cerceve.grid(row=0, column=0)

sag_cerceve = tk.LabelFrame(window,
width=400,
height=250,
bg="orange",
text="Sağ Çerçeve")
sag_cerceve.grid(row=0, column=1)

sol_cerceve_2 = tk.LabelFrame(window,
width=400,
height=250,
bg="red",
text="Sol Çerçeve Üst")
sol_cerceve_2.grid(row=1,column=0)

sag_cerceve_2 = tk.LabelFrame(window,
width=400,
height=250,
bg="blue",
text="Sağ Çerçeve Alt")
sag_cerceve_2.grid(row=1,column=1)

ensag_cerceve = tk.LabelFrame(window,
width=400,
height=250,
bg="pink",
text="Sağ Çerçeve")
ensag_cerceve.grid(row=1, column=2)

radyo_buton = tk.StringVar()
radyo_buton.set("1")

radyo_buton1 = tk.Radiobutton(sag_cerceve_2,
text="Radyo Buton 1",
value="1",
variable=radyo_buton)
radyo_buton1.place(x=100, y=160)

radyo_buton2 = tk.Radiobutton(sol_cerceve,
text="Radyo Buton 2",
value="2",
variable=radyo_buton)
radyo_buton2.place(x=100, y=160)

radyo_buton3 = tk.Radiobutton(sol_cerceve,
text="Radyo Buton 3",
value="3",
variable=radyo_buton)
radyo_buton3.place(x=200, y=160)

window.mainloop()