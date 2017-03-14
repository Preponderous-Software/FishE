from textAdventure import Text_Adventure_Template
import time
import random
import sys
import math


template = Text_Adventure_Template()

class Game(object):

	def __init__(self):
		self.options = []
		
		self.day = 1
		self.time = 8
		
		self.fishCount = 0
		self.money = 0
		self.moneyInBank = 0 # need to be able to save this
		
		self.fishMultiplier = 1
		
		self.totalFishCaught = 0
		self.totalMoneyMade = 0
		self.hoursSpentFishing = 0
		self.moneyMadeFromInterest = 0
		self.timesGottenDrunk = 0
		self.moneyLostFromGambling = 0
		
		self.currentBet = 0

	def play(self):
		self.li = ["New Game", "Load Game"]
		self.input = template.showOptions("Welcome to the game!", "Would you like to start a new game or load your last save?", self.li, 999, 8, 999, 999)
		
		if self.input == "1":
			self.home("What would you like to do?")
			
		elif self.input == "2":
			self.loadGame()
			self.home("What would you like to do?")
		
	def increaseTime(self):
		self.time += 1
		
		if self.time > 23:
			self.time = 0
			
		if 0 <= self.time <= 7: # returns player home if it's late
			
			self.increaseDay()
			
			self.home("You were too tired to do anything else but go home and sleep. Good morning.")
			
	def increaseDay(self):
		self.time = 8
		self.day += 1
		
		self.saveGame()
		
		self.moneyInBank += int(math.ceil(self.moneyInBank * 0.10))
		self.moneyMadeFromInterest += int(math.ceil(self.moneyInBank * 0.10))
		self.totalMoneyMade += int(math.ceil(self.moneyInBank * 0.10))
			
	def saveGame(self):
		self.file = open("savefile.txt", 'w')
		
		self.file.write("%d" % self.day)
		
		self.file.write("\n%d" % self.fishCount)
		self.file.write("\n%d" % self.money)
		self.file.write("\n%d" % self.moneyInBank)
		
		self.file.write("\n%d" % self.fishMultiplier)
		
		self.file.write("\n%d" % self.totalFishCaught)
		self.file.write("\n%d" % self.totalMoneyMade)
		self.file.write("\n%d" % self.hoursSpentFishing)	
		self.file.write("\n%d" % self.moneyMadeFromInterest)
		self.file.write("\n%d" % self.timesGottenDrunk)		
		self.file.write("\n%d" % self.moneyLostFromGambling)
					
	def loadGame(self):
		with open("savefile.txt") as f:
			self.content = f.readlines()
				
		self.day = int(self.content[0])
		
		self.fishCount = int(self.content[1])
		self.money = int(self.content[2])
		self.moneyInBank = int(self.content[3])
		
		self.fishMultiplier = int(self.content[4])
		
		self.totalFishCaught = int(self.content[5])
		self.totalMoneyMade = int(self.content[6])
		self.hoursSpentFishing = int(self.content[7])
		self.moneyMadeFromInterest = int(self.content[8])
		self.timesGottenDrunk = int(self.content[9])
		self.moneyLostFromGambling = int(self.content[10])				

