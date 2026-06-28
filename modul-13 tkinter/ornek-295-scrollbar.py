#yatay kaydırma çubuğu
import tkinter as tk
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

metin = tk.Text(pencere,
    wrap=tk.NONE)
metin.pack(fill=tk.BOTH, expand=True) #Metin kutusu çerçeveye yerleştirilir ve tüm kullanılabilir alanı kaplar.

kaydirma_cubugu = tk.Scrollbar(metin, orient=tk.HORIZONTAL, command=metin.xview)
kaydirma_cubugu.pack(side=tk.BOTTOM, fill=tk.X)

metin.config(xscrollcommand=kaydirma_cubugu.set)

def metinFonksiyonu():
    print(metin.get(1.0, tk.END)) #Metni ilk karakterden son karaktere kadar alır.1 satırı,0 karakteri temsil eder.

buton = tk.Button(pencere, text="Kaydet", command=metinFonksiyonu)
buton.pack(pady=10)

pencere.mainloop()
