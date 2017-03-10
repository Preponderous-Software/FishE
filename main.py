import time
import random
from engine import Engine

class Game(object):

	def __init__(self, engine):
		self.engine = engine
		self.engine.currentLocation = "home"
		
	def dealWithInput(self):
		
		self.playerInput = self.engine.getInput()
		
		if self.playerInput == "sleep":
			pass
			
		elif self.playerInput == "docks":
			self.engine.currentLocation = "docks"
			self.dealWithInput()
			
		elif self.playerInput == "store":
			self.engine.currentLocation = "store"
			self.dealWithInput()
			
		elif self.playerInput == "home":
			self.engine.currentLocation = "home"
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
	myEngine = Engine()
	myGame = Game(myEngine)
	myGame.dealWithInput()
