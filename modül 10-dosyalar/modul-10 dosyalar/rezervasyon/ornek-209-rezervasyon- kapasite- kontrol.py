dosya=open("Rezervasyon.txt","r+")
rezervasyonlar=dosya.readlines()  #rezervasyonlar = ["Nejdet TUT","İrem Burcu Orhan"....]
rezervasyon_kapasitesi = 50
sıra_no=0
i=1
for rezervasyon_sahibi in rezervasyonlar:
  print(i,"nolu rezervasyon sahibi",rezervasyon_sahibi)
  sıra_no+=1
  i+=1
print("Toplam",sıra_no,"adet rezervasyon var")

if rezervasyon_kapasitesi - sıra_no > 0:
  print(rezervasyon_kapasitesi-sıra_no,"adet daha rezervasyon yapabiliriz")
else:
  print("Rezervasyon kapasitemiz dolmuştur.")

dosya.close ()
