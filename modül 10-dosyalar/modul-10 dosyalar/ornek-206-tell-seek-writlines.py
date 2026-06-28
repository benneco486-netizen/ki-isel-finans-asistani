dosya=open("deneme.txt","r+")
#dosyada 26. bayta gittik
dosya.seek(26)

#26. bayttan sonraki verilerin üzerine yazdık
dosya.write("26. bayttan itibaren bu yazıyı yazdık")

# imlecin 63. bayta geldiğini öğreneceğiz
#burda dosyadan okuma yaparsak 63. bayttan sonrası okunacak
print(dosya.tell())

# listemizdeki verileri en sona yazıyoruz
print(dosya.read())
dosya.close()
