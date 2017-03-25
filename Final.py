import pygame,sys
import math

# user stats
# different levels

class Config(object):
	display_width = 1024
	display_height = 566
	
	scale = 0.8
	table_x = int(display_width * scale)
	table_y = int(display_height * scale)
	#https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/American-style_pool_table_diagram_(empty).png/1024px-American-style_pool_table_diagram_(empty).png
	tableImg = pygame.image.load("pool_table.png")
	tableImg = pygame.transform.smoothscale(tableImg,(table_x,table_y))

	edgeX = (display_width - table_x)/2
	edgeY = (display_height - table_y)/2

	white = (255,255,255)
	black = (0,0,0)
	darkGrey = (90,90,90)
	grey = (128,128,128)
	red = (255,0,0)
	ray = (153, 51, 51)
	fps = 20000

def text_objects(text, font):
    textSurface = font.render(text, True, Config.black)
    return textSurface, textSurface.get_rect()

# Start Screen
def splashScreen():
	pygame.mixer.init()
	# Bach Cello Suite No.1 - Prelude by Yo-Yo Ma
	bgm = pygame.mixer.Sound("Bach.ogg")
	bgm.set_volume(.5)
	bgm.play(1)

	display_width = 1024
	display_height = 566
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	clock = pygame.time.Clock()
	welcomeImg = pygame.image.load('welcome.png')

	def drawWelcome(x,y):
		gameDisplay.blit(welcomeImg,(x,y))

	def drawHelper(x,y):
		mouse = pygame.mouse.get_pos()   #get mouse motion
		click = pygame.mouse.get_pressed()   #get mouse click

		questionImg = pygame.image.load("question.png")
		questionImg = pygame.transform.smoothscale(questionImg, (50,50))
		gameDisplay.blit(questionImg,(x,y))

		if x<mouse[0]<x+50 and y<mouse[1]<y+50:
			rect = pygame.Surface((600,400),pygame.SRCALPHA)
			rect.fill((148,148,148,230))
			gameDisplay.blit(rect,(100,30))

			text = "Instruction"
			text1 = "Use 'a' and 'd' to rotate the cue"
			text2 = "Hold mouse button to adjust the power and make the shot"
			text3 = "Win over computer to get coins and unlock more awesome cues"

			smallText1 = pygame.font.SysFont("comicsansms", 20)
			textSurf, textRect = text_objects(text, smallText1)
			textRect.center = (x+370,y+50)
			gameDisplay.blit(textSurf, textRect)

			textSurf, textRect = text_objects(text1, smallText1)
			textRect.center = (x+370,y+100)
			gameDisplay.blit(textSurf, textRect)

			textSurf, textRect = text_objects(text2, smallText1)
			textRect.center = (x+370,y+150)
			gameDisplay.blit(textSurf, textRect)

			textSurf, textRect = text_objects(text3, smallText1)
			textRect.center = (x+370,y+200)
			gameDisplay.blit(textSurf, textRect)


	intro = True

	while intro:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            intro = False
	            sys.exit()
	 	mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
	            
		gameDisplay.fill(Config.white)
		drawWelcome(0,0)
		#draw buttons and do interaction
		if 750<mouse[0]<950 and 320<mouse[1]<370:
			pygame.draw.rect(gameDisplay, Config.grey,(750,320,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,450,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,385,200,50))
			pygame.draw.circle(gameDisplay, Config.darkGrey, (980,50), 15)
			pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
			pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)
			if click[0] == 1:
				intro = False
				GameStatus.restart()
				gameLoop()

		elif 750<mouse[0]<950 and 385<mouse[1]<435:
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,320,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,450,200,50))
			pygame.draw.rect(gameDisplay, Config.grey,(750,385,200,50))
			pygame.draw.circle(gameDisplay, Config.darkGrey, (980,50), 15)
			pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
			pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)
			if click[0] == 1:
				intro = False	
				GameStatus.restart()
				GameStatus.mode = "Single"
				gameLoop()			

		elif 750<mouse[0]<950 and 450<mouse[1]<500:
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,320,200,50))
			pygame.draw.rect(gameDisplay, Config.grey,(750,450,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,385,200,50))
			pygame.draw.circle(gameDisplay, Config.darkGrey, (980,50), 15)
			pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
			pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)
			if click[0] == 1:
				intro = False
				selectLoop()

		elif math.sqrt((mouse[0]-980)**2+(mouse[1]-50)**2) <= 15:
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,320,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,450,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,385,200,50))
			pygame.draw.circle(gameDisplay, Config.grey, (980,50), 15)
			pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
			pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)
			if click[0] == 1:
				pygame.quit()
				intro = False
				sys.exit()


		else:
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,320,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,450,200,50))
			pygame.draw.rect(gameDisplay, Config.darkGrey,(750,385,200,50))
			pygame.draw.circle(gameDisplay, Config.darkGrey, (980,50), 15)
			pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
			pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)

		smallText1 = pygame.font.SysFont("comicsansms", 20)
		textSurf, textRect = text_objects("vs Computer", smallText1)
		textRect.center = ( (750+(200/2)), (320+(50/2)) )
		gameDisplay.blit(textSurf, textRect)

		textSurf, textRect = text_objects("1 ON 1", smallText1)
		textRect.center = ( (750+(200/2)), (385+(50/2)) )
		gameDisplay.blit(textSurf, textRect)

		textSurf, textRect = text_objects("SHOP", smallText1)
		textRect.center = ( (750+(200/2)), (450+(50/2)) )
		gameDisplay.blit(textSurf, textRect)


		largeText = pygame.font.SysFont("comicsansms", 50)
		TextSurf, TextRect = text_objects("RICK'S GAME ROOM", largeText)
		TextRect.center = ((display_width/2),(display_height/7))
		gameDisplay.blit(TextSurf, TextRect)

		drawHelper(30,30)

		pygame.display.update()
		clock.tick(15)

