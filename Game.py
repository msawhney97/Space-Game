'''
Game.py

Actually implements the game
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import math
import pygame
from Ship import Ship
from pygamegame import PygameGame
from Planet import Planet
from Moon import Moon
from math import sin, cos, pi,asin,acos, degrees
from sun import Sun
from newBullet import Missile
from Asteroid import Asteroid
from Fuel import Fuel
import random
from movingStars import Stars
from random import randint, randrange, choice


#CITED PART OF THE CODE HAS BEEN MARKED
#LEVEL1 AND 2 CONTAIN ONLY INITIALIZATIONS, 3 USES LUKAS'S MODULE
#NO OYGAME MODULES USED EXCEPT FOR COLLISION DETECTION FOR WHEN
#SHIP CRASHES INTO OBJECTS



class Game(PygameGame):
    def init(self,level=3):
        self.level=level
        self.theta=0
        self.angle=360
        self.shipFlag=True
        self.instructions=False
        self.lev2ins = False
        self.lev3ins=False
        self.screen3=False
        self.maxStars = 260
        self.starSpeedX, self.starSpeedY = None,None
        self.stars= Stars.listAllStars(self.width,self.height)
        if self.level==1:
            self.level1init()
        elif self.level==2:
            self.level2init()
        elif self.level == 3:
            self.level3init()
        self.initIns()
        self.initButtons()


    def initIns(self):
        self.mainImage = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/main.png').convert_alpha(),
            (self.width, self.height)),0)
        self.ins2 = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/lev2ins.png').convert_alpha(),
            (self.width, self.height)),0) 
        self.ins3 = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/lev3ins.png').convert_alpha(),
            (self.width, self.height)),0)
        self.instruc1 = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/instructions1.png').convert_alpha(),
            (self.width, self.height)),0)
    

    def keyPressed(self, code, mod):
        if code==pygame.K_i:
            self.screen1=False
            self.instructions = True
        if code==pygame.K_ESCAPE:
            quit()
        if self.instructions==True:
            if code==pygame.K_RIGHT:
                self.lev2ins = not(self.lev2ins)
                if self.lev2ins==False:
                    self.lev3ins = True
            if code==pygame.K_LEFT:
                if self.lev2ins == True:
                    self.lev2ins=False
                    self.instructions = True
                elif self.lev3ins==True:
                    self.lev3ins =False
                    self.lev2ins=True                    
        if self.instructions == True:
            if code == pygame.K_BACKSPACE:
                self.instructions = False
                self.lev2ins=False
                self.lev3ins= False
                self.screen1=True
        if self.level==1:
            if code== pygame.K_p:
                self.screen1=False
            if code == pygame.K_r:
                self.init()
                self.screen1=False
        if code == pygame.K_SPACE:
            if self.level==3:
                    ship = self.shipGroup.sprites()[0]
                    self.missiles.add(Missile(ship.x, ship.y, ship.angle))
            else:
                self.shipFlag=False
                if self.level==2:
                    self.planetChange = True
        if self.level==3:
            if code== pygame.K_RETURN:
                self.screen3=False
        
        if self.level==2:
            if code == pygame.K_r:
                self.init(self.level)
                self.mainscreen=False
            elif code== pygame.K_RETURN:
                self.mainscreen=False
        
    



    def timerFired(self, dt):
        if self.level==1: self.timerFired1(dt)
        elif self.level==2: self.timerFired2(dt)
        elif self.level == 3: self.timerFired3(dt)


    #HOW TO INITIALIZE GROUPS FROM LUKAS'S CODE
    def init1(self):
        moon = Moon( self.planetx+self.radCurve, self.planety+self.radCurve )
        planet= Planet(self.planetx,self.planety, "earth", 100)
        ship = Ship(self.planetx+self.r*cos(self.theta), self.planety
            + self.r*sin(self.theta))
        self.planetGroup = pygame.sprite.Group(planet) #c
        self.shipGroup = pygame.sprite.Group(ship)#c
        self.moonGroup = pygame.sprite.Group(moon)#c
    

    def level1init(self):
        self.marsHit=False
        self.screen1=True
        self.playing=True
        self.onScreen=True
        self.marsx = self.width*3/5-50
        self.marsy = self.height/2
        self.mars= Planet(self.marsx,self.marsy, "mars",100,30)
        self.marsGroup = pygame.sprite.Group(self.mars)
        Ship.init()
        Moon.init()
        self.planetx,self.planety=self.width/5,self.height-self.height/3,
        self.r = 120
        self.radCurve=550
        self.moonAngle=80
        self.moonx, self.moony= self.width, self.height
        self.init1()
        self.m=0
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        self.starImage = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/stars.png').convert_alpha(),
            (self.width, self.height)),0)

    def initButtons(self):
        self.playButtonx =  self.width*11/15
        self.playButtony =  self.height*11/15 
        self.instructionx = self.playButtonx-40
        self.instructiony = self.playButtony+80

    def mousePressed(self, x, y):
        print(x,y)
        x1 =self.playButtonx
        x2 =x1+200
        y1 =self.playButtony
        y2 = y1+75
        if x>= x1 and x<= x2 and y>=y1 and y<=y2:
            self.screen1=False
        xi =self.instructionx
        xi1 =xi+290
        yi =self.instructiony
        yi1 = yi+70
        if x<= xi1 and x>=xi and y>=yi and y<=yi1:
            self.screen1=False
            self.instructions=True
            


    def mouseReleased(self, x, y):
        pass
    def drawButton(self,screen):
        midx = self.playButtonx +200/2
        midy = self.playButtony +70/2
        pygame.draw.rect(screen, (0,128,128,0.05), (self.playButtonx,self.playButtony,200,70))
        self.message_display("PLAY", screen, midx,midy, 40)
        pygame.draw.rect(screen, (0,128,128,0.05), (self.instructionx,self.instructiony,285,60))
        self.message_display("Instructions", screen, midx,midy+80, 40)



    
    def checkOnScreen(self,  x ,y ):
        if self.playing==True:
            if (x>= self.width or x<=0 or y>=self.height
            or y<=0):
                self.onScreen=False
            

    
    def launchShip(self):
        ship=self.shipGroup.sprites()[0]
        speed = 13
        if self.level==2: self.score-=1
        ship.x += speed*cos(pi/2-self.theta)
        ship.y -= speed*sin(pi/2-self.theta)
        self.checkOnScreen(ship.x,ship.y)
        self.shipGroup.update(self.width, self.height, self.theta,
            ship.x, ship.y, self.r, self.angle, self.shipFlag)

    def moveMoon(self):
        if self.level==1:
            self.moonAngle+=.018
            self.moonx=self.planetx+self.radCurve*cos(self.moonAngle)
            self.moony=self.planety+self.radCurve*sin(self.moonAngle)
            self.moonGroup.update(self.moonx,self.moony,
                self.radCurve, self.moonAngle)
        else: pass
                

    def implementGravity(self):
        ship=self.shipGroup.sprites()[0]
        xs = ship.x
        ys = ship.y
        xp = self.marsx
        yp = self.marsy
        dist = math.sqrt((xs-xp)**2 + (ys-yp)**2)
        outR=200
        if dist<= outR:
            angle = acos(min(1, max(ship.x/dist, -1)))
            F=9
            ship.x = ship.x +F*cos(angle)
            ship.y = ship.y + F*sin(angle)



        
    def displayMainScreen(self,screen):
        screen.blit(self.mainImage, (0,0), area=None)
        self.message_display("Welcome to a Space Game", screen, self.width/3,
            self.height/5, 50)
        self.message_display("isn't this background awesome?", screen, 
            self.width/3,
            self.height/4, 30)
        self.message_display("Press P to play", screen, self.width/3,
            self.height/3-10, 30)
        self.message_display("Press I for instructions", screen, self.width/3,
            self.height/3+20, 30)
        self.drawButton(screen)


    #COLLISION DETECTION SYNTAX MODIFIED FROM LUKAS'S CODE #m
    def timerFired1(self,dt):
        if self.screen1==False:
            self.moveMoon()
            if pygame.sprite.groupcollide(
                self.shipGroup, self.marsGroup, True, False,
                pygame.sprite.collide_circle): #m
                self.marsHit = True
            if self.shipFlag==True:
                self.theta-=0.080
                self.angle+=0.080*180/pi
                self.shipGroup.update(self.width, self.height, self.theta,
                    self.planetx, self.planety, self.r, self.angle,
                    self.shipFlag) #m
            else:
                self.r+=5
                self.launchShip()
                self.implementGravity()
            if pygame.sprite.groupcollide(
                self.shipGroup, self.moonGroup, True, False,
                pygame.sprite.collide_circle):#m
                self.playing=False
                self.level=2
                self.init(self.level)

                

    def redrawLev1(self,screen):
        if self.marsHit==True:
            self.message_display("Oops we hit Mars :(",screen, self.width/2, 
                self.height/2)
        else:
            if self.screen1==False:
                if self.onScreen==False:
                    self.message_display( "Oops! ",screen,self.width/2, 
                        self.height/2,80)
                    self.message_display( "Press R to restart",screen,
                        self.width/2, self.height/3*2,80)
                elif self.playing==True:
                    self.shipGroup.draw(screen)
                    self.planetGroup.draw(screen)
                    self.moonGroup.draw(screen)
                    self.marsGroup.draw(screen)
                else:
                    self.message_display('Done!', screen)
                    print('hit')
            else:
                self.displayMainScreen(screen)



    
    def level2init(self):
        self.mainscreen=True
        self.planetChange= False
        self.playing=True 
        self.onScreen=True
        self.shipCount=0
        self.score = 350
        self.makePlanets()
        self.gamex, self.gamey = self.width/2, self.height/2
        self.initShip(self .gamex, self.gamey)
        Sun.init()
        self.sunx,self.suny,self.r= (self.width/2,self.height/2, 120)
        self.sun = Sun(self.sunx,self.suny)
        self.initFuel()
        self.sungroup = pygame.sprite.Group(self.sun)
        self.planetList=[self.mars, self.uranus, self.mercury, self.neptune]
        pygame.font.init()
        self.starImage = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/stars.png').convert_alpha(),
            (self.width, self.height)),0)
        self.counter = 0
        self.initScore = 350
        
   




    def makePlanets(self):
        self.mars= Planet(self.width/5,self.height/5, "mars")
        self.marsGroup = pygame.sprite.Group(self.mars)
        self.collPlanet = None
        self.neptune= Planet(4*self.width/5,self.height/5, "neptune")
        self.neptunegroup = pygame.sprite.Group(self.neptune)
        self.uranus = Planet(self.width/5, 4*self.height/5, "uranus")
        self.uranusgroup = pygame.sprite.Group(self.uranus)
        self.mercury = Planet(4*self.width/5, 4*self.height/5, "mercury")
        self.mercurygroup = pygame.sprite.Group(self.mercury)



    def initShip(self,x,y):
        self.theta=90
        self.angle=-110
        self.shipFlag=True
        self.r=120
        # # if self.shipCount<=5:
        # self.shipCount+=1
        Ship.init()
        ship = Ship(x, y)
        self.shipGroup = pygame.sprite.GroupSingle(ship)


    def initFuel(self):
        self.fuelx = choice([self.mars.x , self.uranus.x, self.neptune.x, 
            self.mercury.x])
        self.fuely = choice([self.mars.y, self.uranus.y, self.neptune.y,
         self.mercury.y])
        Fuel.init()
        self.fuel = Fuel(self.fuelx,self.fuely)
        self.fuelGroup = pygame.sprite.Group(self.fuel)



    def drawFuel(self,screen):
        topLeftx=self.width/2-75
        topLefty = self.height/8
        fuelWidth = 150
        fuelHeight = 50
        #pygame.draw.rect(screen, (0,200,0), (topLeftx,topLefty,fuelWidth,fuelHeight), 2)
            



    #COLLISION DETECTION SYNTAX FROM LUKAS'S CODE#m
    def checkColl(self,screen):
            if pygame.sprite.groupcollide(
                self.shipGroup, self.mercurygroup, True, False,
                pygame.sprite.collide_circle):#m
                if (self.collPlanet.x==self.fuelx and 
                    self.collPlanet.y==self.fuely):
                    self.score +=80
                else:
                    self.score+=10
                self.r=120
                self.initShip(self.sunx, self.suny)
            if pygame.sprite.groupcollide(
                self.shipGroup, self.neptunegroup, True, False,
                pygame.sprite.collide_circle): #m
                if (self.collPlanet.x==self.fuelx and 
                    self.collPlanet.y==self.fuely):
                    self.score +=80
                else:
                    self.score+=10
                self.r=120
                self.initShip(self.sunx, self.suny)
            if pygame.sprite.groupcollide(
                self.shipGroup, self.uranusgroup, True, False,
                pygame.sprite.collide_circle): #m
                if (self.collPlanet.x==self.fuelx and 
                    self.collPlanet.y==self.fuely):
                    self.score +=80
                else:
                    self.score+=10
                self.r=120
                self.initShip(self.sunx, self.suny)
            if pygame.sprite.groupcollide(
                self.shipGroup, self.marsGroup, True, False,
                pygame.sprite.collide_circle):#m
                if (self.collPlanet.x==self.fuelx and 
                    self.collPlanet.y==self.fuely):
                    self.score +=80
                else:
                    self.score+=10
                self.r=120
                self.initShip(self.sunx, self.suny)


    def timerFired2(self,dt):
        if self.mainscreen==False:
            self.counter+=1
            if self.playing== True:
                if self.score>=360: 
                    self.level=3
                    self.playing=False
                    self.init(self.level)
                if self.score<=0:
                    self.playing=False
                if self.shipFlag==True:
                    self.theta-=0.090
                    self.angle+=0.090*180/pi
                    self.shipGroup.update(self.width, self.height, self.theta,
                        self.gamex, self.gamey, self.r, self.angle,
                        self.shipFlag)
                else:
                    self.r+=5
                    self.launchShip()
                    self.gamex = self.width/2
                    self.gamey = self.height/2
                ship=self.shipGroup.sprites()[0]
                self.checkOrbit(degrees(self.theta), ship.x,ship.y)
                if self.counter%60==0:
                    self.initFuel()
                self.checkColl(self)


    def checkAngle(self, dist,xp,xs):
        angle  = degrees(acos((xp-xs)/dist))%360
        print(angle, "angle")
        if ((angle<30 and angle>0) or (angle<120 and angle>60)
            or (angle<220 and angle>150) or (angle<310 and angle>260)
            or (angle>330 and angle<359)):
                return True
        return False



    def stickIntoOrbit(self, xp, yp):
        self.shipFlag = True
        
        self.planetChange = False
        self.gamex = xp
        self.gamey = yp

        #self.r = 120
        



        
    def checkOrbit(self,degrees, shipx, shipy):
        if self.planetChange == True:
            degrees = degrees % 360
            ship=self.shipGroup.sprites()[0]
            xs = ship.x
            ys = ship.y
            minDist = 50000
            for planet in [self.mars, self.uranus, self.neptune, self.mercury]:
                if planet != self.collPlanet:
                    dist = ((xs-planet.x)**2+(ys-planet.y)**2)**0.5
                    if dist<minDist:
                        minDist = dist
                        xp = planet.x
                        yp = planet.y
                        r = planet.radius
                        self.collPlanet = planet
                    
            outR=200
            inR = 190
            # print(minDist, "dist", r,  "r",  outR, "outR")
            if  minDist >inR and minDist< outR:
                print("i'm here")
                if not self.checkAngle(minDist,xp,xs):
                    print("made it")
                    self.stickIntoOrbit(self.collPlanet.x, self.collPlanet.y)


    def makeLev2(self,screen):
        self.marsGroup.draw(screen)
        self.neptunegroup.draw(screen)
        self.drawScore(screen)
        self.uranusgroup.draw(screen)
        self.mercurygroup.draw(screen)
        self.sungroup.draw(screen)
        self.shipGroup.draw(screen)
        self.fuelGroup.draw(screen)
        self.message_display("Fuel = %d"  % self.score, 
            screen,self.width/2,
            self.height/12,75)
        self.drawFuel(screen)


    def redrawLev2(self,screen):
        if self.mainscreen==False:
            if self.playing==False:
                if self.score<=0:
                    if self.onScreen==True:
                        self.message_display("You lost, let's try again!",screen, self.width/2, 
                            self.height/2-10, 70)
                        self.message_display("Press R!", screen, self.width/2, self.height/2+70)
            if self.onScreen==False:
                self.message_display( "Oops! Press R to restart",screen, 
                    self.width/2,self.height/2,85)                
            else:
                self.makeLev2(screen)
            # else:
            #     self.message_display('Done!', screen, self.width/2, self.height/2)
        else:
            self.drawLev2(screen)

    #image initialization from Lukas's code (#modified)
    def drawLev2(self,screen):
            lev2Image = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/lev2.png').convert_alpha(),
            (self.width, self.height)),0)
            screen.blit(lev2Image, (0,0), area=None) #m
            self.message_display("Time to Fuel Up!",screen,self.width/2,
                self.height/2 )
            self.message_display("Press enter to continue!",screen, 
                self.width/2, self.height*2/3,82 )


    
    def level3init(self):
        self.win=False
        self.screen3=True
        self.bgColor = (0, 0, 0)
        Ship.init()
        ship = Ship(self.width / 2, self.height / 2)
        self.shipGroup = pygame.sprite.GroupSingle(ship)
        self.earthStage=1
        planet= Planet(self.width/2,self.height -100, "earth")
        self.planetGroup = pygame.sprite.Group(planet)
        self.asteroids = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        self.hitCount=1
        self.score3 = 0
        self.earthFlag=False
        self.counter=0
        self.lost=False
        self.bgImage = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/Lev3.png').convert_alpha(),
            (self.width, self.height)),0)
        self.closeImage = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load('images/finish.jpg').convert_alpha(),
            (self.width, self.height)),0)

    #collision detection from lukas's code (#COPIED)
    def timerFired3(self, dt):
        if self.screen3==False:
            if self.score3>=500:
                self.win=True
            if self.counter % 30 == 0:
                 #m
                x = random.randint(0, self.width)
                y = 1
                self.asteroids.add(Asteroid(x, y))
            self.counter+=1
            self.shipGroup.sprites()[0].update2(dt, self.isKeyPressed, 
                self.width, self.height)
            self.asteroids.update(self.width, self.height)
            self.missiles.update(self.width, self.height)
            ship = self.shipGroup.sprite
            for asteroid in pygame.sprite.groupcollide(
                self.asteroids, self.missiles, True, True,
                pygame.sprite.collide_circle): #copied
                self.asteroids.add(asteroid.destroy())
                self.score3 += 5
            for asteroid in pygame.sprite.groupcollide(
                self.asteroids, self.planetGroup,   True, False,
                pygame.sprite.collide_circle):  #copied
                self.hitCount+=1
                pass
            if self.hitCount%5==0: 
                self.earthStage+=1
                self.earthFlag=True
                self.hitCount += 1
                if self.hitCount==4:
                    self.lost=True

            if self. earthFlag==True and (self.earthStage==2 or self.earthStage==3):
                self.planetGroup.update(self.earthStage, self.width/2,
                    self.height -100)
                self.earthFlag=False

    def makeScreen3(self,screen):
        screen.blit(self.bgImage, (0,0), area=None)
        self.message_display("Protect The Earth!", screen, self.width/2,
            self.height/2-30, 80)
        self.message_display("Press Enter to Continue", screen, self.width/2, self.height/2+40, 70)


    def redrawLev3(self, screen):
        if self.win==True:
            screen.blit(self.closeImage, (0,0), area=None)
            self.message_display("You won!", screen, self.width/2, self.height/2+80, 90)
            self.message_display("Congratulations!", screen, self.width/2, self.height/2, 90)        
        elif self.lost==True:
            Stars.updateStars(self.stars,screen,self.width, self.height)
            self.message_display("We lost the Earth!", screen, self.width/2, self.height/2, 90)
            self.message_display("Press R to try again",screen, self.width/2, self.height/2+80, 90)  
        elif self.screen3==False:
            Stars.updateStars(self.stars,screen,self.width, self.height)
            self.shipGroup.draw(screen)
            self.asteroids.draw(screen)
            self.missiles.draw(screen)
            self.planetGroup.draw(screen)
            self.message_display("Score:%d"%self.score3, screen, self.width/12+20, self.height/12,50)
        else:
            self.makeScreen3(screen)

    def drawScore(self,screen):
        pygame.draw.rect(screen, (255,0,0), (10,10,200,20), 0)
        pygame.draw.rect(screen, (0,250,154), (10,10,200*(self.score/100),20), 
            0)


    def makeInstructions(self,screen):
        if self.screen1==False:
            if self.instructions==True:
                    screen.blit(self.instruc1, (0,0), area=None)
            if self.lev2ins ==True:
                screen.blit(self.ins2, (0,0), area=None)
            if self.lev3ins == True:
                screen.blit(self.ins3, (0,0), area=None)




    def redrawAll(self, screen):
        if self.instructions==True:
            self.makeInstructions(screen)

        else:
            if self.level==1 or self.level==2:
                screen.blit(self.starImage, (0,0), area=None)
                ship = self.shipGroup.sprites()[0]
            ship = self.shipGroup.sprites()[0]
            if self.level==1: self.redrawLev1(screen)
            elif self.level==2: self.redrawLev2(screen)
            elif self.level ==3:
                self.redrawLev3(screen)

    
    def text_objects(text, font, shade):
        textSurface = font.render(text, True, shade)
        return textSurface, textSurface.get_rect()


    
    def message_display(self,text, screen,x,y,size=115,
        font_path="SFOUTERLimits.ttf",
        shade=(192,192,192)):
        largeText = pygame.font.Font(font_path,size)
        TextSurf, TextRect = Game.text_objects(text, largeText,shade)
        TextRect.center = (x,y)
        screen.blit(TextSurf, TextRect)

        




Game(1200, 700).run()
print(cos(90))
