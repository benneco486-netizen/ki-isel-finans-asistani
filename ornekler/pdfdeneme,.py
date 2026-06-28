import PyPDF2
with open("dokuman.pdf","rb")as dosya:
  okuyucu=PyPDF2.PdfReader(dosya)
  sayfa=okuyucu.pages[0]
  print(sayfa.extract_text())
