import pygame 
from math import sin, cos
from GameObject import GameObject

class Moon(GameObject):
	@staticmethod
	def init(angle=90):
		Moon.moonImage = pygame.transform.rotate(
			pygame.transform.scale(
		pygame.image.load('images/cartoon-moon.png').convert_alpha(),
		(100, 100)),angle)

	def __init__(self,x,y):
		super(Moon,self). __init__(x,y,
			Moon.moonImage, 20)	
	def update(self,x,y, r,angle):
		super(Moon, self). __init__(x, 
			y, Moon.moonImage,30)
		Moon.init(angle)