# LOCATIONS -------------------------------------------------------------------------------------------------------------------------	
	def home(self, p):		
		self.prompt = p
		self.li = ["Sleep", "See Stats", "Go to Docks"]
		self.input = template.showOptions("You sit at home, polishing one of your prized fishing poles.", self.prompt, self.li, self.day, self.time, self.money, self.fishCount)
		
		if self.input == "1":
			self.sleep()
		
		elif self.input == "2":
			self.seeStats()
			self.home("What would you like to do?")
		
		elif self.input == "3":
			self.increaseTime()
			self.docks("What would you like to do?")
				
	def docks(self, p):
		self.prompt = p
		self.li = ["Fish", "Go Home", "Go to Shop", "Go to Tavern", "Go to Bank"]
		self.input = template.showOptions("You breathe in the fresh air. Salty.", self.prompt, self.li, self.day, self.time, self.money, self.fishCount)
		
		if self.input == "1":
			self.fish()
			
		elif self.input == "2":
			self.increaseTime()
			self.home("What would you like to do?")
			
		elif self.input == "3":
			self.increaseTime()
			self.shop("What would you like to do?")
		
		elif self.input == "4":
			self.increaseTime()
			self.tavern("What would you like to do?")
			
		elif self.input == "5":
			self.increaseTime()
			self.bank("What would you like to do? Money in Bank: $%d" % self.moneyInBank)

	def shop(self, p):
		self.prompt = p
		self.li = ["Buy/Sell", "Go to Docks"]
		self.input = template.showOptions("The shopkeeper winks at you as you behold his collection of fishing poles.", self.prompt, self.li, self.day, self.time, self.money, self.fishCount)
		
		if self.input == "1":
			self.buysell("What would you like to do?")
			
		elif self.input == "2":
			self.increaseTime()
			self.docks("What would you like to do?")
	
	def tavern(self, p):
		self.prompt = p
		self.li = ["Get drunk ( $10 )", "Gamble", "Go to Docks"]
		self.input = template.showOptions("You sit at the bar, watching the barkeep clean a mug with a dirty rag.", self.prompt, self.li, self.day, self.time, self.money, self.fishCount)
		
		if self.input == "1":
			if self.money >= 10:
				self.getDrunk()
			else:
				self.tavern("You don't have enough money!")
		
		elif self.input == "2":
			self.gamble("What will the dice land on? Current Bet: $%d" % self.currentBet)
		
		elif self.input == "3":
			self.increaseTime()
			self.docks("What would you like to do?")
			
	def bank(self, p): # IN DEVELOPMENT
		self.prompt = p
		self.li = ["Make a Deposit", "Make a Withdrawal", "Go to docks"]
		self.input = template.showOptions("You're at the front of the line and the teller asks you what you want to do.", self.prompt, self.li, self.day, self.time, self.money, self.fishCount)
		
		if self.input == "1":
			if self.money > 0:
				self.deposit("How much would you like to deposit? Money: $%d" % self.money)
			else:
				self.bank("You don't have anything to deposit!")
		
		elif self.input == "2":
			if self.moneyInBank > 0:
				self.withdraw("How much would you like to withdraw? Money In Bank: $%d" % self.moneyInBank)
			else:
				self.bank("You don't have any money in the bank!")
			
		elif self.input == "3":
			self.increaseTime()
			self.docks("What would you like to do?")
			
