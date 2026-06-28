import tkinter as tk
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

def dosyaFonksiyonu():
    print("Yeni Dosya")
def dosyaAc():
    print("Dosya Aç")
def kaydet():
    print("Kaydet")
def kaynakFonksiyonu():
    print("Veri")
def degerFonksiyonu():
    print("Değer")
def grafikFonksiyonu():
    print("Grafik")
def undo():
    print("Geri Al")
def redo():
    print("İleri Al")
def findchange():
    print("Bul ve Değiştir")
def kaydetveac():
    print("Kaydet ve Aç")
def about():
    print("Hakkında")


menu_cubugu = tk.Menu(pencere)
pencere.config(menu=menu_cubugu)

dosya = tk.Menu(menu_cubugu, tearoff=False)  #tearoff=False:menü sürekli menü çubuğuna bağlı kalır
kaynak = tk.Menu(menu_cubugu, tearoff=False) #tearoff=true:menü farklı pencereye taşınır
edit = tk.Menu(menu_cubugu, tearoff=False)
help = tk.Menu(menu_cubugu, tearoff=False)

menu_cubugu.add_cascade(label="Dosya", menu=dosya) #add_cascade ile bir menüye alt menü eklemek için kullanılır.
menu_cubugu.add_cascade(label="Kaynak", menu=kaynak)
menu_cubugu.add_cascade(label="Düzenle", menu=edit)
menu_cubugu.add_cascade(label="Yardım", menu=help)

dosya.add_command(label="Yeni Dosya", command=dosyaFonksiyonu)
dosya.add_command(label="Aç", command=dosyaAc)
dosya.add_command(label="Kaydet",command=kaydet)
dosya.add_command(label="Kaydet ve Aç", command=kaydetveac)
dosya.add_command(label="Çıkış", command=pencere.destroy)

kaynak.add_command(label="Veri", command=kaynakFonksiyonu)
kaynak.add_command(label="Değer", command=degerFonksiyonu)
kaynak.add_command(label="Grafik", command=grafikFonksiyonu)

edit.add_command(label="Geri Al", command=undo)
edit.add_command(label="İleri Al", command=redo)
edit.add_command(label="Bul ve Değiştir", command=findchange)

help.add_command(label="Hakkında", command=about)

pencere.mainloop()
