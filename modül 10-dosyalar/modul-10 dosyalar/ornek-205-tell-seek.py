dosya=open("deneme.txt","r")

# dosyamızı for döngüsü ile okuruz. tüm veri okunur.
for veri in dosya:
  print("İçindeki Veri:",veri)
print("-"*20)

#imlecin nerede olduğunu ekrana yazdırılır.son kaldığı yer söyler.
print("İmlecin son kaldığı byte sayısı:",dosya.tell())
print("-"*20)

# imleci 15. bayta taşıyoruz
dosya.seek(15)
#imlecin bulunduğu yerden 20 bayt veri okuyoruz
print(dosya.read(20))
print("-"*20)

#imlecin nerede olduğunu görüntülüyoruz
print("İmlecin son kaldığı byte sayısı:",dosya.tell())

dosya.close()
