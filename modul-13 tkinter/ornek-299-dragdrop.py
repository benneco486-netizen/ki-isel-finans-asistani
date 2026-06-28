from tkinter import *
pencere = Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

def surukleBasla(event):
    bilesen = event.widget    #event.widget ile sürüklenen bileşene (etiket) erişilir.
    bilesen.baslaX = event.x  #etiket üzerindeki tıklama noktasının başlangıç konumunu saklar.x
    bilesen.baslaY = event.y  #etiket üzerindeki tıklama noktasının başlangıç konumunu saklar.y
def surukleHareket(event):
    bilesen = event.widget
    x = bilesen.winfo_x() - bilesen.baslaX + event.x #bilesen.winfo:etiketin pencereye göre mevcut konumunu verir.
    y = bilesen.winfo_y() - bilesen.baslaY + event.y #event.x ve event.y etiketin pencereye göre mevcut konumunu verir.
    bilesen.place(x=x,y=y)

etiket = Label(pencere,bg="red",fg="white",
    width=15,height=5,text="Sürükle Beni",
    font=20)
etiket.place(x=0, y=0)

etiket.bind("<Button-1>",surukleBasla)
etiket.bind("<B1-Motion>",surukleHareket)
pencere.mainloop()
