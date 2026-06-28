def rezervasyon_sil(rezervasyon_no):
    dosya=open("Rezervasyon.txt","r+")
    rezervasyonlar=dosya.readlines()
    if rezervasyon_no < len(rezervasyonlar):
        print("Rezervasyon bilgileriniz: ",rezervasyonlar[rezervasyon_no])
        emin_misiniz=input("Kaydı silmek istediğinizden emin misiniz e/h")
        if emin_misiniz=="e" or emin_misiniz=="E":
            rezervasyonlar.pop(rezervasyon_no)
            dosya.seek(0)
            dosya.writelines(rezervasyonlar)
            dosya.close()
            print("Rezervasonunuz başarıyla silinmiştir.")
        else:
            print("Rezervasyon silme işleminiz iptal edilmiştir")
    else:
        print("Hatalı bir rezervason numarası girdiniz")

print("Rezervasyon silme ekranına hoşgeldiniz")
rezervasyon_no=int(input("Lütfen rezervasyon numaranızı giriniz"))
rezervasyon_no-=1
rezervasyon_sil(int(rezervasyon_no))
