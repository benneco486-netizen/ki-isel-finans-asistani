with open("asal.txt","r") as dosya :
  veri=dosya.read()
  asal_sayilar=veri.split(" ")
print("Çıkış yapmak için 0 tuşuna basınız.")
while True:
  kontrol_sayisi=input("Asal olup olmadığını kontrol etmek istediğiniz sayıyı giriniz: ")
  if kontrol_sayisi == "0":
    print("çıkış yapıldı...")
    break
  elif kontrol_sayisi in asal_sayilar :
    print("Girdiğiniz asal sayıdır.")
  else:
    print("Girdiğiniz sayı asal değildir.")
