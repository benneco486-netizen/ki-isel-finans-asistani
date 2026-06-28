#2. örnek
import tkinter as tk
root = tk.Tk()
root.title("Bind Metodu Örneği 2")
root.geometry("600x400")

def fare_uzerine_geldi(event):

  event.widget.config(bg="red")

def fare_uzerinden_ayrildi(event):
  event.widget.config(bg="green")

buton = tk.Button(root, text="Üzerime Gelince Renk Değiştirir",
bg="lightgray", fg="black", padx=20, pady=10)
buton.pack(pady=20)

# Fare üzerine gelme olayını butona bağlama
buton.bind("<Enter>", fare_uzerine_geldi)
# Fare üzerinden ayrılma olayını butona bağlama
buton.bind("<Leave>", fare_uzerinden_ayrildi)

root.mainloop()
