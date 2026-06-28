import tkinter as tk
from tkinter import messagebox
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulama Hoş Geldiniz!")

def butonFonksiyonu():
    mesaj = messagebox.showinfo(
        title="Bilgi",
        message="Butona tıkladın." )
    
buton = tk.Button(
    pencere,
    text="Ben Bir Butonum",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    height=5,
    width=20,
    cursor="hand2",
    command= butonFonksiyonu)
buton.pack()
pencere.mainloop()