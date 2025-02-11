#Tocando música mp3

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load('C:/Users/rdavi/OneDrive/ESTUDOS/PYTHON/Exercicio.021/ex21.mp3')
pygame.mixer.music.play(loops=-1, start=0.0)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
