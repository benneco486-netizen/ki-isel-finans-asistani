def rezervasyon_yap():
  rezervasyon_bilgi=input("Rezervasyon kayıt bilgilerinizi giriniz:")
  veri = rezervasyon_bilgi + "\n"
  dosya=open("Rezervasyon.txt","a")
  dosya.write(veri)
  dosya.close()

def rezervasyon_kontrol() :
  rezervasyon_bilgi=input("Kontrol için Rezervasyon bilgilerinizi giriniz:")
  with open("Rezervasyon.txt","r") as dosya:
    veri=dosya.read()
    rezervasyonlar=veri.split("\n")
    if rezervasyon_bilgi in rezervasyonlar:
      print("Rezervasyonunuz bulunmaktadır.")
    else:
      print("Rezervasyon kaydınız yoktur.")

while True:
  islem=input("Rezervasyon yapmak için 1, kontrol etmek için 2, programı kapatmak için 3 tuşuna basınız:")
  if islem == "1" :
    rezervasyon_yap()
  elif islem =="2":
    rezervasyon_kontrol()
  elif islem =="3":
    print("Çıkış Yapıldı...")
    break
  else:
    print("Geçersiz işlem...")
    continue
