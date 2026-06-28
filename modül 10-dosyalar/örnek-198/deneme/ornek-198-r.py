dosya = open ("deneme.txt","r",encoding="utf-8")
belge=dosya.read()
print ("Dosya içindeki bilgi şu:",belge)
dosya.close
