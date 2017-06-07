import pygame
import math
from GameObject import GameObject

class Sun(GameObject):
	@staticmethod
	def init():
		Sun.SunImage = pygame.transform.rotate(
			pygame.transform.scale(
		pygame.image.load('images/Render_Sun.png').convert_alpha(),
		(150, 150)),-90)
	def __init__(self,x,y):
		super(Sun, self). __init__(x,y,
			Sun.SunImage, 20)
	