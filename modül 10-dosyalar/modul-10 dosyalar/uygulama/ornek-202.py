asal_sayi=[2]
for sayi in range (3,1001):
  for bolen_sayi in range (2,sayi):
    sayi_asalmi=False
    if sayi % bolen_sayi==0:
      sayi_asalmi=True
      break
  if sayi_asalmi==False:
    asal_sayi.append(sayi)
veri=" "
for i in asal_sayi:
  veri+=str(i)           # veri=veri+str(i)
  veri+=" "

dosya = open ("asal.txt","w")
dosya.write(veri)
dosya.close()
