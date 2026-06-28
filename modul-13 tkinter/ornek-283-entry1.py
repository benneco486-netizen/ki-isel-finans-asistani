import tkinter as tk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Entry Uygulamasına Hoş Geldiniz!")

giris = tk.Entry(pencere, width=50)
giris.insert(string="Kafanıza göre bir şeyler yazın...", index=0)

giris.pack()

pencere.mainloop()