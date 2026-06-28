import tkinter as tk
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulama Hoş Geldiniz!")

def butonFonksiyonu():
    dialog = tk.Toplevel(pencere)
    dialog.title("Bilgi")
    dialog.geometry("300x150")
    dialog.resizable(False, False)
    dialog.grab_set()  # Odak bu pencerede kalsın

    label = tk.Label(dialog, text="Butona tıkladın.", font=("Arial", 12))
    label.pack(pady=30)

    btn = tk.Button(dialog, text="Tamam", command=dialog.destroy)
    btn.pack()

buton = tk.Button(
    pencere,
    text="Ben Bir Butonum",
    bg="orange",
    fg="black",
    font=24,
    height=5,
    width=20,
    cursor="hand2",
    command=butonFonksiyonu)
buton.pack()

pencere.mainloop()
