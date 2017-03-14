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

	def play(self):
		self.li = ["New Game", "Load Game"]
		self.input = template.showOptions("Welcome to the game!", "Would you like to start a new game or load your last save?", self.li, 999, 8)
		
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
			self.time = 8
			self.home("You were too tired to do anything else but go home and sleep. Good morning.")
			
	def increaseDay(self):
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
		self.file.write("\n%d" % self.moneyInbank)
		
		self.file.write("\n%d" % self.fishMultiplier)
		
		self.file.write("\n%d" % self.totalFishCaught)
		self.file.write("\n%d" % self.totalMoneyMade)
		self.file.write("\n%d" % self.hoursSpentFishing)	
		self.file.write("\n%d" % self.moneyMadeFromInterest)
			
	def loadGame(self):
		with open("savefile.txt") as f:
			self.content = f.readlines()
				
		self.day = int(self.content[0])
		
		self.fishCount = int(self.content[1])
		self.money = int(self.content[2])
		self.moneyInbank = int(self.content[3])
		
		self.fishMultiplier = int(self.content[4])
		
		self.totalFishCaught = int(self.content[5])
		self.totalMoneyMade = int(self.content[6])
		self.hoursSpentFishing = int(self.content[7])
		self.moneyMadeFromInterest = int(self.content[8])

# LOCATIONS -------------------------------------------------------------------------------------------------------------------------	
	def home(self, p):		
		self.prompt = p
		self.li = ["Sleep", "Check Inventory", "See Stats", "Go to Docks"]
		self.input = template.showOptions("You sit at home, polishing one of your prized fishing poles.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.sleep()
			
		elif self.input == "2":
			self.checkInventory()
			self.home("What would you like to do?")
		
		elif self.input == "3":
			self.seeStats()
			self.home("What would you like to do?")
		
		elif self.input == "4":
			self.increaseTime()
			self.docks("What would you like to do?")
				
	def docks(self, p):
		self.prompt = p
		self.li = ["Fish", "Check Inventory", "Go Home", "Go to Shop", "Go to Tavern", "Go to Bank"]
		self.input = template.showOptions("You breathe in the fresh air. Salty.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.fish()

		elif self.input == "2":
			self.checkInventory()
			self.docks("What would you like to do?")
			
		elif self.input == "3":
			self.increaseTime()
			self.home("What would you like to do?")
			
		elif self.input == "4":
			self.increaseTime()
			self.shop("What would you like to do?")
		
		elif self.input == "5":
			self.increaseTime()
			self.tavern("What would you like to do?")
			
		elif self.input == "6":
			self.increaseTime()
			self.bank("What would you like to do? Money in Bank: $%d" % self.moneyInBank)

	def shop(self, p):
		self.prompt = p
		self.li = ["Buy/Sell", "Check Inventory", "Go to Docks"]
		self.input = template.showOptions("The shopkeeper winks at you as you behold his collection of fishing poles.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.buysell("What would you like to do?")
		
		elif self.input == "2":
			self.checkInventory()
			self.shop("What would you like to do?")
			
		elif self.input == "3":
			self.increaseTime()
			self.docks("What would you like to do?")
	
	def tavern(self, p):
		self.prompt = p
		self.li = ["Gamble", "Go to Docks"]
		self.input = template.showOptions("You sit at the bar, watching the barkeep clean a mug with a dirty rag.", self.prompt, self.li, self.day, self.time)
		
		if self.input == "1":
			self.gamble()
			self.tavern("Gambling! What a rush!")
		
		elif self.input == "2":
			self.increaseTime()
			self.docks("What would you like to do?")
			
	def bank(self, p): # IN DEVELOPMENT
		self.prompt = p
		self.li = ["Make a Deposit", "Make a Withdrawal", "Check inventory", "Go to docks"]
		self.input = template.showOptions("You're at the front of the line and the teller asks you what you want to do.", self.prompt, self.li, self.day, self.time)
		
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
			self.checkInventory()
			self.bank("The people in line behind you are getting impatient, hurry up and make a decision!")
			
		elif self.input == "4":
			self.increaseTime()
			self.docks("What would you like to do?")
			
# ACTIONS -------------------------------------------------------------------------------------------------------------------------	
	def sleep(self):
		if self.time > 20:			
			self.time = 8
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
		self.input = template.showOptions("The shopkeeper waits for you to make a decision.", self.prompt, self.li, self.day, self.time)
		
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
	
	def checkInventory(self):
		template.lotsOfSpace()
		template.divider()
		print "Fish: %d " % self.fishCount,
		print "| Money: $%d" % self.money
		template.divider()
		raw_input(" [ CONTINUE ]")
		
	def seeStats(self):
		template.lotsOfSpace()
		template.divider()
		print "Total Fish Caught: %d " % self.totalFishCaught,
		print "| Total Money Made: $%d " % self.totalMoneyMade,
		print "| Hours Spent Fishing: %d" % self.hoursSpentFishing
		template.divider()
		print "Money Made From Interest: $%d" % self.moneyMadeFromInterest
		template.divider()
		raw_input(" [ CONTINUE ]")	
		
	def gamble(self): # decide whether to do an in depth game or just having it be like "you gamble for a few hours and win/lose this much $"
		template.lotsOfSpace()
		template.divider()
		print "Gambling coming soon"
		template.divider()
		raw_input(" [ CONTINUE ]")
		
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
