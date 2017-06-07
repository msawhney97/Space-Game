#Taken from (andrewID) slathar
import random
class Stars(object):
	def listAllStars(x,y):
		starsList=[]
		for i in range(360):
			starsList.append([random.randint(0,1400),random.randint(0,800)])
		return starsList

	def updateStars(starsAll,screen,x,y):
		for star in starsAll:
			star[1] -= -3
			#star[0] += -5
			if star[0] <= 0 or star[0] > 1400:
				star[0] = random.randint(0,1400)
				star[1] = random.randint(0,800)
			if star[1] <0 or star[1] > 700:
				star[0] = random.randint(0,1400)
				star[1] = random.randint(0,800)
			screen.set_at(star,(255,255,255))
