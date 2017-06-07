import pygame
import math
from GameObject import GameObject

class Planet(GameObject):
	def init(self,path,r):
		Planet.planetImage = pygame.transform.rotate(
			pygame.transform.scale(
		pygame.image.load(path).convert_alpha(),
 		(r, r)),-90)

	
	def __init__(self,x,y,planetName,r=200, collR=100):
		self.type= planetName
		if self.type == "mars":
			path = "images/Mars.png"
		elif self.type== "neptune":
			path = "images/Neptune.png"
		elif self.type == "mercury":
			path = "images/venus.png"
		elif self.type == "uranus":
			path = "images/uranus.png"
		elif self.type == "earth":
			path = "images/earth.png"
		self.init(path,r)
		super(Planet, self). __init__(x,y,
			Planet.planetImage, collR)


	def update(self,level,x,y, r=200, collR=100):
		if level == 2:
			path = "images/earth2.png"
		elif level == 3:
			path = "images/earth3.png"
		self.init(path,r)
		super(Planet, self). __init__(x,y,
			Planet.planetImage, collR)





	def __str__(self):
		return ("%s") % self.type

