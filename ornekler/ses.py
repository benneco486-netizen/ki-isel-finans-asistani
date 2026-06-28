import pygame
import time

pygame.init()
pygame.mixer.init()

# Dosya yolu
dosya_yolu = "C:/Users/Vektorel/Desktop/Yeni klasör/muzik.wav"

# Dosya açılıp okunabiliyor mu kontrol et
with open(dosya_yolu, "rb") as muzik_dosyasi:
    pygame.mixer.music.load(dosya_yolu)
    pygame.mixer.music.play()

    # Müzik bitene kadar bekle
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # CPU'yu yormamak için bekleme ekliyoruz
