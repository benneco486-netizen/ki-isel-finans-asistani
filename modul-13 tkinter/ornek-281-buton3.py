import tkinter as tk
window = tk.Tk()
window.geometry("600x450")
window.title("Renk Değişen Buton Örneği")

def on_enter(e):
    button.config(bg="lightblue",text="Rengim Değişti")
def on_leave(e):
    button.config(bg="SystemButtonFace",text="Renk Değişen Buton")  # Sistemin varsayılan buton rengi

button = tk.Button(window,
                   text="Renk Değiştiren Buton",
                   bg="red",
                   fg="black",
                   font=("Tahoma", 10, "bold", "italic"),
                   height=4,
                   width=30,
                   cursor="spider",
                   command=lambda: print("Tıklandı!"))
button.pack(pady=20)

button.bind("<Enter>", on_enter)  # Mouse butonun üzerine geldiğinde
button.bind("<Leave>", on_leave)  # Mouse butonun üzerinden ayrıldığında

window.mainloop()
