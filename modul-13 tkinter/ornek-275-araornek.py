import tkinter as tk

pencere = tk.Tk()

def toggle_fullscreen(event=None): # fonksiyonun isteğe bağlı bir event parametresi vardır
    pencere.attributes("-fullscreen",not pencere.attributes("-fullscreen"))

pencere.bind("f11",toggle_fullscreen)
# f11 tuşuna basıldığında ftam ekran modu değiştirilir
pencere.mainloop()  