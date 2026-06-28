import tkinter as tk
pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulama Hoş Geldiniz!")

def butonFonksiyonu():
    etiket.config(text="Nasılsın?", # config=etiketin ayarlarını güncelle yada değiştir.
                  bg="red",
                  font="Verdana" )

    yazdigin_sey = giris.get()        # entry yazılan değeri değişkene aktarır
    etiket.config(text=yazdigin_sey)
    giris.config(state="normal")      #disabled ile entry tek veri girişi yapılır
                                      #normal ile birden fazla veri girişi yapılır
buton = tk.Button(
    pencere,
    text="Ben Bir Butonum",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    height=5,
    width=20,
    cursor="hand2",
    command= butonFonksiyonu)
buton.pack()

etiket = tk.Label(
    pencere,
    text="Ben Bir Etiketim",
    font="Tahoma 24",
    bg="blue",
    fg="white",
    wraplength=150)
etiket.pack(pady=10)

giris = tk.Entry(pencere,width=50)
metin="Kafanıza göre bir şeyler yazın..."
giris.insert(string=metin,index=0)
giris.pack()

def metin_sil(event):
    if giris.get() == metin:
        giris.delete(0, tk.END)
        giris.unbind("<FocusIn>", focus)

focus = giris.bind("<FocusIn>", metin_sil)

pencere.mainloop()