# SHOP screen
def selectLoop():
	display_width = 1024
	display_height = 566
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	clock = pygame.time.Clock()
	welcomeImg = pygame.image.load('welcomeBlur.png')

	def drawWelcome(x,y):
		gameDisplay.blit(welcomeImg,(x,y))

	def drawSelect(x,y,cueName,price):
		CueList = ["classical.png","arrow.png","stripe.png","master.png"]

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		s = pygame.Surface((200,400), pygame.SRCALPHA)
		if GameStatus.cue == CueList.index(cueName):
			s.fill((148,148,148,160))
		elif ((x<mouse[0]<x+200 and y<mouse[1]<y+400)):
			s.fill((148,148,148,160))
			if click[0] == 1 and GameStatus.coins >= price and (cueName not in GameStatus.unlockedCue):
				GameStatus.coins -= price
				GameStatus.cue = CueList.index(cueName)
				GameStatus.unlockedCue.append(cueName)
			elif click[0] == 1 and cueName in GameStatus.unlockedCue:
				GameStatus.cue = CueList.index(cueName)
		else:
			s.fill((90,90,90,160))


		image = pygame.Surface((390,80))
		image.fill((128,128,128))
		cueImage = pygame.image.load("cues/"+cueName)
		cueImage = pygame.transform.smoothscale(cueImage,(390,80))
		image.blit(cueImage,(0,0))
		image.set_colorkey((128,128,128))
		image = image.convert_alpha()
		image0 = image.convert_alpha()
		ox,oy = image.get_rect().center
		image = pygame.transform.rotate(image0, 80)
		rect = image.get_rect()		
		rect.center = ox,oy

		s.blit(image, (50,0))

		if not cueName in GameStatus.unlockedCue:
			#lock img: https://lh5.ggpht.com/0nEi836Ec0mgHa6X_NgY4cKtAz0tug-hndFg0SuHwEAE4S6GlBTcEu7ynKyCcPLSMAo=w300
			lockImg = pygame.image.load("lock.png")
			lockImg = pygame.transform.smoothscale(lockImg, (70,70))
			s.blit(lockImg,(80,200))
			#https://lh6.ggpht.com/7uOU316xrU1bE2ja0pwoQpc9DExtoUV21kl8F90KWTDwdjymZt7jjunlYK4_AjkycA=w300, https://lh6.ggpht.com/7uOU316xrU1bE2ja0pwoQpc9DExtoUV21kl8F90KWTDwdjymZt7jjunlYK4_AjkycA=w300
			coinImg = pygame.image.load("coin.png")
			coinImg = pygame.transform.smoothscale(coinImg, (20,20))
			s.blit(coinImg,(10,10))

			smallText2 = pygame.font.SysFont("comicsansms", 20)
			textSurf, textRect = text_objects(str(price), smallText2)
			textRect.center = (50, 17)
			s.blit(textSurf, textRect)

		gameDisplay.blit(s, (x,y))

		if cueName == "classical.png":
			smallText = pygame.font.SysFont("comicsansms", 20)
			textSurf, textRect = text_objects("Classical", smallText)
			textRect.center = (x+100,y+450)
			gameDisplay.blit(textSurf, textRect)

			powerImg = pygame.image.load("powerBar/power1.png")
			powerImg = pygame.transform.smoothscale(powerImg, (100,20))
			gameDisplay.blit(powerImg, (x+50,y+420))

		if cueName == "stripe.png":
			smallText = pygame.font.SysFont("comicsansms", 20)
			textSurf, textRect = text_objects("Premium", smallText)
			textRect.center = (x+100,y+450)
			gameDisplay.blit(textSurf, textRect)

			powerImg = pygame.image.load("powerBar/power3.png")
			powerImg = pygame.transform.smoothscale(powerImg, (100,20))
			gameDisplay.blit(powerImg, (x+50,y+420))

		if cueName == "arrow.png":
			smallText = pygame.font.SysFont("comicsansms", 20)
			textSurf, textRect = text_objects("Master", smallText)
			textRect.center = (x+100,y+450)
			gameDisplay.blit(textSurf, textRect)

			powerImg = pygame.image.load("powerBar/power2.png")
			powerImg = pygame.transform.smoothscale(powerImg, (100,20))
			gameDisplay.blit(powerImg, (x+50,y+420))

		if cueName == "master.png":
			smallText = pygame.font.SysFont("comicsansms", 20)
			textSurf, textRect = text_objects("Legend", smallText)
			textRect.center = (x+100,y+450)
			gameDisplay.blit(textSurf, textRect)

			powerImg = pygame.image.load("powerBar/power4.png")
			powerImg = pygame.transform.smoothscale(powerImg, (100,20))
			gameDisplay.blit(powerImg, (x+50,y+420))


	intro = True
	while intro:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            intro = False
	            sys.exit()
	            
		gameDisplay.fill(Config.white)
		drawWelcome(0,0)

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed() 

		drawSelect(70,50,"classical.png",0)
		drawSelect(300,50,"arrow.png",40)
		drawSelect(530,50,"stripe.png",100)
		drawSelect(750,50,"master.png",300)


		box = pygame.Surface((80,40), pygame.SRCALPHA)
		if 920<mouse[0]<1000 and 480<mouse[1]<520:
			box.fill((128,128,128,90))
			if click[0] == 1:
				intro = False
				GameStatus.restart()
				gameLoop()

		else:
			box.fill((90,90,90,90))
		gameDisplay.blit(box,(920,480))

		smallText1 = pygame.font.SysFont("comicsansms", 20)
		textSurf, textRect = text_objects("Start", smallText1)
		textRect.center = (960, 500)
		gameDisplay.blit(textSurf, textRect)

		#coin img: https://lh6.ggpht.com/7uOU316xrU1bE2ja0pwoQpc9DExtoUV21kl8F90KWTDwdjymZt7jjunlYK4_AjkycA=w300
		coinImg = pygame.image.load("coin.png")
		coinImg = pygame.transform.smoothscale(coinImg, (20,20))
		gameDisplay.blit(coinImg,(800,20))

		smallText2 = pygame.font.SysFont("comicsansms", 20)
		textSurf, textRect = text_objects(str(GameStatus.coins), smallText2)
		textRect.center = (840, 27)
		gameDisplay.blit(textSurf, textRect)

		pygame.display.update()
		clock.tick(15)

# Game End Screen
def gameEnd():
	display_width = 1024
	display_height = 566
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	clock = pygame.time.Clock()
	welcomeImg = pygame.image.load('welcomeBlur.png')

	def drawWelcome(x,y):
			gameDisplay.blit(welcomeImg,(x,y))

	intro = True

	while intro:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            intro = False
	            sys.exit()

	            
		gameDisplay.fill(Config.white)
		drawWelcome(0,0)

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if GameStatus.gameWon == "computer":
			largeText = pygame.font.SysFont("comicsansms", 120)
			TextSurf, TextRect = text_objects("You Lost!", largeText)
			TextRect.center = ((display_width/2),(display_height/3))
			gameDisplay.blit(TextSurf, TextRect)

		elif GameStatus.gameWon == "player":
			if GameStatus.addCoin == True:
				GameStatus.coins += 30
				GameStatus.addCoin = False
			largeText = pygame.font.SysFont("comicsansms", 120)
			TextSurf, TextRect = text_objects("You Won!", largeText)
			TextRect.center = ((display_width/2),(display_height/3))
			gameDisplay.blit(TextSurf, TextRect)

			largeText2 = pygame.font.SysFont("comicsansms", 80)
			TextSurf, TextRect = text_objects("Your winning rate: 100%", largeText2)
			TextRect.center = ((display_width/2),(display_height/2))
			gameDisplay.blit(TextSurf, TextRect)

			coinImg = pygame.image.load("coin.png")
			coinImg = pygame.transform.smoothscale(coinImg, (20,20))
			gameDisplay.blit(coinImg,(800,20))

			smallText2 = pygame.font.SysFont("comicsansms", 20)
			textSurf, textRect = text_objects("+30", smallText2)
			textRect.center = (840, 27)
			gameDisplay.blit(textSurf, textRect)


		if 750<mouse[0]<950 and 350<mouse[1]<400:
			pygame.draw.rect(gameDisplay, Config.grey,(750,350,200,50))
			if click[0] == 1:
				GameStatus.gameWon = None
				splashScreen()
				
		else: pygame.draw.rect(gameDisplay, Config.darkGrey,(750,350,200,50))

		smallText1 = pygame.font.SysFont("comicsansms", 20)
		textSurf, textRect = text_objects("Menu", smallText1)
		textRect.center = ( (750+(200/2)), (350+(50/2)) )
		gameDisplay.blit(textSurf, textRect)

		pygame.display.update()
		clock.tick(15)

