import tkinter as tk
from tkinter import ttk
pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")

bolunmus_pencere_h = ttk.PanedWindow(pencere,
orient=tk.HORIZONTAL) #Yerleşimi yatay olarak ayarlanır.
bolunmus_pencere_h.pack(fill=tk.BOTH, expand=True)

bolunmus_pencere_v = ttk.PanedWindow(bolunmus_pencere_h,
orient=tk.VERTICAL ) #Yerleşimi dikey olarak ayarlanır.

cerceve_1 = ttk.Frame(bolunmus_pencere_h,
width=600,
height=200,
relief=tk.RIDGE) #Kenarlık görünümü ayarlanır. sırt kenarlıklı ayarlanır

cerceve_2 = ttk.Frame(bolunmus_pencere_h,
width=600,
height=300,
relief=tk.RAISED) #Kenarlık görünümü ayarlanır. yükseltilmiş kenarlık ayarlanır

cerceve_3 = ttk.Frame(bolunmus_pencere_h,
width=240,
height=500,
relief=tk.GROOVE) #Kenarlık görünümü ayarlanır. oluklu(kanal) kenarlık ayarlanır

bolunmus_pencere_h.add(bolunmus_pencere_v)
bolunmus_pencere_v.add(cerceve_1)
bolunmus_pencere_v.add(cerceve_2)
bolunmus_pencere_h.add(cerceve_3)

pencere.mainloop()