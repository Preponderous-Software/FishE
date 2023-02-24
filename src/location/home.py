from location.enum.locationType import LocationType
from player.player import Player
from world.timeService import TimeService
from stats.stats import Stats
from template.textAdventureTemplate import TextAdventureTemplate

# @author Daniel McCoy Stephenson
class Home:
    def __init__(self, template: TextAdventureTemplate, currentPrompt: str, player: Player, stats: Stats, timeService: TimeService):
        self.template = template
        self.currentPrompt = currentPrompt
        self.player = player
        self.stats = stats
        self.timeService = timeService
    
    def run(self, prompt):
        li = ["Sleep", "See Stats", "Go to Docks", "Quit"]
        self.input = self.template.showOptions("You sit at home, polishing one of your prized fishing poles.", prompt, li, self.timeService.day, self.timeService.time, self.player.money, self.player.fishCount)
        
        if self.input == "1":
            self.sleep()
            return LocationType.HOME
        elif self.input == "2":
            self.displayStats()
            self.currentPrompt = "What would you like to do?"
            return LocationType.HOME
        elif self.input == "3":
            self.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
        elif self.input == "4":
            return LocationType.NONE
            
    def sleep(self):
        self.timeService.increaseDay()
        self.currentPrompt = "You sleep until the next morning."

    def displayStats(self):
        self.template.lotsOfSpace()
        print("Total Fish Caught: %d" % self.stats.totalFishCaught)
        print("Total Money Made: %d" % self.stats.totalMoneyMade)
        print("Hours Spent Fishing: %d" % self.stats.hoursSpentFishing)
        print("Money Made From Interest: %d" % self.stats.moneyMadeFromInterest)
        print("Times Gotten Drunk: %d" % self.stats.timesGottenDrunk)
        print("Money Lost Gambling: %d" % self.stats.moneyLostFromGambling)
        self.template.lotsOfSpace()
        input(" [ CONTINUE ]")