# Collection of all game status
class GameStatus(object):
	turn = "player"
	computerGoal = False
	playerGoal = False
	computerFail = False
	computerWinRound = False
	playerFail = False
	playerWinRound = False
	cue = 0
	gameWon = None
	playerGroup = None
	computerGroup = None
	mode = "AI"
	coins = 1000
	unlockedCue = ["classical.png"]
	addCoin = True

	# initialize all game status
	@staticmethod
	def restart():
		GameStatus.turn = "player"
		GameStatus.computerGoal = False
		GameStatus.playerGoal = False
		GameStatus.computerFail = False
		GameStatus.computerWinRound = False
		GameStatus.playerFail = False
		GameStatus.playerWinRound = False
		GameStatus.gameWon = None
		GameStatus.playerGroup = None
		GameStatus.computerGroup = None
		CueBall.x = 200
		CueBall.y = 200
		Cue.start = True
		CueBall.vel = 0.1
		Cue.shoot = False
		GameStatus.addCoin = True
		Ball.goalLst = []


# writing function and Text class modified from: https://github.com/horstjens/ThePythonGameBook/blob/master/pygame/020_shooting_from_tank.py
def write(msg="pygame is cool",size = 28,color = Config.white):
    """helper function for the Text sprite"""
    myfont = pygame.font.SysFont("None", size)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext 

class Text(pygame.sprite.Sprite):
    """ a helper class to write text on the screen """
    number = 0 
    book = {}
    def __init__(self, pos, function):
        self.number = Text.number # get a unique number
        Text.number += 1 # prepare number for next Textsprite
        Text.book[self.number] = self # store myself into the book
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = [0.0,0.0]
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.function = function
        self.msg = None
        self.update(0)
        
        
    def update(self, seconds):
		if self.function == "turn":        
			if GameStatus.mode == "AI":
				if GameStatus.turn == "player":
					self.msg = "Player's turn"
				elif GameStatus.turn == "computer":
					self.msg = "Computer's turn"

			if GameStatus.mode == "Single":
				if GameStatus.turn == "player":
					self.msg = "Player 1's turn"
				elif GameStatus.turn == "computer":
					self.msg = "Player 2's turn"
			self.image = write(self.msg)

		if self.function == "type":
			if GameStatus.mode == "AI":
				if GameStatus.playerGroup == 1:
					self.msg = "You're Solids"
				if GameStatus.playerGroup == 2:
					self.msg = "You're Stripes"
				if GameStatus.playerGroup == None:
					self.msg = None
			self.image = write(self.msg)

		if self.function == "foul":
			self.msg = "Foul"
			self.image = write(self.msg,40,Config.black)

		
		self.rect = self.image.get_rect()
		self.rect.centerx = self.pos[0]
		self.rect.centery = self.pos[1]

class Wall(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.groups)
		image = pygame.Surface((Config.table_x-30, Config.table_y-30))
		image.fill((128,128,128))
		if self.name == "top":
			pygame.draw.line(image, Config.red, (72,43), (388,43), 1)
			pygame.draw.line(image, Config.red, (430,43), (Config.table_x-72,43), 1)
		elif self.name == "left":
			pygame.draw.line(image, Config.red, (44,72), (44,Config.table_y-72), 1)
		elif self.name == "right":
			pygame.draw.line(image, Config.red, (Config.table_x-44,72), (Config.table_x-44,Config.table_y-72), 1)
		elif self.name == "bottom":
			pygame.draw.line(image, Config.red, (72,Config.table_y-45), (388,Config.table_y-45), 1)
			pygame.draw.line(image, Config.red, (430,Config.table_y-45), (Config.table_x-72,Config.table_y-45), 1)
		image.set_colorkey((128,128,128))
		self.image = image
		self.rect = self.image.get_rect()
		self.rect = (Config.edgeX,Config.edgeY,Config.display_width,Config.display_height)
		self.mask = pygame.mask.from_surface(self.image)

class TopWall(Wall):
	def __init__(self):
		self.name = "top"
		Wall.__init__(self)

class LeftWall(Wall):
	def __init__(self):
		self.name = "left"
		Wall.__init__(self)

class RightWall(Wall):
	def __init__(self):
		self.name = "right"
		Wall.__init__(self)

class BottomWall(Wall):
	def __init__(self):
		self.name = "bottom"
		Wall.__init__(self)

class Hole(pygame.sprite.Sprite):
	def __init__(self):
			pygame.sprite.Sprite.__init__(self,self.groups)
			image = pygame.Surface((Config.display_width, Config.display_height))
			image.fill((128,128,128))


			pygame.draw.arc(image, Config.black, ((132,84),(34,34)), 0.6, 4.3)
			pygame.draw.arc(image, Config.black, ((862,84),(34,34)), -0.9, 2.8)
			pygame.draw.arc(image, Config.black, ((130,447),(34,34)), 2.2, 5.6)
			pygame.draw.arc(image, Config.black, ((499,80),(28,28)), 0.2, math.pi-0.2)
			pygame.draw.arc(image, Config.black, ((499,456),(28,28)), -math.pi+0.2,-0.2)
			pygame.draw.arc(image, Config.black, ((862,447),(34,34)), -2.5, 1.1)

			image.set_colorkey((128,128,128))
			self.image = image
			self.rect = self.image.get_rect()
			self.rect.center = (Config.display_width/2, Config.display_height/2)
			self.mask = pygame.mask.from_surface(self.image)	

