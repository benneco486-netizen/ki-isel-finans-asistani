dosya=open("istiklal.txt","r",encoding="utf-8")

# readlines ile içeriği liste olarak alacam
liste=dosya.readlines()

# listenin uzunluğunu hesaplayarak kaç satır olduğunu ekrana yazıyorum
print(len(liste))

#listenin 6. satırını ekrana yazıyorum
#listenin ilk satırının liste[0] olduğunu hatırlayın
print(liste[5])

#dosyada başa dönüyorum
dosya.seek(0)
# baştan sona satır satır okuyorum
for satır in range(len(liste)):
  print(dosya.readline())
dosya.close()
