from location.enum.locationType import LocationType


class Home:
    def __init__(self, fishE):
        self.fishE = fishE
        self.player = fishE.player
        self.stats = fishE.stats
    
    def run(self, prompt):
        li = ["Sleep", "See Stats", "Go to Docks"]
        self.input = self.fishE.template.showOptions("You sit at home, polishing one of your prized fishing poles.", prompt, li, self.fishE.day, self.fishE.time, self.player.money, self.player.fishCount)
        
        if self.input == "1":
            self.sleep()
            return LocationType.HOME
        
        elif self.input == "2":
            self.displayStats()
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.HOME
        
        elif self.input == "3":
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
    def sleep(self) -> str:
        if self.fishE.time > 20:
            self.fishE.increaseDay()
            self.fishE.currentPrompt = "What would you like to do?"
        else:
            self.fishE.currentPrompt = "You can't sleep yet. What would you like to do?"

    def displayStats(self):
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()
        print("Total Fish Caught: %d" % self.stats.totalFishCaught)
        print("| Total Money Made: %d" % self.stats.totalMoneyMade)
        print("| Hours Spent Fishing: %d" % self.stats.hoursSpentFishing)
        self.fishE.template.divider()
        print("Money Made From Interest: %d" % self.stats.moneyMadeFromInterest)
        print("| Times Gotten Drunk: %d" % self.stats.timesGottenDrunk)
        print("| Money Lost Gambling: %d" % self.stats.moneyLostFromGambling)
        self.fishE.template.divider()
        input(" [ CONTINUE ]")