def rezervasyon_yap():
    rezervasyon_kapasitesi = 50
    dosya=open("Rezervasyon.txt","r+")
    rezervasyonlar = dosya.readlines()
    mevcut_rezervasyon = len(rezervasyonlar)
    if rezervasyon_kapasitesi - mevcut_rezervasyon >0 :
        print(rezervasyon_kapasitesi - mevcut_rezervasyon,"adet daha rezervasyon yapabiliriz")
        yeni_rezervasyon = input("Rezervasyon bilgilerini giriniz:")
        dosya.write("\n" + yeni_rezervasyon )
        print("Rezervasyon numaranız =",mevcut_rezervasyon+1)
        print("Rezervasyon bilgileriniz : ",yeni_rezervasyon)
        print("Razervasyonunuz başarıya tamamlanmıştır.")
    else:
        print("Rezervasyon kapasitemiz dolmuştur.")
        dosya.close()

print("Rezervasyon Ekranına Hoş Geldiniz")
rezervasyon_yap()
