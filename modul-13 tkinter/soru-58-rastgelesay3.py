# 2. yol
import tkinter as tk
from tkinter import messagebox
import random

def generate_random_numbers():
    try:
        # 1 ile 100 arasında 6 benzersiz sayı üret
        random_numbers = random.sample(range(1, 101), 6)

        # Sonuçları göster
        result_label.config(text=f"Üretilen Sayılar: {', '.join(map(str,# random_numbers))}")

        # Sayıları ayrı ayrı kutularda göster
        for i, num in enumerate(random_numbers):
            number_labels[i].config(text=str(num))

    except Exception as e:
        messagebox.showerror("Hata", f"Sayı üretilirken bir hata oluştu: {str(e)}")

# Ana pencere oluştur
root = tk.Tk()
root.title("Rastgele Sayı Üreteci")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Başlık
header = tk.Label(root, text="1-100 Arası 6 Benzersiz Rastgele Sayı",
                 font=("Arial", 14, "bold"), bg="#f0f0f0", pady=10)
header.pack()

# Sayıları göstermek için frame
numbers_frame = tk.Frame(root, bg="#f0f0f0")
numbers_frame.pack(pady=20)

# 6 sayı için kutuları oluştur
number_labels = []
for i in range(6):
    number_frame = tk.Frame(numbers_frame, width=50, height=50,
                           bg="#ffffff", bd=1, relief=tk.RAISED)
    number_frame.grid(row=0, column=i, padx=5)
    number_frame.pack_propagate(False)

    label = tk.Label(number_frame, text="-", font=("Arial", 16, "bold"), bg="#ffffff")
    label.pack(expand=True)
    number_labels.append(label)

# Sonuç etiketi
result_label = tk.Label(root, text="Henüz sayı üretilmedi", bg="#f0f0f0", font=("Arial", 10))
result_label.pack(pady=10)

# Buton
generate_button = tk.Button(root, text="Rastgele Sayılar Üret",
                           command=generate_random_numbers,
                           bg="#4CAF50", fg="white",
                           font=("Arial", 12),
                           relief=tk.RAISED, bd=2,
                           padx=10, pady=5)
generate_button.pack(pady=20)

# Açıklama
description = tk.Label(root, text="Bu program 1-100 arasında 6 benzersiz rastgele sayı üretir.",
                      font=("Arial", 8), bg="#f0f0f0")
description.pack(side=tk.BOTTOM, pady=10)

# Uygulamayı başlat
root.mainloop()