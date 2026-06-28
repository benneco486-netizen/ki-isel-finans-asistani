import tkinter as tk
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Check Button Örneği")

def gonderFonksiyonu():
    python_secildi = python_onay.get()
    java_secildi = java_onay.get()
    csharp_secildi = csharp_onay.get()

    if python_secildi == 1:
        print("Python seçildi.")
    else:
        print("Python seçilmedi.")

    if java_secildi == 1:
        print("Java seçildi.")
    else:
        print("Java seçilmedi.")

    if csharp_secildi == 1:
        print("C# seçildi.")
    else:
        print("C# seçilmedi.")

# Her bir Checkbutton için ayrı IntVar oluşturma
python_onay = tk.IntVar()
java_onay = tk.IntVar()
csharp_onay = tk.IntVar()

# Başlangıçta hiçbirinin seçili olmaması için değerleri 0 yapma
python_onay.set(0)
java_onay.set(0)
csharp_onay.set(0)

# Python Checkbutton'ını oluşturma ve değişkene atama
checkbutton_python = tk.Checkbutton(pencere, text="Python", variable=python_onay, command=gonderFonksiyonu)
checkbutton_python.place(x=100, y=100)

# Java Checkbutton'ını oluşturma ve değişkene atama
checkbutton_java = tk.Checkbutton(pencere, text="Java", variable=java_onay, command=gonderFonksiyonu)
checkbutton_java.place(x=100, y=150)

# C# Checkbutton'ını oluşturma ve değişkene atama
checkbutton_csharp = tk.Checkbutton(pencere, text="C#", variable=csharp_onay, command=gonderFonksiyonu)
checkbutton_csharp.place(x=100, y=200)

pencere.mainloop()