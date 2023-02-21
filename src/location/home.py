from location.enum.locationType import LocationType


class Home:
    def __init__(self, fishE):
        self.fishE = fishE
    
    def run(self, p):
        li = ["Sleep", "See Stats", "Go to Docks"]
        self.input = self.fishE.template.showOptions("You sit at home, polishing one of your prized fishing poles.", p, li, self.fishE.day, self.fishE.time, self.fishE.money, self.fishE.fishCount)
        
        if self.input == "1":
            self.sleep()
            return LocationType.HOME
        
        elif self.input == "2":
            self.displayStats()
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.HOME
        
        elif self.input == "3":
            self.fishE.increaseTime()
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
        stats = self.fishE.stats
        print("Total Fish Caught: %d" % stats.getTotalFishCaught())
        print("| Total Money Made: %d" % stats.getTotalMoneyMade())
        print("| Hours Spent Fishing: %d" % stats.getHoursSpentFishing())
        self.fishE.template.divider()
        print("Money Made From Interest: %d" % stats.getMoneyMadeFromInterest())
        print("| Times Gotten Drunk: %d" % stats.getTimesGottenDrunk())
        print("| Money Lost Gambling: %d" % stats.getMoneyLostFromGambling())
        self.fishE.template.divider()
        input(" [ CONTINUE ]")