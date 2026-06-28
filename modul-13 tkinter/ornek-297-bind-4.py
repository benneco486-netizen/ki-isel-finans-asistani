import tkinter as tk

pencere = tk.Tk()
pencere.title("Bind Metodu - WASD Tuşları")
pencere.geometry("600x400")

x = 250
y = 150

etiket = tk.Label(pencere, text="🐵", font=("Arial", 30), fg="green")
etiket.place(x=x, y=y)

def hareket(event):
    global x, y

    if event.char == "a":      # SOL
        x -= 10
    elif event.char == "d":    # SAĞ
        x += 10
    elif event.char == "s":    # AŞAĞI
        y += 10
    elif event.char == "w":    # YUKARI
        y -= 10

    etiket.place(x=x, y=y)

pencere.bind("<Key>", hareket)
pencere.focus_set()

pencere.mainloop()
