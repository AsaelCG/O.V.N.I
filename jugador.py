#aqui tendrá toda la jugabilidad, controles, vidas. se me acaba de ocurrir, que para el 3°
# nivel goku se convierta en ssj y con ese derrote a freezer. 
from main import *
import pygame

class Jugador():
    def __init__(self):
        self.__salud = 100
        self.__puntuacion = 0
    
    def controles (self, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and goku_rect.left > -35:
            goku_rect.x -= 5
        if keys[pygame.K_RIGHT] and goku_rect.right < 815:
            goku_rect.x += 5
        if keys[pygame.K_UP] and goku_rect.top > 0:
            goku_rect.y -= 5
        if keys[pygame.K_DOWN] and goku_rect.bottom < 630:
            goku_rect.y += 5
        if keys[pygame.K_SPACE]:
            pygame.draw.circle(window, BLUE, (400, 300), 50)

    def danio (self, danio):
        self.__salud -= danio
    
    @property
    def puntuacion (self):
        return self.__puntuacion
    
    @property
    def salud (self):
        return self.__salud
    
    def sumar_puntos(self, puntos):
        self.__puntuacion += puntos
    
    def convertirse(self):
        #aqui tiene que transformarse cuando se cambie de nivel
        pass