import time
import random

class Game(object):

	def __init__(self):
		self.currentLocation = "home"
		self.times = {0: "12:00 AM",
				    1: "1:00 AM",
				    2: "2:00 AM",
				    3: "3:00 AM",
				    4: "4:00 AM",
				    5: "5:00 AM",
				    6: "6:00 AM",
				    7: "7:00 AM",
				    8: "8:00 AM",
				    9: "9:00 AM",
				    10: "10:00 AM",
				    11: "11:00 AM",
				    12: "12:00 PM",
				    13: "1:00 PM",
				    14: "2:00 PM",
				    15: "3:00 PM",
				    16: "4:00 PM",
				    17: "5:00 PM",
				    18: "6:00 PM",
				    19: "7:00 PM",
				    20: "8:00 PM", 
				    21: "9:00 PM",
				    22: "10:00 PM", 
				    23: "11:00 PM"}

		self.currentTime = 6
		
		self.day = 1
		
		self.money = 0
		
		self.fish = 0
		
		self.newDawn = False
		
		self.divider = "-" * 60
		
	def increaseTime(self):
		
		self.currentTime = self.currentTime + 1
		
		if self.currentTime == 5:
			self.day = self.day + 1
		
		if self.currentTime > 23:
			self.currentTime = 1
		
	def getInput(self):
		print "\n"
		print self.divider
		print "\nDay %d" % self.day
		print "\nTime: " + self.times[self.currentTime]
		print "\nMoney: $%d" % self.money
		print "\nFish: %d" % self.fish
		
		if self.currentLocation == "home":
			print "\nYou sit at home, twiddling your thumbs."
			
		if self.currentLocation == "docks":
			print "\nYou sit on the edge of the docks, fishing pole in hand."
		
		if self.currentLocation == "store":
			print "\nThe shopkeeper winks at you as you behold his collection of fishing poles."
		
		print "\nOPTIONS:"
		
		if self.currentLocation == "home":
			
			if 22 <= self.currentTime <= 24 or 1 <= self.currentTime < 6:
				print "\nYou're too tired to do anything but sleep."
				
				print "\n"
				print self.divider
				
				raw_input("\n\n[CONTINUE]")
				
				self.currentLocation = "home"
				return "sleep" 
			
			print "\n\t[1] Sleep"
			print "\n\t\t[2] Head to Docks"
			print "\n\t\t\t[3] Go to store"
			
			decision = raw_input("> ") 
			
			if decision == '1':
				return "sleep"
			elif decision == '2':
				return "docks"
			elif decision == '3':
				return "store"
			elif decision == '4':
				return "collection"
			else:
				raw_input("That wasn't an option! [ENTER TO CONTINUE]")
				self.getInput()
		
		if self.currentLocation == "docks":
			
			if 22 <= self.currentTime <= 24 or 1 <= self.currentTime < 6:
				print "\nYou're too tired to do anything but go home and sleep."
				
				print "\n"
				print self.divider
				
				raw_input("\n\n[CONTINUE]")
				
				self.currentLocation = "home"
				return "sleep" 
			
			print "\n\t[1] Fish!"
			print "\n\t\t[2] Go to store"
			print "\n\t\t\t[3] Go home"
			
			decision = raw_input("> ")
			
			if decision == '1':
				return "fish"
			elif decision == '2':
				return "store"
			elif decision == '3':
				return "home"
			else:
				raw_input("That wasn't an option! [ENTER TO CONTINUE]")
				self.getInput()
				
		if self.currentLocation == "store":
			
			if 22 <= self.currentTime <= 24 or 1 <= self.currentTime < 6:
				print "\nYou're too tired to do anything but go home and sleep."
				
				print "\n"
				print self.divider
				
				raw_input("\n\n[CONTINUE]")
				
				self.currentLocation = "home"
				return "sleep" 
			
			print "\n\t[1] Browse/Sell!"
			print "\n\t\t[2] Head to Docks"
			print "\n\t\t\t[3] Go home"
			
			decision = raw_input("> ")
			
			if decision == '1':
				return "browse"
			elif decision == '2':
				return "docks"
			elif decision == '3':
				return "home"
			else:
				raw_input("That wasn't an option! [ENTER TO CONTINUE]")
				self.getInput()
				
		print "\n"
		print self.divider
		
	def dealWithInput(self):
		
		self.playerInput = self.getInput()
		
		if self.playerInput == "sleep":
			
			print "\n"
			
			print self.divider					
			
			print "\nYou pass into the world of dreams."
			
			self.currentTime = 8
			
			for i in range(0,3):
				time.sleep(1)
				print "..."
				
			print "\nYou wake up feeling refreshed.\n"
			
			print self.divider
			
			self.day = self.day + 1
			
			raw_input("\n\n[CONTINUE]")
			
			self.dealWithInput()
			
		elif self.playerInput == "docks":
			self.currentLocation = "docks"
			self.increaseTime()
			self.dealWithInput()
			
		elif self.playerInput == "store":
			self.currentLocation = "store"
			self.increaseTime()
			self.dealWithInput()
			
		elif self.playerInput == "home":
			self.currentLocation = "home"
			self.increaseTime()
			self.dealWithInput()
			
		elif self.playerInput == "browse":
			print "\n"
			print self.divider
			print "\nUnfortunately, they're out of fishing poles!"
			print "\nYou sell %d fish for $%d" % (self.fish, self.fish * 2)
			
			self.money = self.money + (self.fish * 2)
			self.fish = 0
			
			print "\n"
			print self.divider
			
			raw_input("\n\n[CONTINUE]")
			
			self.increaseTime()
			self.dealWithInput()
			
		elif self.playerInput == "fish":
			print "\n"
			print self.divider
			print "\nYou cast your line, hoping for a bite."

			seconds = random.randint(1,10)

			for i in range(0,seconds):
				time.sleep(1)
				self.increaseTime()
				print "..."
				
				if self.currentTime == 5: # if player manages to stay up all night via fishing
					self.newDawn = True;
		
			time.sleep(1)
			print "You caught one! It only took %d hours!\n" % seconds
			
			if self.newDawn == True:
				print "\nThe sight of the sunrise gives you new energy. You won't be needing sleep tonight.\n"
				self.newDawn = False
			
			self.fish = self.fish + 1
			
			print self.divider
			
			raw_input("\n\n[CONTINUE]")
			
			self.dealWithInput()
			
if __name__ == "__main__":

	myGame = Game()
	myGame.dealWithInput()
