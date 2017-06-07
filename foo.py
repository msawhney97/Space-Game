import pygame

pygame.image.load("images/asteroidA.gif").convert_alpha()




# from math import asin, sin, cos, acos, degrees
# print(sin(50))
# print(sin(80))
# print(sin(-80))
# print(sin(-50))
# print(cos(50))
# print(cos(80))
# print(cos(-80))
# print(cos(-50))

# print(degrees(asin(1)))


# Actually implements the game
# Lukas Peraza, 2015 for 15-112 Pygame Lecture
# '''
# import pygame
# from Ship import Ship
# from Asteroid import Asteroid
# from Bullet import Bullet
# #from Explosion import Explosion
# from pygamegame import PygameGame
# import random


# class Game(PygameGame):
#     def init(self):
#         self.bgColor = (0, 0, 0)
#         Ship.init()
#         ship = Ship(self.width / 2, self.height / 2)
#         self.shipGroup = pygame.sprite.GroupSingle(ship)

#         Asteroid.init()
#         self.asteroids = pygame.sprite.Group()
#         for i in range(5):
#             x = random.randint(0, self.width)
#             y = random.randint(0, self.height)
#             self.asteroids.add(Asteroid(x, y))

#         self.bullets = pygame.sprite.Group()

#         Explosion.init()
#         self.explosions = pygame.sprite.Group()

#     def keyPressed(self, code, mod):
#         if code == pygame.K_SPACE:
#             ship = self.shipGroup.sprites()[0]
#             self.bullets.add(Bullet(ship.x, ship.y, ship.angle))

#     def timerFired(self, dt):
#         self.shipGroup.update(dt, self.isKeyPressed, self.width, self.height)
#         self.asteroids.update(self.width, self.height)
#         self.bullets.update(self.width, self.height)
#         self.explosions.update(dt)

#         ship = self.shipGroup.sprite

#         if ((not ship.isInvincible()) and
#              pygame.sprite.groupcollide(
#              self.shipGroup, self.asteroids, False, False,
#              pygame.sprite.collide_circle)):

#             self.explosions.add(Explosion(ship.x, ship.y))
#             self.shipGroup.add(Ship(self.width / 2, self.height / 2))

#         for asteroid in pygame.sprite.groupcollide(
#             self.asteroids, self.bullets, True, True,
#             pygame.sprite.collide_circle):
#             self.asteroids.add(asteroid.breakApart())

#     def redrawAll(self, screen):
#         self.shipGroup.draw(screen)
#         self.asteroids.draw(screen)
#         self.bullets.draw(screen)
#         self.explosions.draw(screen)

# Game(800, 500).run()


# implements the Ship class, which defines the player controllable ship
# Lukas Peraza, 2015 for 15-112 Pygame Lecture
# '''
# import pygame
# import math
# from GameObject import GameObject


# class Ship(GameObject):
#     # we only need to load the image once, not for every ship we make!
#     #   granted, there's probably only one ship...
#     @staticmethod
#     def init():
#         Ship.shipImage = pygame.transform.rotate(pygame.transform.scale(
#             pygame.image.load('images/spaceship.png').convert(),
#             (60, 100)), -90)

#     def __init__(self, x, y):
#         super(Ship, self).__init__(x, y, Ship.shipImage, 30)
#         self.power = 1
#         self.drag = 0.9
#         self.angleSpeed = 5
#         self.angle = 0  # starts pointing straight up
#         self.maxSpeed = 20
#         self.invincibleTime = 1500
#         self.timeAlive = 0
#         self.image.set_alpha(100)

#     def update(self, dt, keysDown, screenWidth, screenHeight):
#         self.timeAlive += dt

#         if keysDown(pygame.K_LEFT):
#             self.angle += self.angleSpeed

#         if keysDown(pygame.K_RIGHT):
#             # not elif! if we're holding left and right, don't turn
#             self.angle -= self.angleSpeed

#         if keysDown(pygame.K_UP):
#             self.thrust(self.power)
#         else:
#             vx, vy = self.velocity
#             self.velocity = self.drag * vx, self.drag * vy

#         super(Ship, self).update(screenWidth, screenHeight)

#         if self.isInvincible():
#             self.image.set_alpha(100)
#         else:
#             self.image.set_alpha(255)

#     def thrust(self, power):
#         angle = math.radians(self.angle)
#         vx, vy = self.velocity
#         # distribute the thrust in x and y directions based on angle
#         vx += power * math.cos(angle)
#         vy -= power * math.sin(angle)
#         speed = math.sqrt(vx ** 2 + vy ** 2)
#         if speed > self.maxSpeed:
#             factor = self.maxSpeed / speed
#             vx *= factor
#             vy *= factor
#         self.velocity = (vx, vy)

#     def isInvincible(self):
#         return self.timeAlive < self.invincibleTime













