import tkinter as tk
from tkinter import messagebox
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

def butonFonksiyonu():
    rb = radyo_buton.get()   #get:hangi radyo buton seçilirse verisi gelmesidir.
    if rb == "1":
          mesaj = messagebox.showinfo(title="RADYO BUTON 1 BİLGİSİ",
          message="Elma Doğru Seçim")
    elif rb == "2":
          mesaj = messagebox.showinfo(title="RADYO BUTON 2 BİLGİSİ",
          message="Armut Doğru Seçim")
    elif rb == "3":
          mesaj = messagebox.showinfo(title="RADYO BUTON 3 BİLGİSİ",
          message="Portakal Doğru Seçim")
    else:
          mesaj = messagebox.showinfo(title="RADYO BUTON BİLGİSİ",
          message="Hiçbir Seçim Yapmadınız")


buton = tk.Button(
    pencere,
    text="Tıkla",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="black",
    font=24,
    height=2,
    width=10,
    cursor="hand2",
    command= butonFonksiyonu)
buton.pack(pady=10)

radyo_buton = tk.StringVar()
radyo_buton.set("0") #Hiçbiri seçili değil 1,2,3 yazarsak o seçenek seçili olur

radyo_buton1 = tk.Radiobutton(pencere, text="Elma", value="1",variable=radyo_buton)
radyo_buton1.place(x=100, y=160)
radyo_buton2 = tk.Radiobutton(pencere,text="Armut",value="2",variable=radyo_buton)
radyo_buton2.place(x=250, y=160)
radyo_buton3 = tk.Radiobutton(pencere,text="Portakal",value="3",variable=radyo_buton)
radyo_buton3.place(x=400, y=160)

pencere.mainloop()