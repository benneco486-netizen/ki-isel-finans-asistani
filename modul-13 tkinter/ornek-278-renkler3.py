import tkinter as tk
pencere = tk.Tk()
pencere.title("Renk Örneği 3")
pencere.geometry("300x150")

# Etiket oluştur (ön plan rengi kırmızı, arka plan sarı)
etiket = tk.Label(pencere, text="Merhaba Tkinter!", fg="red", bg="#FFFF00")
etiket.pack(pady=20)

# Düğme oluştur (ön plan beyaz, arka plan mavi)
dugme = tk.Button(pencere, text="Tıkla", fg="white", bg="#0000FF")
dugme.pack()

pencere.mainloop()