# ACTIONS -------------------------------------------------------------------------------------------------------------------------	
	def sleep(self):
		if self.time > 20:			
			self.increaseDay()
			self.home("You had a good night's rest.")
		
		else:
			self.home("You're not tired!")
		
	def fish(self):
		template.lotsOfSpace()
		template.divider()
		
		print "Fishing... ",
		sys.stdout.flush()
		time.sleep(1)
		
		hours = random.randint(1, 10)
		
		for i in range(hours):
			print "><> ",
			sys.stdout.flush()
			time.sleep(1)
			self.increaseTime()
			self.hoursSpentFishing += 1
		
		self.fishCount += 1 * self.fishMultiplier
		self.totalFishCaught += 1 * self.fishMultiplier
		
		if self.fishMultiplier == 1:
		
			if hours == 1:
				self.docks("Nice catch! It only took %d hour!" % hours)
			else:
				self.docks("Nice catch! It only took %d hours!" % hours)
		else:
			if hours == 1:
				self.docks("You caught %d fish! It only took %d hour!" % (self.fishMultiplier, hours))
			else:
				self.docks("You caught %d fish! It only took %d hours!" % (self.fishMultiplier, hours))
				
	def buysell(self, p):
		self.prompt = p
		self.li = ["Sell Fish", "Buy Better Bait ( $50 )",  "Back"]
		self.input = template.showOptions("The shopkeeper waits for you to make a decision.", self.prompt, self.li, self.day, self.time, self.money, self.fishCount)
		
		if self.input == "1":
			self.money += self.fishCount * 5
			self.totalMoneyMade += self.fishCount * 5
			self.fishCount = 0
			
			self.buysell("You sold all of your fish!")
			
		elif self.input == "2":
			if self.money < 50:
				self.buysell("You don't have enough money!")
			else:
				self.fishMultiplier += 1
				self.money -= 50	
				self.buysell("You bought some better bait!")	
			
		elif self.input == "3":
			self.shop("What now, moneybags?")
	
		
	def seeStats(self):
		template.lotsOfSpace()
		template.divider()
		print "Total Fish Caught: %d " % self.totalFishCaught,
		print "| Total Money Made: $%d " % self.totalMoneyMade,
		print "| Hours Spent Fishing: %d" % self.hoursSpentFishing
		template.divider()
		print "Money Made From Interest: $%d" % self.moneyMadeFromInterest,
		print "| Times Gotten Drunk: %d" % self.timesGottenDrunk,
		print "| Money Lost Gambling: $%d" % self.moneyLostFromGambling	
		template.divider()
		raw_input(" [ CONTINUE ]")	
		
	def getDrunk(self):
		template.lotsOfSpace()
		template.divider()
		
		self.money -= 10
		
		for i in range(3):
			print "... ",
			sys.stdout.flush()
			time.sleep(1)
		
		self.timesGottenDrunk += 1
		
		self.increaseDay()
		self.home("Your head is pounding after last night.")
		
	def gamble(self, p):
		self.prompt = p
		self.li = ["1", "2", "3", "4", "5", "6", "Change Bet", "Back"]
		self.input = int(template.showOptions("Once you place your bet, the burly man in front of you will throw the dice.", self.prompt, self.li, self.day, self.time, self.money, self.fishCount))
				
		if 1 <= self.input <= 6 and self.currentBet > 0:
			self.diceThrow = random.randint(1,6)
			
			if self.input == self.diceThrow:
				self.money += self.currentBet
				self.totalMoneyMade += self.currentBet
				self.currentBet = 0
				self.gamble("You guessed correctly! Care to try again? Current Bet: $%d" % self.currentBet)
			else:
				self.money -= self.currentBet
				self.moneyLostFromGambling += self.currentBet
				self.currentBet = 0
				self.gamble("The dice rolled a %d! You lost your money! Care to try again? Current Bet: $%d" % (self.diceThrow, self.currentBet))
		
		elif self.input == 7:
			 self.changeBet("How much money would you like to bet? Money: $%d" % self.money)
		
		elif self.input == 8:
			self.tavern("What would you like to do?")
			
		else:
			self.gamble("You didn't bet any money! What will the dice land on? Current Bet: $%d" % self.currentBet)
			 
	def changeBet(self, p):
		self.prompt = p
		template.lotsOfSpace()
		template.divider()
		print self.prompt
		template.divider()
		
		try:
			self.amount = int(raw_input("> "))
		except ValueError:
			self.deposit("Try again. Money: $%d" % self.money)
			
		if self.amount <= self.money:
			self.currentBet = self.amount
		
			self.gamble("What will the dice land on? Current Bet: $%d" % self.currentBet)
		else:
			self.deposit("You don't have that much money on you! Money: $%d" % self.money)
		
	def deposit(self, p):
		self.prompt = p
		template.lotsOfSpace()
		template.divider()
		print self.prompt
		template.divider()
		
		try:
			self.amount = int(raw_input("> "))
		except ValueError:
			self.deposit("Try again. Money: $%d" % self.money)
			
		if self.amount <= self.money:
			self.moneyInBank += self.amount
			self.money -= self.amount
		
			self.bank("$%d deposited successfully." % self.amount)
		else:
			self.bank("You don't have that much money on you!")
		
	
	def withdraw(self, p):
		self.prompt = p
		template.lotsOfSpace()
		template.divider()
		print self.prompt
		template.divider()
		
		try:
			self.amount = int(raw_input("> "))
		except ValueError:
			self.withdraw("Try again. Money In Bank: $%d" % self.moneyInBank)
			
		if self.amount <= self.moneyInBank:
			self.money += self.amount
			self.moneyInBank -= self.amount
			
		
			self.bank("$%d withdrawn successfully." % self.amount)
		else:
			self.bank("You don't have that much money in the bank!")
		

FishE = Game()
FishE.play()
