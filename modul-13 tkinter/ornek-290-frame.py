import tkinter as tk
window = tk.Tk()
window.title("Uygulamaya Hoş geldiniz!")

sol_cerceve = tk.LabelFrame(window,
width=400,
height=500,
bg="gray",
text="Sol Çerçeve")
sol_cerceve.grid(row=0, column=0)

sag_cerceve = tk.LabelFrame(window,
width=400,
height=500,
bg="orange",
text="Sağ Çerçeve")
sag_cerceve.grid(row=0, column=1)

sol_cerceve_1 = tk.LabelFrame(sol_cerceve,
width=400,
height=300,
bg="red",
text="Sol Çerçeve Üst")
sol_cerceve_1.grid(row=0,column=0)

sol_cerceve_2 = tk.LabelFrame(sol_cerceve,
width=400,
height=200,
bg="blue",
text="Sol Çerçeve Alt")
sol_cerceve_2.grid(row=1,column=0)

window.mainloop()