class Ball(pygame.sprite.Sprite):
	ballLst = ["x" for x in range(15)]
	sizeX = 23
	sizeY = 23
	velLst = [0 for i in range(16)]
	goalLst = []
	instantGoal = False
	notfoal = False

	def __init__(self, x = 500 , y = 300, num = 0):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.x = x
		self.y = y

		self.accel = 29
		self.vel = 0
		self.dx = 0
		self.dy = 0
		self.num = num
		self.rotate = 0
		self.cueBallCol = False
		self.wallbounce = False
		self.ballCol = True
		self.enableCueCol = True
		self.enableBallCol = True
		self.text = None
		self.ballColLst = None

		image = pygame.Surface((Ball.sizeX,Ball.sizeY), pygame.SRCALPHA, 32)
		image = image.convert_alpha()
		if self.num == 0:
			ballImg = pygame.image.load("balls/white.png")
		elif self.num == 8:
			ballImg = pygame.image.load("balls/black.png")
		else:
			ballImg = pygame.image.load("balls/%d.png" % (self.num))

		if self.num == 0:
			self.group = 0
		elif self.num == 8:
			self.group = 3
		elif self.num <= 7:
			self.group = 1
		else: self.group = 2

		ballImg = pygame.transform.scale(ballImg, (Ball.sizeX, Ball.sizeY))
		image.blit(ballImg,(0,0))
		self.image = image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.mask = pygame.mask.from_surface(self.image)

	def move(self,seconds):

		# ---- handle collision with the cue ball
		cueBallCollisionLst = pygame.sprite.spritecollide(self, CueBall.groups[0], False, pygame.sprite.collide_mask)
		if cueBallCollisionLst and self.enableCueCol:
			Ball.notfoal = True
			if GameStatus.turn == "player" and GameStatus.playerGroup != None and self.group != GameStatus.playerGroup:
				self.text = Text((Config.display_width/2,Config.display_height/2),"foul")
			Ball.velLst[self.num] = self.vel
			self.enableCueCol = False
			dy = CueBall.y - self.y
			dx = self.x - CueBall.x
			if GameStatus.mode == "AI" and GameStatus.turn == "computer":
				collisionAngle = math.atan2(dy,dx)
				if abs(collisionAngle)>150: collisionAngle *= 0.85
			else:collisionAngle = math.atan2(dy,dx)
			selfvel_x = self.vel*math.cos(self.rotate-collisionAngle)			
			selfvel_y = self.vel*math.sin(self.rotate-collisionAngle)			
			cuevel_x = CueBall.vel*math.cos(math.radians(CueBall.rotate)-collisionAngle)
			cuevel_y = CueBall.vel*math.sin(math.radians(CueBall.rotate)-collisionAngle)
			temp_selfvel_x = cuevel_x
			temp_cuevel_x = selfvel_x
			temp_selfvel_y = selfvel_y
			temp_cuevel_y = cuevel_y
			final_selfvel_x = math.cos(collisionAngle) * temp_selfvel_x + math.cos(collisionAngle + math.pi/2) * temp_selfvel_y 
			final_selfvel_y = math.sin(collisionAngle) * temp_selfvel_x + math.sin(collisionAngle + math.pi/2) * temp_selfvel_y
			final_cuevel_x = math.cos(collisionAngle) * temp_cuevel_x + math.cos(collisionAngle + math.pi/2) * temp_cuevel_y
			final_cuevel_y = math.sin(collisionAngle) * temp_cuevel_x + math.sin(collisionAngle + math.pi/2) * temp_cuevel_y

			self.cueBallCol = True
			CueBall.ballCol = True

			self.x += 4*math.cos(collisionAngle)
			self.y -= 4*math.sin(collisionAngle)
			CueBall.x -= 4*math.cos(collisionAngle)
			CueBall.y += 4*math.sin(collisionAngle)

			self.vel = math.sqrt(final_selfvel_x**2+final_selfvel_y**2)*1.4
			self.rotate = math.atan2(final_selfvel_y,final_selfvel_x)
			
			CueBall.vel = math.sqrt(final_cuevel_x**2+final_cuevel_y**2)

			if GameStatus.turn == "player" and GameStatus.mode == "AI":
				if Cue.spin == "down slight":
					CueBall.vel -= 40
				if Cue.spin == "down hard":
					CueBall.vel -= 60
				if Cue.spin == "up slight":
					CueBall.vel += 10
				if Cue.spin == "up hard":
					CueBall.vel += 30

			CueBall.rotate = math.degrees(math.atan2(final_cuevel_y,final_cuevel_x))

		ncueBallCollisionLst = pygame.sprite.spritecollide(self, CueBall.groups[0], False, pygame.sprite.collide_mask)
		if ncueBallCollisionLst == []:
			self.enableCueCol = True
			
		# ----- handle collision with other balls
		otherCol = pygame.sprite.spritecollide(self, Ball.groups[0], False, pygame.sprite.collide_mask)
		otherCol.remove(self)

		if otherCol:
			for ball in otherCol:
				if self.num != 0 and ball.num != 0:
					dy = ball.y - self.y
					dx = self.x - ball.x
					collisionAngle = math.atan2(dy,dx)
					selfvel_x = self.vel*math.cos(self.rotate-collisionAngle)			
					selfvel_y = self.vel*math.sin(self.rotate-collisionAngle)			
					othervel_x = ball.vel*math.cos(ball.rotate-collisionAngle)			
					othervel_y = ball.vel*math.sin(ball.rotate-collisionAngle)			
					temp_selfvel_x = othervel_x
					temp_othervel_x = selfvel_x
					temp_selfvel_y = selfvel_y
					temp_othervel_y = othervel_y
					final_selfvel_x = math.cos(collisionAngle) * temp_selfvel_x + math.cos(collisionAngle + math.pi/2) * temp_selfvel_y
					final_selfvel_y = math.sin(collisionAngle) * temp_selfvel_x + math.sin(collisionAngle + math.pi/2) * temp_selfvel_y
					final_othervel_x = math.cos(collisionAngle) * temp_othervel_x + math.cos(collisionAngle + math.pi/2) * temp_othervel_y
					final_othervel_y = math.sin(collisionAngle) * temp_othervel_x + math.sin(collisionAngle + math.pi/2) * temp_othervel_y

					self.ballCol = True
					ball.ballCol = True

					self.x += 2*math.cos(collisionAngle)
					self.y -= 2*math.sin(collisionAngle)
					ball.x -= 2*math.cos(collisionAngle)
					ball.y += 2*math.sin(collisionAngle)

					self.vel = math.sqrt(final_selfvel_x**2+final_selfvel_y**2)
					self.rotate = math.atan2(final_selfvel_y,final_selfvel_x)
					

					ball.vel = math.sqrt(final_othervel_x**2+final_othervel_y**2)*1.2
					ball.rotate = math.atan2(final_othervel_y,final_othervel_x)

		# ---- handle wall bounce
		collisionLst = pygame.sprite.spritecollide(self, Wall.groups[0], False, pygame.sprite.collide_mask)
		if collisionLst:
			if collisionLst[0].name == "top":
				self.wallbounce = True
				self.y += 2
				self.rotate *= -1
				self.vel *= 0.7
			if collisionLst[0].name == "bottom":
				self.wallbounce = True
				self.y -= 2
				self.rotate *= -1
				self.vel *= 0.7
			if collisionLst[0].name == "left":
				self.wallbounce = True
				self.x += 2
				self.rotate = math.pi-self.rotate
				self.vel *= 0.7
			if collisionLst[0].name == "right":
				self.wallbounce = True
				self.x -= 2
				self.rotate = math.pi-self.rotate 
				self.vel *= 0.7

		# ---- go in to holes ----
		holeLst = pygame.sprite.spritecollide(self, Hole.groups[0], False, pygame.sprite.collide_mask)
		if holeLst:
			Ball.instantGoal = True
			self.vel = 0
			Ball.goalLst.append(self)
			if GameStatus.turn == "computer":
				if self.num == 8:
					GameStatus.gameWon = "player"
				if GameStatus.computerGroup == None:
					GameStatus.computerGoal = True
					GameStatus.computerGroup = self.group
					if self.group == 1:
						GameStatus.playerGroup = 2
					else: GameStatus.playerGroup = 1
				if self.group == GameStatus.computerGroup:
					GameStatus.computerGoal = True
			else:
				if self.num == 8:
					GameStatus.gameWon = "computer"
				if GameStatus.playerGroup == None:
					GameStatus.playerGoal = True
					GameStatus.playerGroup = self.group
					if self.group == 1:
						GameStatus.computerGroup = 2
					else: GameStatus.computerGroup = 1
				if self.group == GameStatus.playerGroup:
					GameStatus.playerGoal = True
			
			self.kill()

		distance = self.vel * seconds
		if self.vel >= 0:
			self.vel -= self.accel*seconds
		dx = distance*math.cos(self.rotate)*1.5
		dy = distance*math.sin(self.rotate)*1.5
		self.x += dx
		self.y -= dy
		if self.vel<0:
			self.vel = 0

	def update(self,seconds):
		self.move(seconds)
		if GameStatus.turn == "computer" and self.text != None:
			self.text.kill()
			self.text = None
		Ball.velLst[self.num] = self.vel
		self.rect.centerx = self.x
		self.rect.centery = self.y
		self.mask = pygame.mask.from_surface(self.image)

