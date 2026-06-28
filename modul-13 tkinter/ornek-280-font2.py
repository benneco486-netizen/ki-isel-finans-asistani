import tkinter as tk
pencere = tk.Tk()
pencere.title("tkinter penceresi")
pencere.geometry("300x200+500+200")
# geometry ile pencerin boyutlarını ayarlşıyoruz.pencere.geometry("enxboy+x+y")

giris_etiketi= tk.Label(pencere,
                        text="kullanıcı adı",
                        fg="red",
                        font=("tahoma",30,"bold","italic"))

giris_etiketi.pack()

giris_alani =tk.Entry(pencere)
giris_alani.pack()

pencere.mainloop()