import tkinter as tk
pencere = tk.Tk()
pencere.title("tkinter penceresi")

pencere.geometry("300x200+500+200")
# geometry ile pencerin boyutlarını ayarlşıyoruz.pencere.geometry("enxboy+x+y")

etiket=tk.Label(pencere,
                text="Merhaba python127 grubu",
                fg="red",
                font=("tahoma",30,"bold","italic"))
etiket.pack()
pencere.mainloop()