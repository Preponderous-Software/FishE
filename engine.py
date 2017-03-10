class Engine(object):
	
	def __init__(self):
		self.currentLocation = "?" # will be changed by map class
		self.returnLocation = "?" # will be used by map class to change current location
		
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
			
if __name__ == "__main__":
	myEngine = Engine()
	myDecision = myEngine.getInput()
