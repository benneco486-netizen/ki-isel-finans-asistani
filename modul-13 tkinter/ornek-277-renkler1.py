import tkinter as tk
pencere = tk.Tk()
pencere.title("renk kodu örneği")

etiket= tk.Label(pencere,
                  text="merhaba 127 python grubu",
                  fg="#000000",
                  bg="#00868b")
etiket.pack()
tk.mainloop()