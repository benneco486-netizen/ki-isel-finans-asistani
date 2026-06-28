import sys
import tkinter
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title('Masaüstü Hava Durumu Uygulaması')
        self.win.geometry('520x200')
        #self.win.iconbitmap('./img/main_icon.ico')
        self.apikey = '1716b90ca82052701509df676f664807'

    def getdata_exec(self,sehir):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (sehir, self.apikey)).json()
        if r['cod'] == '200' or r['cod'] == 200:
            data = (r['weather'][0]['description'], r['weather'][0]['icon'][2:], (r['sys']['country'], r['name']), float(r['main']['temp'])-273.15)
            self.label_2 = tkinter.Label(text='Konum: ')
            self.label_3 = tkinter.Label(text='%s / %s' % (data[2][0] , data[2][1]))
            self.label_4 = tkinter.Label(text='Sıcaklık: ')
            self.label_5 = tkinter.Label(text='%f °C' % data[3])
            self.label_2.grid(row=1, column=0)
            self.label_3.grid(row=1, column=1)
            self.label_4.grid(row=2, column=0)
            self.label_5.grid(row=2, column=1)

            parcali_bulut = ['few clouds', 'broken clouds', 'scattered clouds','overcast clouds']
            yagmurlu = ['shower rain', 'rain', 'light rain', 'light intensity shower rain']
            saganak = ['thunderstorm', 'thunderstorm with light rain']
            karlı = ['snow', 'light snow']
            temiz = ['clear sky','light intensity drizzle']
            #sisli = 'mist'

            if data[0] in parcali_bulut:    #parcali_bulutlu
                self.label_6 = tkinter.Label(text='Açıklama:')
                self.label_7 = tkinter.Label(text='Parçalı/hafif bulutlu')
                self.label_6.grid(row=3, column=0)
                self.label_7.grid(row=3, column=1)
                if data[1] == 'd':
                    self.gorsel = Image.open('s_parcali_bulut.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
                else:
                    self.gorsel = Image.open('g_parcali_bulut.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)

            elif data[0] in yagmurlu: #yagmurlu
                self.label_6 = tkinter.Label(text='Açıklama:')
                self.label_7 = tkinter.Label(text='Orta/hafif yağmurlu')
                self.label_6.grid(row=3, column=0)
                self.label_7.grid(row=3, column=1)
                if data[1] == 'd':
                    self.gorsel = Image.open('s_yagmurlu.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)

                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
                else:
                    self.gorsel = Image.open('g_yagmurlu.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
            elif data[0] in saganak: #saganak
                self.label_6 = tkinter.Label(text='Açıklama:')
                self.label_7 = tkinter.Label(text='Sağanak yağış')
                self.label_6.grid(row=3, column=0)
                self.label_7.grid(row=3, column=1)
                if data[1] == 'd':
                    self.gorsel = Image.open('saganak.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
                else:
                    self.gorsel = Image.open('saganak.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
            elif data[0] in karlı: #karlı
                self.label_6 = tkinter.Label(text='Açıklama:')
                self.label_7 = tkinter.Label(text='Karlı')
                self.label_6.grid(row=3, column=0)
                self.label_7.grid(row=3, column=1)
                if data[1] == 'd':
                    self.gorsel = Image.open('karli.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
                else:
                    self.gorsel = Image.open('karli.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
            elif data[0] in temiz: #temiz hava
                self.label_6 = tkinter.Label(text='Açıklama:')
                self.label_7 = tkinter.Label(text='Açık/temiz gökyüzü')
                self.label_6.grid(row=3, column=0)
                self.label_7.grid(row=3, column=1)
                if data[1] == 'd':
                    self.gorsel = Image.open('s_temiz.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
                else:
                    self.gorsel = Image.open('g_temiz.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
            elif data[0] == 'mist': #sisli
                self.label_6 = tkinter.Label(text='Açıklama:')
                self.label_7 = tkinter.Label(text='Sisli')
                self.label_6.grid(row=3, column=0)
                if data[1] == 'd':
                    self.gorsel = Image.open('sisli.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
                else:
                    self.gorsel = Image.open('sisli.png')
                    self.panel = ImageTk.PhotoImage(self.gorsel)
                    self.label_8 = tkinter.Label(text='Durum: ')
                    self.label_9 = tkinter.Label(self.win, image=self.panel)
                    self.label_8.grid(row=4, column=0)
                    self.label_9.grid(row=4, column=1)
            else:
                print (data[0])
        elif r['cod'] == '404':
            messagebox.showinfo('Hata' , 'Öyle bir şehir yok.')
        elif r['cod'] == '401' or r['cod'] == 401:
            messagebox.showinfo('Hata', 'API key hatalı ve ya süresi doldu.')
        elif r['cod'] == '400':
            messagebox.showinfo('Hata' , 'Herhangi bir mekan verilmedi.')

    def build(self):
        self.label_1 = tkinter.Label(text='Aranacak bölge ve ya şehir giriniz:')
        self.entry_1 = tkinter.Entry()
        self.button_1 = tkinter.Button(text='ARA', command=lambda: self.getdata_exec(self.entry_1.get()))

        self.button_1.config(width=10)

        self.label_1.grid(row=0, column=0)
        self.entry_1.grid(row=0, column=1)
        self.button_1.grid(row=0, column=2, padx=5)


    def run(self):
        self.build()
        self.win.mainloop()

if __name__ == '__main__':
    main = App()
    sys.exit(main.run())