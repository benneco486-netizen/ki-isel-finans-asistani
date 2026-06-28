import tkinter as tk
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

liste = tk.Listbox(pencere,
                   selectmode=tk.MULTIPLE)  
                   #kullanıcılar birden fazla öğe seçebilir
liste.insert(0, "Python")
liste.insert(1, "Java")
liste.insert(2, "C#")
liste.insert(3, "R")
liste.insert(4, "C++")

liste.place(x=5, y=5)

def listeOgeleri():
    liste_indeks = liste.curselection()
    print(liste_indeks)
    for i in liste_indeks:
        print(liste.get(i))

buton = tk.Button(pencere,
                  text="Seç",
                  command=listeOgeleri)
buton.place(x=10, y=175)

pencere.mainloop()