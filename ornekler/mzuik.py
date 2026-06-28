import pygame
import time
pygame.init()
pygame.mixer.init()
# dosya yolu
dosyayolu="Z://NEJDET TUT//python//dosyalar//muzik.mp3"
#dosya açılıp ounabiliyor mu kontrol et
with open(dosyayolu,"rb")as muzik_dosyasi:
  pygame.mixer.music.load(dosyayolu)
  pygamea.mixer.music.play()

  # mğüz,k kadar bekle 
  while pygame.mixer.music.get_busy():
    time.sleep(0.1) #CPUYu yormamak için bekleme ekliyoruz
