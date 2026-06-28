dosya3=open("deneme.txt","r+")
print ("Dosya içindeki bilgi:",dosya3.read())
dosya3.write("Bu basit bir dosyadır.r+ açma kipi ile dosyanın sonuna yazılmıştır.")
dosya3.close()
