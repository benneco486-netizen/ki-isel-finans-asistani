import tkinter as tk
from tkinter import messagebox
pencere =tk.Tk()
pencere.geometry("400x400")

def bilgimesaji():
  messagebox.showinfo("bilgi","bu bir bilgi mesajdır")
def uyarimesaji():
  messagebox.showwarning("uyarı","dikkatli olun")
def hatamesaji():
  messagebox.askquestion("onay","devam etmek istiyor musunuz")
def onaysor():
  cevap=messagebox.askquestion("onay","devam etmek istiyormusnuz")
  if cevap== "yes":
    print("evet seçildi")
  else:
    print("hayır seçildi")
def okcancel():
  cevap=messagebox.askokcancel("hata","bri ahta oluştu programı kapatmak istiyormusunuz")
  if cevap: # kullanıcı tamam a tıkladıysa porgramı kapat
      pencere.destroy()
  else:
    print("kullanıcı işlemi kapattı")
def yesno():
  cevap=messagebox.askyesno("soru","devam etmek isstiyormusunuz")
  if cevap:
    print("kullanıcı evet dedi")
  else:
    print("kullanıcı hayır dedi")

# butonlar oluştur

buton1= tk.Button(pencere, text="bilgi",command= bilgimesaji)
buton2= tk.Button(pencere,text="uayrı",command=uyarimesaji)
buton3= tk.Button(pencere,text="hata",command=hatamesaji)
buton4= tk.Button(pencere, text="onay sor",command=onaysor)
buton5= tk.Button(pencere,text="tamam mı?,devam mı?",command=okcancel)
buton6= tk.Button(pencere, text="evet-hayır",command=yesno)

# butonlaru yerleştir

buton1.pack()
buton2.pack()
buton3.pack()
buton4.pack()
buton5.pack()
buton6.pack()

pencere.mainloop()