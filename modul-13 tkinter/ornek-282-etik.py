import tkinter as tk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Label Uygulamasına Hoş Geldiniz!")

etiket = tk.Label(
    pencere,
    text="Ben Bir Etiketim",
    font=("Tahoma", 24),
    bg="#00e5ee",
    fg="black",
    wraplength=250  # Metni etiket içinde 250 piksel genişliğinde satır başı yapar
)

etiket.pack()

pencere.mainloop()