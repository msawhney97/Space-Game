import pygame
from GameObject import GameObject


class Fuel(GameObject):
    def init():
        Fuel.fuelImage = pygame.transform.rotate(
        pygame.transform.scale(
        pygame.image.load("images/fuelstation.png").convert_alpha(),
        (75, 75)),0)

    def __init__ (self,x,y):
        super(Fuel, self). __init__(x,y,
            Fuel.fuelImage, 60)