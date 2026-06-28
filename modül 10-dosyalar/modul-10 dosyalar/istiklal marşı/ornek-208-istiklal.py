dosya=open("istiklal.txt","r+",encoding="utf-8")

# readlines ile içeriği liste olarak alacam
liste=dosya.readlines()
print(len(liste))

# her 4 kıtadan sonra araya bir satır çizgi ekliyoruz
# listeye 4 satırda bir ek satır eklediğimden beşer beşer ilerleyeceğim
eklenecek_satır=30 * "-" + "\n"
for ekle in range(4,52,5):
  liste.insert(ekle,eklenecek_satır)

# dosyada başa gelecem
dosya.seek(0)

# çizgi eklenmiş listeyi yazdıracağım
dosya.writelines(liste)
dosya.seek(0)
yeni_liste=dosya.readlines()
print(yeni_liste)

dosya.close()
