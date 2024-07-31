#El juego va a comenzar con una pantalla inicial que diga: presiona cualquier tecla para 
#continuar, cuando la presione, comenzará el juego al instante.  

#1.importar paqueteria
import pygame, random
import sys
from jugador import *

#2.definir constantes
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

#3.Iniciamos el mundo
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#4.cargamos recursos: imgs, sonidos, etc
goku = pygame.image.load('sources/images/goku.png')
gokussj = pygame.image.load('sources/images/gokussj.png')
laser_corto = pygame.mixer.Sound('sources/sounds/laser_corto.mp3')
laser_continuo = pygame.mixer.Sound ('sources/sounds/laser_continuo.mp3')
canon_laser = pygame.mixer.Sound ('sources/sounds/canon_laser.mp3')
fondo = pygame.image.load('sources/images/abduccion_fondo.png').convert()
goku_rect = goku.get_rect()
goku_rect.center = (400, 515)



#5. Inicializamos variables

#Loop por siempre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    window.fill (BLACK)
    window.blit(goku, goku_rect)
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)


    