class CueBall(Ball):
	x = 190
	y = 190
	cueCollision = False
	vel = 90
	accel = 22
	dx = 0
	dy = 0
	wallbounce = False
	rotate = 0
	ballCol = False
	instantCollision = False

	def __init__(self,father,num):
		pygame.sprite.Sprite.__init__(self,self.groups)
		Ball.__init__(self,num=num)
		self.father = father
		self.num = 0
		self.rect.center = (200,200)

	def move(self,seconds):
		if CueBall.cueCollision == True and CueBall.wallbounce == False and CueBall.ballCol == False:
			distance = CueBall.vel * seconds
			if CueBall.vel >= 0:
				CueBall.vel -= CueBall.accel*seconds
			CueBall.dx = distance*math.cos(math.radians(self.father.rotate))
			CueBall.dy = distance*math.sin(math.radians(self.father.rotate))
			CueBall.x += CueBall.dx
			CueBall.y -= CueBall.dy
			CueBall.rotate = self.father.rotate
			

		# ------- bounce with walls --------

		collisionLst = pygame.sprite.spritecollide(self, Wall.groups[0], False, pygame.sprite.collide_mask)
		if collisionLst:
			if collisionLst[0].name == "top":
				CueBall.wallbounce = True
				CueBall.y += 2
				CueBall.rotate *= -1
			if collisionLst[0].name == "bottom":
				CueBall.wallbounce = True
				CueBall.y -= 2
				CueBall.rotate *= -1
			if collisionLst[0].name == "left":
				CueBall.wallbounce = True
				CueBall.x += 2
				CueBall.rotate = 180-CueBall.rotate
			if collisionLst[0].name == "right":
				CueBall.wallbounce = True
				CueBall.x -= 2
				CueBall.rotate = 180-CueBall.rotate 

		# ----- go into holes -----
		holeLst = pygame.sprite.spritecollide(self, Hole.groups[0], False, pygame.sprite.collide_mask)
		if holeLst:
			CueBall.vel = 0
			CueBall.x = 10000
			CueBall.y = 10000
			pygame.time.wait(2000)
			CueBall.x = 200
			CueBall.y = 200

		if CueBall.cueCollision == True:
			distance = CueBall.vel * seconds
			if CueBall.vel >= 0:
				CueBall.vel -= CueBall.accel*seconds
			dx = distance*math.cos(math.radians(CueBall.rotate))
			dy = distance*math.sin(math.radians(CueBall.rotate))
			CueBall.x += dx
			CueBall.y -= dy
					

		if CueBall.cueCollision == False and CueBall.vel <= 0:
			CueBall.vel = 90


	def update(self,seconds):
		self.move(seconds)
		if (GameStatus.turn == "player") or (GameStatus.mode == "Single" and GameStatus.turn == "computer"):
			if pygame.mouse.get_pressed()[0]:
				self.scale = self.father.scale
				if GameStatus.cue == 0:
					CueBall.vel += self.scale*0.13
				elif GameStatus.cue == 1:
					CueBall.vel += self.scale*0.15
				elif GameStatus.cue == 2:
					CueBall.vel += self.scale*0.17
				elif GameStatus.cue == 3:
					CueBall.vel += self.scale*0.2
									
				if self.scale == 3:
					CueBall.vel = 90
		else: 
			if CueBall.cueCollision == False:
				CueBall.vel = 70 + Cue.totalDist * 0.17

		collisionLst = pygame.sprite.spritecollide(self, Cue.groups[0], False, pygame.sprite.collide_mask)
		if collisionLst:
			CueBall.cueCollision = True
			CueBall.instantCollision = True
		else:
			CueBall.instantCollision = False

		self.x = CueBall.x
		self.y = CueBall.y
		self.rect.centerx = CueBall.x
		self.rect.centery = CueBall.y
		Ball.velLst[self.num] = CueBall.vel
		self.mask = pygame.mask.from_surface(self.image)


