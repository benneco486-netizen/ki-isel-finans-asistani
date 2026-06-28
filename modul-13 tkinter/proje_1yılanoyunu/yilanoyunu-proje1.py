import tkinter as tk
import random

# Oyun ayarları
GRID_SIZE = 20
OYUN_GENISLIGI = 600
OYUN_YUKSEKLIGI = 480
YILAN_RENGI = "green"
YEM_RENGI = "red"
ARKA_PLAN_RENGI = "black"
YILAN_BASLANGIC_UZUNLUGU = 3
HAREKET_HIZI = 150  # Milisaniye cinsinden gecikme

class YilanOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("Yılan Oyunu")

        self.yon = "right"
        self.yilan_vucudu = []
        # Yılan başlangıç pozisyonunu doğru şekilde oluştur
        for i in range(YILAN_BASLANGIC_UZUNLUGU):
            self.yilan_vucudu.append((100 - i * GRID_SIZE, 100))

        self.yem_pozisyonu = self.yem_olustur()
        self.oyun_devam_ediyor = True

        self.canvas = tk.Canvas(self.root, bg=ARKA_PLAN_RENGI, width=OYUN_GENISLIGI, height=OYUN_YUKSEKLIGI)
        self.canvas.pack()

        self.skor = 0
        self.skor_etiketi = tk.Label(self.root, text=f"Skor: {self.skor}", font=("Arial", 16))
        self.skor_etiketi.pack()

        # Yılan parçalarını tutacak liste
        self.yilan_parcalari = []

        # Oyunu başlat
        self.yemi_ciz()
        self.yilani_ciz()
        self.hareketi_baslat()

        # Klavye olaylarını bağlama
        self.root.bind("<Up>", lambda event: self.yon_degistir("up"))
        self.root.bind("<Down>", lambda event: self.yon_degistir("down"))
        self.root.bind("<Left>", lambda event: self.yon_degistir("left"))
        self.root.bind("<Right>", lambda event: self.yon_degistir("right"))

    def yem_olustur(self):
        while True:
            x = random.randrange(0, OYUN_GENISLIGI // GRID_SIZE) * GRID_SIZE
            y = random.randrange(0, OYUN_YUKSEKLIGI // GRID_SIZE) * GRID_SIZE
            if (x, y) not in self.yilan_vucudu:
                return (x, y)

    def yemi_ciz(self):
        self.canvas.delete("yem")  # Önceki yemi sil
        x, y = self.yem_pozisyonu
        self.canvas.create_oval(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=YEM_RENGI, tag="yem")

    def yilani_ciz(self):
        self.canvas.delete("yilan")  # Önceki yılanı sil

        for x, y in self.yilan_vucudu:
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=YILAN_RENGI, tag="yilan")

    def yon_degistir(self, yeni_yon):
        if yeni_yon == "up" and self.yon != "down":
            self.yon = yeni_yon
        elif yeni_yon == "down" and self.yon != "up":
            self.yon = yeni_yon
        elif yeni_yon == "left" and self.yon != "right":
            self.yon = yeni_yon
        elif yeni_yon == "right" and self.yon != "left":
            self.yon = yeni_yon

    def hareketi_baslat(self):
        if self.oyun_devam_ediyor:
            self.yilan_hareket_et()
            self.root.after(HAREKET_HIZI, self.hareketi_baslat)

    def yilan_hareket_et(self):
        kafa_x, kafa_y = self.yilan_vucudu[0]

        if self.yon == "up":
            yeni_kafa = (kafa_x, kafa_y - GRID_SIZE)
        elif self.yon == "down":
            yeni_kafa = (kafa_x, kafa_y + GRID_SIZE)
        elif self.yon == "left":
            yeni_kafa = (kafa_x - GRID_SIZE, kafa_y)
        elif self.yon == "right":
            yeni_kafa = (kafa_x + GRID_SIZE, kafa_y)

        self.yilan_vucudu.insert(0, yeni_kafa)

        if yeni_kafa == self.yem_pozisyonu:
            self.skor += 10
            self.skor_etiketi.config(text=f"Skor: {self.skor}")
            self.yem_pozisyonu = self.yem_olustur()
            self.yemi_ciz()
        else:
            self.yilan_vucudu.pop()

        self.yilani_ciz()
        self.carpismayi_kontrol_et()

    def carpismayi_kontrol_et(self):
        kafa_x, kafa_y = self.yilan_vucudu[0]

        # Duvar çarpışması
        if kafa_x < 0 or kafa_x >= OYUN_GENISLIGI or kafa_y < 0 or kafa_y >= OYUN_YUKSEKLIGI:
            self.oyunu_bitir()

        # Kendine çarpma
        if len(self.yilan_vucudu) > 1 and self.yilan_vucudu[0] in self.yilan_vucudu[1:]:
            self.oyunu_bitir()

    def oyunu_bitir(self):
        self.oyun_devam_ediyor = False
        self.canvas.create_text(OYUN_GENISLIGI // 2, OYUN_YUKSEKLIGI // 2,
                               text=f"Oyun Bitti! Skor: {self.skor}", fill="white", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    oyun = YilanOyunu(root)
    root.mainloop()
