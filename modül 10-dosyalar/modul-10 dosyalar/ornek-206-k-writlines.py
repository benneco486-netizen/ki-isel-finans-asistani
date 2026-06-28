dosya=open("deneme.txt","r+")
#listedeki veriler string olmazsa hata alırız.
liste=["1","2","3","4"]
dosya.writelines(liste)
dosya.close()