class Table(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.x = Config.edgeX
		self.y = Config.edgeY
		self.image = Config.tableImg
		self.rect = (Config.edgeX,Config.edgeY,Config.display_width,Config.display_height)

class Cue(pygame.sprite.Sprite):
	# All cue pics are taken from: https://www.parriscues.com/products/category/limited_edition/
	CueList = ["classical.png","arrow.png","stripe.png","master.png"]
	sizeX = 580
	sizeY = 128
	rotate = 0
	turnSpeed = 10
	start = True
	shoot = False
	totalDist = None
	spin = None

	def __init__(self, x = Config.display_width/3, y = Config.display_height/2, n = 0, rotate = 0):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.type = Cue.CueList[n]
		self.posx = x
		self.posy = y
		self.barx = x
		self.bary = y
		self.rotate = rotate
		Cue.shoot = False
		self.scale = 3
		self.accel = 100
		self.offset = 0
		self.auto = False
		self.ray = self.makeRay()
		self.text = None

		image = pygame.Surface((Cue.sizeX*2+7,Cue.sizeY))
		image.fill((128,128,128))
		cueImage = pygame.image.load("cues/"+self.type)
		cueImage = pygame.transform.scale(cueImage,(Cue.sizeX,Cue.sizeY))
		image.blit(cueImage,(0,0))
		image.set_colorkey((128,128,128))
		self.image0 = image.convert_alpha()
		self.image = image.convert_alpha()

		self.rect = self.image0.get_rect()
		self.rect.center = (200,Config.display_height/2)
		self.mask = pygame.mask.from_surface(self.image)

		# --- AI init ----
		self.min_dist = None
		self.min_ball = None
		self.near_dist = None
		self.near_hole = None
		self.AIauto = False
		self.timeCorrection = False

	def makeRay(self):
		return Ray((CueBall.x,CueBall.y),(CueBall.x+1000*math.cos(math.radians(self.rotate)),CueBall.y-1000*math.sin(math.radians(self.rotate))),10)			

	# check if there's any other object between ball and obj2
	@staticmethod
	def checkBlocked(ball,obj2):
		if isinstance(obj2,tuple):
			x,y = obj2
			ray = Ray((x,y),(ball.x,ball.y),15)
		else:
			ray = Ray((obj2.x,obj2.y),(ball.x,ball.y),15)
		blockLst = pygame.sprite.spritecollide(ray, ball.groups[0], False, pygame.sprite.collide_mask)
		if blockLst == []:
			ray.kill()
			return False
		else:
			for eachball in blockLst:
				if eachball != ball:
					ray.kill()
					return True
			ray.kill()
			return False
	# check if only the black ball has left
	def checkBlack(self,ballLst):
		count = 0
		if GameStatus.turn == "computer":
			if GameStatus.computerGroup == None:
				return False
			for ball in ballLst:
				if ball.group == GameStatus.computerGroup or ball.num == 8:
					count+=1
			if count == 1:
				return True
			else:
				return False
		else:return False


	def isLegalAngle(self,aimBall,hole):
		hx,hy = hole
		angleToTest = math.degrees(math.atan2(aimBall.y-hy,hx-aimBall.x))
		if angleToTest < 0:
			angleToTest = 360+angleToTest
		smallestAngle = self.rotate-80
		biggestAngle = self.rotate+80
		if smallestAngle < angleToTest < biggestAngle:
			return True
		return False

	def player(self,seconds):
		self.barx = CueBall.x
		self.bary = CueBall.y

		if CueBall.cueCollision == True:
			self.ray.kill()
			for ballIndex in range(len(Ball.velLst)):
				if Ball.velLst[ballIndex] > 0:
					break
				if ballIndex == len(Ball.velLst)-1 and CueBall.vel<=0:
					Ball.instantGoal = False
					pygame.time.wait(500)
					if GameStatus.mode == "AI":
						print(Ball.notfoal)
						if Ball.notfoal == False:
							self.text = Text((Config.display_width/2,Config.display_height/2),"foul")
						if GameStatus.playerGoal == False:
							GameStatus.playerFail = True
						else: GameStatus.playerWinRound = True
					if GameStatus.mode == "Single":
						if GameStatus.turn == "player":
							if GameStatus.playerGoal == False:
								GameStatus.playerFail = True
							else: GameStatus.playerWinRound = True
						if GameStatus.turn == "computer":
							if GameStatus.computerGoal == False:
								GameStatus.computerFail = True
							else: GameStatus.computerWinRound = True
					self.auto = True
					Cue.shoot = False
					CueBall.cueCollision = False
					CueBall.wallbounce = False
					CueBall.ballCol = False

		if CueBall.vel >0:
			self.auto = False

		if Cue.shoot == False:
			# ------------ keyboard --------------
			pressedkeys = pygame.key.get_pressed()
			# -------- manual rotate ----------
			self.turn = 0
			if pressedkeys[pygame.K_a]:
				self.turn += 1
				Cue.turnSpeed += 1
			elif pressedkeys[pygame.K_d]:
				self.turn -= 1
				Cue.turnSpeed += 1
			else:
				Cue.turnSpeed = 10

			# -------- do rotate ---------
			self.rotate += self.turn * Cue.turnSpeed * seconds
			self.rotate %= 360
			Cue.rotate = math.radians(self.rotate)
			ox,oy = self.image0.get_rect().center
			self.image = pygame.transform.rotate(self.image0, self.rotate)
			self.rect = self.image.get_rect()
			self.rect.center = ox,oy
			
			self.rect.centerx = round(self.posx)
			self.rect.centery = round(self.posy)
			self.mask = pygame.mask.from_surface(self.image)


		# -------- Power Bar ----------
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if click[0] and not(955<mouse[0]<1005 and 375<mouse[1]<425):
			self.scale += int(self.accel*seconds)
			if self.scale >= 56:
				self.scale = 3
			Cue.shoot = True
			PowerBar(self)
			PowerDisplay(self,self.scale)
			if self.offset < 3:
				self.offset += 0.2
				self.posx -= self.offset*math.cos(math.radians(self.rotate))
				self.posy += self.offset*math.sin(math.radians(self.rotate))
			self.auto = False
			GameStatus.playerGoal = False
		
		elif not click[0]:
			self.scale = 40
			if self.offset > 0:
				self.offset -= 0.06
				self.posx += self.offset*math.cos(math.radians(self.rotate))
				self.posy -= self.offset*math.sin(math.radians(self.rotate))
				self.auto = False


		# --------- Auto Relocation -----------

		if self.auto == True or Cue.start == True:
			self.posx = CueBall.x
			self.posy = CueBall.y
			self.auto = False
			Cue.start = False

		self.rect.centerx = round(self.posx)
		self.rect.centery = round(self.posy)

	def update(self,seconds):
		if GameStatus.turn == "computer":
			if GameStatus.computerWinRound == True:
				GameStatus.turn = "computer"
				Ball.notfoal = False
				self.scale = 3
				self.timeCorrection = False
				self.ray = self.makeRay()
				GameStatus.computerGoal = False
				GameStatus.computerFail = False
				GameStatus.playerFail = False
				GameStatus.computerWinRound = False
				GameStatus.playerWinRound = False
			elif GameStatus.computerFail == True:
				GameStatus.turn = "player"
				Ball.notfoal = False
				self.ray = self.makeRay()
				GameStatus.computerFail = False
				GameStatus.playerFail = False
				GameStatus.computerWinRound = False
				GameStatus.playerWinRound = False
		if GameStatus.turn == "player":
			if GameStatus.playerWinRound == True:
				GameStatus.turn = "player"
				Ball.notfoal = False
				self.ray = self.makeRay()
				GameStatus.computerFail = False
				GameStatus.playerFail = False
				GameStatus.computerWinRound = False
				GameStatus.playerWinRound = False
			elif GameStatus.playerFail == True:
				if self.text != None:
					self.text.kill()
					pygame.time.delay(1000)
					Ball.notfoal = False
				GameStatus.turn = "computer"
				self.scale = 3
				self.posx = CueBall.x
				self.posy = CueBall.y
				self.timeCorrection = False
				self.ray = self.makeRay()
				GameStatus.computerFail = False
				GameStatus.playerFail = False
				GameStatus.computerWinRound = False
				GameStatus.playerWinRound = False


		if GameStatus.turn == "player":
			self.player(seconds)

			count = 0
			lst = Ball.groups[0].sprites()
			
			if GameStatus.playerGroup == None:
				count = 7

			for ball in lst:
				if ball.num == 8:
					count = 7
				if ball.group == GameStatus.playerGroup:
					count += 1
			if count == 0 and GameStatus.gameWon == None:				
				GameStatus.gameWon = "player"



		################# AI ##################

		# First, find the nearest unblocked ball to the CueBall
		# Then, find the nearest unblocked hole to the nearest unblocked ball
		# Calculate the angle
		# Make the shot

		if GameStatus.turn == "computer":
			if GameStatus.mode == "AI":

				ballLst = Ball.groups[0].sprites()			
				if Cue.shoot == False:
					if not self.checkBlack(ballLst):	
						for ball in ballLst:
							if ball.num == 8:
									continue
							if GameStatus.computerGroup != None and ball.group != GameStatus.computerGroup:
								continue
							elif Cue.checkBlocked(ball,CueBall):
								continue
							cur_dist = (CueBall.x-ball.x)**2+(CueBall.y-ball.y)**2
							if (self.min_dist == None or cur_dist < self.min_dist):
								self.min_dist = cur_dist
								self.min_ball = ball
								continue

					elif self.checkBlack(ballLst): 
						for ball in ballLst:
							if ball.num == 8:
								self.min_ball = ball

				aim_x, aim_y = self.min_ball.x, self.min_ball.y

				if CueBall.cueCollision == False:
					holeLst = [(143,95),(883,95),(143,470),(883,470),(512,83),(512,482)]
					for hole in holeLst:
						x,y = hole
						if Cue.checkBlocked(self.min_ball,hole):
							continue
						if not self.isLegalAngle(self.min_ball,hole):
							continue
						distance = (x-aim_x)**2+(y-aim_y)**2
						if self.near_dist == None or distance <= self.near_dist:
							self.near_dist = distance
							self.near_hole = hole
							continue

					if self.near_hole == None:
						holeLst = [(143,95),(883,95),(143,470),(883,470),(512,83),(512,482)]
						for hole in holeLst:
							x,y = hole
							if self.isLegalAngle(self.min_ball,hole):
								self.near_hole = hole

				hole_x, hole_y = self.near_hole
				#print(self.min_ball.num,self.near_hole)

				if CueBall.cueCollision == False:
					dist1 = math.sqrt((CueBall.x-self.min_ball.x)**2+(CueBall.y-self.min_ball.y)**2)
					dist2 = math.sqrt((self.min_ball.x-hole_x)**2+(self.min_ball.y-hole_y)**2)
					Cue.totalDist = dist1+dist2

				if CueBall.cueCollision == True:
					for ballIndex in range(len(Ball.velLst)):
						if Ball.velLst[ballIndex] > 0:
							break
						if ballIndex == len(Ball.velLst)-1 and CueBall.vel<=0:
							Ball.instantGoal = False
							pygame.time.wait(500)
							if GameStatus.computerGoal == False:
								GameStatus.computerFail = True
							else: GameStatus.computerWinRound = True
							self.AIauto = True
							Cue.shoot = False
							self.min_dist = None
							self.near_dist = None
							CueBall.cueCollision = False
							CueBall.wallbounce = False
							CueBall.ballCol = False



				if CueBall.cueCollision == False:
					finalAngle = math.atan2(hole_y-aim_y,aim_x-hole_x)
					dx = 15*math.cos(finalAngle)
					dy = 15*math.sin(finalAngle)
					temp_x = aim_x+dx
					temp_y = aim_y-dy

					aimAngle = -math.degrees(math.atan2(temp_y-CueBall.y,temp_x-CueBall.x))
					if aimAngle < 0:
						aimAngle = 360+aimAngle
					self.rotate = aimAngle
					Cue.rotate = math.radians(aimAngle)
					ox,oy = self.image0.get_rect().center
					self.image = pygame.transform.rotate(self.image0, self.rotate)
					self.rect = self.image.get_rect()
					self.rect.center = ox,oy

					if self.scale >= 40:
						self.scale = 40

					if seconds>=0.2:
						seconds = 0.03
					self.scale += int(self.accel*seconds)*0.7
			

				if CueBall.cueCollision == False and self.timeCorrection == False:
					if self.scale < 40:
						self.offset += 1
						self.posx -= self.offset*math.cos(math.radians(self.rotate))
						self.posy += self.offset*math.sin(math.radians(self.rotate))

					if self.scale > 40:
						self.offset -= 0.1
						self.posx += self.offset*math.cos(math.radians(self.rotate))
						self.posy -= self.offset*math.sin(math.radians(self.rotate))

				if CueBall.instantCollision == True:
					self.ray.kill()
					self.timeCorrection = True
					self.offset = 0
					self.scale = 3

				if self.AIauto == True or Cue.start == True:
					self.posx = CueBall.x
					self.posy = CueBall.y
					self.AIauto = False
					Cue.start = False

				count = 0
				lst = Ball.groups[0].sprites()
				if GameStatus.computerGroup == None:
					count = 7
				for ball in lst:
					if ball.num == 8:
						count = 7
					if ball.group == GameStatus.computerGroup:
						count+=1

				if count == 0:
					GameStatus.gameWon = "computer"

				self.rect.centerx = round(self.posx)
				self.rect.centery = round(self.posy)
				self.mask = pygame.mask.from_surface(self.image)
			
			elif GameStatus.mode == "Single":
				self.player(seconds)

				count = 0
				lst = Ball.groups[0].sprites()
				if GameStatus.computerGroup == None:
					count = 7
				for ball in lst:
					if ball.num == 8:
						count = 7
					if ball.group == GameStatus.computerGroup:
						count+=1
				if count == 0 and GameStatus.gameWon == None:
					GameStatus.gameWon = "computer"


class Ray(pygame.sprite.Sprite):
	def __init__(self,start,end,width):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.sx,self.sy = start
		self.ex,self.ey = end
		length = math.sqrt((self.ey-self.sy)**2+(self.ex-self.sx)**2)
		self.height = width
		image = pygame.Surface((2*length,self.height))
		image.fill((128,128,128))
		pygame.draw.rect(image, Config.ray, (0,0,length,self.height))
		image.set_colorkey((128,128,128))
		self.image = image
		self.image0 = image
		self.rect = self.image.get_rect()
		angle = math.degrees(math.atan2(self.ey-self.sy,self.sx-self.ex))
		ox,oy = self.image0.get_rect().center
		self.image = pygame.transform.rotate(self.image0, angle)
		self.rect = self.image.get_rect()
		self.rect.center = ox,oy
		self.rect.center = (self.sx,self.sy)
		self.mask = pygame.mask.from_surface(self.image)

	def rotate(self):
		length = int(math.sqrt((self.ey-self.sy)**2+(self.ex-self.sx)**2))
		self.image0 = pygame.transform.scale(self.image0, (2*length, self.height))
		angle = math.degrees(math.atan2(self.ey-self.sy,self.sx-self.ex))
		ox,oy = self.image0.get_rect().center
		self.image = pygame.transform.rotate(self.image0, angle)
		self.rect = self.image.get_rect()
		self.rect.center = ox,oy
		self.rect.center = (self.sx,self.sy)
		self.mask = pygame.mask.from_surface(self.image)

	def update(self,seconds):
		self.sx,self.sy = CueBall.x, CueBall.y
		self.ex,self.ey = (CueBall.x+1000*math.cos(Cue.rotate),CueBall.y-1000*math.sin(Cue.rotate))
		self.rotate()
		lst =  pygame.sprite.spritecollide(self, Ball.groups[0], False, pygame.sprite.collide_mask)
		if lst:
			nearDist = None
			for ball in lst:
				dist = int(math.sqrt((ball.y-self.sy)**2+(ball.x-self.sx)**2))
				if nearDist == None or dist <= nearDist:
					nearDist = dist
					self.ex,self.ey = ball.x,ball.y
					self.rotate()
					angle = math.degrees(Cue.rotate)+180
					ox,oy = self.image0.get_rect().center
					self.image = pygame.transform.rotate(self.image0, angle)
					self.rect = self.image.get_rect()
					self.rect.center = ox,oy
					self.rect.center = (self.sx,self.sy)
					self.mask = pygame.mask.from_surface(self.image)


class PowerBar(pygame.sprite.Sprite):
	sizeX = 20
	sizeY = 60
	dist = 100

	def __init__(self,father):
		pygame.sprite.Sprite.__init__(self,self.groups)
		image = pygame.Surface((PowerBar.sizeX, PowerBar.sizeY))
		image.fill(Config.darkGrey)
		pygame.draw.rect(image,Config.grey,(2,2,16,56))
		self.image = image.convert_alpha()
		self.rect = self.image.get_rect()
		self.father = father

		if 0<=father.rotate<90 or 180<=father.rotate<270:
			self.rect.centerx = self.father.barx - math.cos(math.radians(father.rotate))*PowerBar.dist - 50
			self.rect.centery = self.father.bary + math.sin(math.radians(father.rotate))*PowerBar.dist - 50
		elif 90<=father.rotate<180 or 270<=father.rotate<=360:
			self.rect.centerx = self.father.barx - math.cos(math.radians(father.rotate))*PowerBar.dist + 50
			self.rect.centery = self.father.bary + math.sin(math.radians(father.rotate))*PowerBar.dist - 50

	def update(self,seconds):
		if not pygame.mouse.get_pressed()[0]:
			self.kill()

class PowerDisplay(PowerBar):
	def __init__(self,father,scale):
		PowerBar.__init__(self,father)
		self.scale = scale

		image = pygame.Surface((16,56))
		image.fill(Config.grey)
		pygame.draw.rect(image,Config.red,(0,56-self.scale,16,self.scale))
		image.set_colorkey(Config.grey)
		self.image = image.convert_alpha()
		self.rect.centerx = self.rect.centerx+2
		self.rect.centery = self.rect.centery+2

	def update(self,seconds):
		if not pygame.mouse.get_pressed()[0]:
			self.kill()
		else:
			self.image = pygame.transform.scale(self.image,(16,self.scale))

class GameStatusDisplay(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.image = GameStatusDisplay.drawSlot()
		self.rect = self.image.get_rect()
		self.rect.center = (500,40)

	@staticmethod
	def drawSlot():
		image = pygame.Surface((1000,50))
		image.fill((128,128,128))
		slotImg = pygame.image.load("slot.png")
		slotImg = pygame.transform.scale(slotImg, (200,40))
		image.blit(slotImg, (120,0))
		image.blit(slotImg, (700,0))
		image.set_colorkey((128,128,128))
		image.convert_alpha()
		return image


	def update(self,seconds):
		image = GameStatusDisplay.drawSlot()
		compStartX = 130
		playStartX = 710
		if Ball.instantGoal == True:
			for ball in Ball.goalLst:
				if ball.num == 8:
					ballImg = pygame.image.load("balls/black.png")
				else:
					ballImg = pygame.image.load("balls/%d.png" % (ball.num))
				ballImg = pygame.transform.scale(ballImg, (23,23))
				if ball.group == GameStatus.computerGroup:
					image.blit(ballImg,(compStartX,10))
					self.image = image
					compStartX += 20
				if ball.group == GameStatus.playerGroup:
					image.blit(ballImg,(playStartX,10))
					self.image = image
					playStartX += 20

class SpinDisplay(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.image = SpinDisplay.drawBall()
		self.rect = self.image.get_rect()
		self.rect.center = (980,400)	
	@staticmethod
	def drawBall(center = 1):
		img = pygame.Surface((50,50))
		img.fill((127,127,127))
		ballImg = pygame.image.load("balls/white.png")
		ballImg = pygame.transform.smoothscale(ballImg, (50,50))
		img.blit(ballImg,(0,0))
		if center == 1:
			pygame.draw.circle(img, Config.red, (25,25), 2)
		img.set_colorkey((127,127,127))
		img.convert_alpha()
		return img

	def update(self,seconds):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if 955<mouse[0]<1005 and 388<mouse[1]<394:
			if click[0]:
				img = SpinDisplay.drawBall(0)
				pygame.draw.circle(img, Config.red, (25,18), 2)
				self.image = img
				Cue.spin = "up slight"
		if 955<mouse[0]<1005 and 375<mouse[1]<388:
			if click[0]:
				img = SpinDisplay.drawBall(0)
				pygame.draw.circle(img, Config.red, (25,10), 2)
				self.image = img
				Cue.spin = "up hard"
		if 955<mouse[0]<1005 and 406<mouse[1]<412:
			if click[0]:
				img = SpinDisplay.drawBall(0)
				pygame.draw.circle(img, Config.red, (25,32), 2)
				self.image = img
				Cue.spin = "down slight"
		if 955<mouse[0]<1005 and 412<mouse[1]<425:
			if click[0]:
				img = SpinDisplay.drawBall(0)
				pygame.draw.circle(img, Config.red, (25,40), 2)
				self.image = img
				Cue.spin = "down hard"
		if 955<mouse[0]<1005 and 394<mouse[1]<406:
			if click[0]:
				img = SpinDisplay.drawBall(0)
				pygame.draw.circle(img, Config.red, (25,25), 2)
				self.image = img	
				Cue.spin = None

def gameLoop():
	screen = pygame.display.set_mode((Config.display_width,Config.display_height))
	background = pygame.Surface((screen.get_size()))
	background.fill(Config.black)
	#http://bensprout.com/wp-content/uploads/2016/10/floor-dark-wood-floors-seamless-dark-wood-floor-texture.jpg, http://bensprout.com/wp-content/uploads/2016/10/floor-dark-wood-floors-seamless-dark-wood-floor-texture.jpg
	floorImg = pygame.image.load("floor.jpg")
	background.blit(floorImg, (0,0))

	crashed = False
	FPS = Config.fps
	clock = pygame.time.Clock()

	cueGroup = pygame.sprite.Group()
	tableGroup = pygame.sprite.Group()
	ballGroup = pygame.sprite.Group()
	wallGroup = pygame.sprite.Group()
	topWallGroup = pygame.sprite.Group()
	leftWallGroup = pygame.sprite.Group()
	rightWallGroup = pygame.sprite.Group()
	bottomWallGroup = pygame.sprite.Group()
	holeGroup = pygame.sprite.Group()
	cueBallGroup = pygame.sprite.Group()
	rayGroup = pygame.sprite.Group()
	textGroup = pygame.sprite.Group()
	gameStatusDisplayGroup = pygame.sprite.Group()
	spinDisplayGroup = pygame.sprite.Group()
	allGroups = pygame.sprite.LayeredUpdates()

	Table._layer = 3
	TopWall._layer = 4
	Ray._layer = 5
	Ball._layer = 6
	CueBall._layer = 7
	Cue._layer = 8
	PowerBar._layer = 9
	RightWall._layer = 10
	BottomWall._layer = 11
	LeftWall._layer = 12
	Hole._layer = 13
	Text._layer = 14
	GameStatusDisplay._layer = 15
	SpinDisplay._layer = 16

	Cue.groups = cueGroup,allGroups
	Table.groups = tableGroup,allGroups
	Ball.groups = ballGroup,allGroups
	PowerBar.groups = allGroups
	CueBall.groups = cueBallGroup,allGroups
	Wall.groups = topWallGroup,leftWallGroup,bottomWallGroup,rightWallGroup,allGroups
	Hole.groups = holeGroup,allGroups
	Ray.groups = rayGroup,allGroups
	Text.groups = textGroup,allGroups
	GameStatusDisplay.groups = gameStatusDisplayGroup,allGroups
	SpinDisplay.groups = spinDisplayGroup,allGroups

	table = Table()
	cue = Cue(x = Config.display_width/3, y = Config.display_height/2, n = GameStatus.cue, rotate = 0)
	text = Text((500,30),"turn")
	slot = GameStatusDisplay()
	spin = SpinDisplay()

	ball1 = Ball(692,283,1)
	ball2 = Ball(709,275,2)
	ball3 = Ball(709,290,3)
	ball4 = Ball(725,264,4)
	ball5 = Ball(725,283,5)
	ball6 = Ball(725,301,6)
	ball7 = Ball(741,293,7)
	ball8 = Ball(741,275,8)
	ball9 = Ball(741,256,9)
	ball10 = Ball(741,312,10)
	ball11 = Ball(758,283,11)
	ball12 = Ball(758,302,12)
	ball13 = Ball(758,321,13)
	ball14 = Ball(758,264,14)
	ball15 = Ball(758,245,15)

	cueball = CueBall(cue,0)
	topwall = TopWall()
	leftwall = LeftWall()
	bottomwall = BottomWall()
	rightwall = RightWall()
	hole = Hole()

	text2 = Text((500,530),"type")

	while not crashed:
		milliseconds = clock.tick(Config.fps)  # milliseconds passed since last frame
		seconds = milliseconds / 1000.0
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
				pygame.quit()
				crashed = True
				sys.exit()

		if GameStatus.gameWon != None:
			crashed = True
			gameEnd()


		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		allGroups.clear(screen, background)
		allGroups.update(seconds)
		allGroups.draw(screen)

		#pygame.draw.rect(background, Config.darkGrey,(40,520,100,30))

		pygame.display.update()


	pygame.quit()

def main():
	pygame.init()
	splashScreen()


if __name__ == '__main__':
    main()
