'''
Ship.py

implements the Ship class, which defines the player controllable ship
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import math
from math import sin,cos,pi
from GameObject import GameObject


class Ship(GameObject):
    # we only need to load the image once, not for every ship we make!
    #   granted, there's probably only one ship...
    #modified
    @staticmethod
    def init(angle=-90):
        Ship.shipImage = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/newship.png').convert_alpha(),
            (30,50)), angle)
        #modified
    def __init__(self, x, y):
        super(Ship, self).__init__(x, y, Ship.shipImage, 30)
        self.power = 1
        self.drag = 0.9
        self.angleSpeed = 2
        self.angle =90 #rts pointing straight up
        self.maxSpeed = 20
        self.theta=0
    


    def update(self, screenWidth, screenHeight, theta, x, y, r,
        angle,flag):

        # theta+=0.1
        if flag==True:
            super(Ship, self). __init__(x + r*cos(theta),
                y + r*sin(theta), Ship.shipImage,30)
            Ship.init(angle)
        else:
            super(Ship, self). __init__(x,
                y,Ship.shipImage,30)
            Ship.init(angle)

        print('going')


        
    #Lukas's code
    def update2(self, dt, keysDown, screenWidth, screenHeight):
        if keysDown(pygame.K_LEFT):
            self.angle += self.angleSpeed

        if keysDown(pygame.K_RIGHT):
            # not elif! if we're holding left and right, don't turn
            self.angle -= self.angleSpeed

        if keysDown(pygame.K_UP):
            self.thrust(self.power)
        if keysDown(pygame.K_DOWN):
            self.thrust(-self.power)
        else:
            vx, vy = self.velocity
            self.velocity = self.drag * vx, self.drag * vy

        super(Ship, self).update(screenWidth, screenHeight)




#lukas
    def thrust(self, power):
        angle = math.radians(self.angle)
        vx, vy = self.velocity
        # distribute the thrust in x and y directions based on angle
        vx += power * math.cos(angle)
        vy -= power * math.sin(angle)
        speed = math.sqrt(vx ** 2 + vy ** 2)
        if speed > self.maxSpeed:
            factor = self.maxSpeed / speed
            vx *= factor
            vy *= factor
        self.velocity = (vx, vy)
