import time
import random

class Game(object):

	def __init__(self):
		self.currentLocation = "home"
		
	def getInput(self):
		print "\n"
		print "-" * 40
		
		if self.currentLocation == "home":
			print "\nYou sit at home, twiddling your thumbs."
			
		if self.currentLocation == "docks":
			print "\nYou sit on the edge of the docks, fishing pole in hand."
		
		if self.currentLocation == "store":
			print "\nThe shopkeeper winks at you as you behold his collection of fishing poles."
		
		print "\nOPTIONS:"
		
		if self.currentLocation == "home":
			print "\n\t[1] Sleep"
			print "\n\t\t[2] Head to Docks"
			print "\n\t\t\t[3] Go to store"
			print "\n\t\t\t\t[4] View Collection"
			
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
			print "\n\t[1] Browse!"
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
		print "-" * 40	
		
	def dealWithInput(self):
		
		self.playerInput = self.getInput()
		
		if self.playerInput == "sleep":
			pass
			
		elif self.playerInput == "docks":
			self.currentLocation = "docks"
			self.dealWithInput()
			
		elif self.playerInput == "store":
			self.currentLocation = "store"
			self.dealWithInput()
			
		elif self.playerInput == "home":
			self.currentLocation = "home"
			self.dealWithInput()
			
		elif self.playerInput == "collection":
			pass
			
		elif self.playerInput == "fish":
			print "\n"
			print "-" * 40
			print "\nYou cast your line, hoping for a bite."

			seconds = random.randint(1,10)

			for i in range(0,seconds):
				time.sleep(1)
				print "..."
		
			time.sleep(1)	
			print "You caught one! It only took %d hours!\n" % seconds
			
			print "-" * 40
			
			raw_input("\n\n[CONTINUE]")
			
			self.dealWithInput()
			
		elif self.playerInput == "browse":
			pass
			
if __name__ == "__main__":

	myGame = Game()
	myGame.dealWithInput()
