from location import bank, docks, home, shop, tavern
from location.enum.locationType import LocationType
from player.player import Player
from world.timeService import TimeService
from stats.stats import Stats
from template.textAdventureTemplate import TextAdventureTemplate
import math

# @author Daniel McCoy Stephenson
class FishE:
    def __init__(self):
        self.running = True
        
        self.template = TextAdventureTemplate()

        self.player = Player()
        self.stats = Stats()

        self.timeService = TimeService(self.player, self.stats)
                
        self.currentPrompt = "What would you like to do?"

        self.locations = {
            LocationType.BANK: bank.Bank(self.template, self.currentPrompt, self.player, self.stats, self.timeService),
            LocationType.DOCKS: docks.Docks(self.template, self.currentPrompt, self.player, self.stats, self.timeService),
            LocationType.HOME: home.Home(self.template, self.currentPrompt, self.player, self.stats, self.timeService),
            LocationType.SHOP: shop.Shop(self.template, self.currentPrompt, self.player, self.stats, self.timeService),
            LocationType.TAVERN: tavern.Tavern(self.template, self.currentPrompt, self.player, self.stats, self.timeService)
        }
        
        self.currentLocation = LocationType.HOME

    def play(self):
        while self.running:               
            # change location
            nextLocation = self.locations[self.currentLocation].run(self.currentPrompt)
            
            if nextLocation == LocationType.NONE:
                self.running = False
            
            self.currentLocation = nextLocation
            
            # increase time & save
            self.timeService.increaseTime()


FishE = FishE()
FishE.play()