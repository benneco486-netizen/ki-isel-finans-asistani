def rezervasyon_guncelle(rezervasyon_no):
    dosya=open("Rezervasyon.txt","r+")
    rezervasyonlar=dosya.readlines()
    if rezervasyon_no < len(rezervasyonlar):
        print("\n Rezervason bilgileriniz: ",rezervasyonlar[rezervasyon_no])
        guncelleme=input("Lütfen rezervasyon güncelleme bilgilerini giriniz")
        rezervasyonlar[rezervasyon_no]= guncelleme +"\n"
        print("Güncel rezervason bilgileriniz: ",rezervasyonlar[rezervasyon_no])
        dosya.seek(1)
        dosya.writelines(rezervasyonlar)
        dosya.close()
        print("Rezervasonunuz başarıyla güncellenmişitir.")
    else:
        print("Hatalı bir rezervason numarası girdiniz")

print("Rezervasyon güncelleme ekranına hoş geldiniz")
rezervasyon_no=int(input("lütfen rezervasyon numaranızı giriniz:"))
rezervasyon_no-=1
rezervasyon_guncelle (int(rezervasyon_no))
