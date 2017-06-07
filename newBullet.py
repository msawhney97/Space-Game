import pygame
import math
from math import cos,sin,radians,degrees,pi
from GameObject import GameObject



class Missile(GameObject):

    def init(self,path,r,theta=0):
        Missile.missileImage = pygame.transform.rotate(
            pygame.transform.scale(
        pygame.image.load(path).convert_alpha(),
        (r, r)),theta)

    def __init__(self,x,y,angle):
        self.dir = 20
        self.init( "images\missile.png", 20,angle)
        self.size = 20
        angle= radians(angle)
        super(Missile,self). __init__ (x,y,Missile.missileImage,20)
        self.missileX = self.dir *cos(angle)
        self.missileY= -self.dir * sin(angle)
        self.velocity = self.missileX, self. missileY
        self.timeOnScreen=0


    def update(self, screenWidth, screenHeight):
        super(Missile, self).update(screenWidth, screenHeight)
        self.timeOnScreen += 1
        if self.y < 0 or self.y > screenHeight or self.x < 0 or self.x > screenWidth:
            self.kill()