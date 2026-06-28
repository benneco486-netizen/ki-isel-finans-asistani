import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Combox Örneği")

def butonFonksiyonu():
    acilirkutu = acilir_kutu.get()
    if acilirkutu =="İstanbul":
        print("İstanbul seçildi.")
    elif acilirkutu =="Ankara":
        print("Ankara seçildi.")
    elif acilirkutu =="İzmir":
        print("İzmir seçildi.")
    elif acilirkutu =="Antalya":
        print("Antalya seçildi.")
    elif acilirkutu =="Sivas":
        print("Sivas seçildi.")
    elif acilirkutu =="Adana":
        print("Adana seçildi.")

buton = tk.Button(pencere,text="Tıkla",bg="orange",fg="black",activebackground="red",
    activeforeground="black",font=24,height=2,width=10,cursor="hand2",
    command= butonFonksiyonu)
buton.pack(pady=10)

acilir_kutu=tk.StringVar()  
#Değişken bir metin olarak alır. İçeriği dinamik olarak günceller.
acilir_kutu=ttk.Combobox(pencere,
                         textvariable = acilir_kutu,
                         values=("İstanbul","Ankara","İzmir","Antalya","Sivas","Adana"),
                         state="readonly")
acilir_kutu.place(relx=0.4, rely=0.3)

pencere.mainloop()