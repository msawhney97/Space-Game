'''
Asteroid.py

implements the Asteroid class
Lukas Peraza, 2015 for 15-112 Pygame Lecture

Mostly unmodified
'''
import pygame
import random
from random import randint
from GameObject import GameObject


class Asteroid(GameObject):
    @staticmethod
    def init():

        Asteroid.images = []
        for asteroid in range(1):
            r=random.randint(30,90)
            image = pygame.transform.scale(
                pygame.image.load("images/asteroidb.png").convert_alpha(),
                (r, r))
            Asteroid.images.append(image)

    minSize = 2
    maxSize = 6
    maxSpeed = 3
    #slightly modified

    def __init__ (self,x,y,level = None):
        Asteroid.init()
        if level==None:
            level = randint(Asteroid.minSize, Asteroid.maxSize) 
        self.level = level
        asteroid = random.choice(Asteroid.images)
        super(Asteroid, self).__init__(x, y, asteroid, 40)
        self.angleSpeed = random.randint(-10, 10)
        x = 0
        y = random.randint(1, 2)
        self.velocity = x, y

        
    def update(self, screenWidth, screenHeight):
        self.angle += self.angleSpeed
        super(Asteroid, self).update(screenWidth, screenHeight)
        if self.y>700: self.kill()

    def destroy(self):
        if self.level == Asteroid.minSize:
            return []
        else:
            return [Asteroid(self.x, self.y, self.level - 1)]
