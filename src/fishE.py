from location import bank, docks, home, shop, tavern
from location.enum.locationType import LocationType
from player.player import Player
from stats.stats import Stats
from template.textAdventureTemplate import TextAdventureTemplate
import time
import random
import sys
import math


class FishE:
    def __init__(self):
        self.running = True
        
        self.template = TextAdventureTemplate()

        self.options = []

        self.day = 1
        self.time = 8

        self.player = Player()
        self.stats = Stats()

        self.currentBet = 0
        self.priceForBait = 50

        self.locations = {
            LocationType.HOME: home.Home(self),
            LocationType.DOCKS: docks.Docks(self),
            LocationType.SHOP: shop.Shop(self),
            LocationType.TAVERN: tavern.Tavern(self),
            LocationType.BANK: bank.Bank(self)
        }
        
        self.currentLocation = LocationType.HOME
        self.currentPrompt = "What would you like to do?"

    def play(self):
        li = ["New Game", "Load Game"]
        input = self.template.showOptions(
            "Welcome to the game!",
            "Would you like to start a new game or load your last save?",
            li,
            999,
            8,
            999,
            999,
        )

        if input == "2":
            self.loadGame()
        
        while self.running:
            if self.currentLocation == None:
                print("WARNING: currentLocation is None.")
                
            nextLocation = self.locations[self.currentLocation].run(self.currentPrompt)
            self.currentLocation = nextLocation
            self.increaseTime()
            

    def increaseTime(self):
        self.time += 1

        if self.time > 23:
            self.time = 0

        if 0 <= self.time <= 7:  # returns player home if it's late

            self.increaseDay()

            self.locations["home"].run(
                "You were too tired to do anything else but go home and sleep. Good morning."
            )

    def increaseDay(self):
        self.time = 8
        self.day += 1

        self.saveGame()

        moneyToAdd = int(math.ceil(self.player.moneyInBank * 0.10))
        self.player.moneyInBank += moneyToAdd
        self.stats.moneyMadeFromInterest += moneyToAdd
        self.stats.totalMoneyMade += moneyToAdd
        
        self.currentLocation = "home"

    def saveGame(self):
        self.file = open("savefile.txt", "w")

        self.file.write("%d" % self.day)

        self.file.write("\n%d" % self.player.fishCount)
        self.file.write("\n%d" % self.player.money)
        self.file.write("\n%d" % self.player.moneyInBank)
        self.file.write("\n%d" % self.player.fishMultiplier)

        self.file.write("\n%d" % self.stats.totalFishCaught)
        self.file.write("\n%d" % self.stats.totalMoneyMade)
        self.file.write("\n%d" % self.stats.hoursSpentFishing)
        self.file.write("\n%d" % self.stats.moneyMadeFromInterest)
        self.file.write("\n%d" % self.stats.timesGottenDrunk)
        self.file.write("\n%d" % self.stats.moneyLostFromGambling)

    def loadGame(self):
        with open("savefile.txt") as f:
            self.content = f.readlines()
            
        if len(self.content) == 0:
            print("No save file found.")
            return

        self.day = int(self.content[0])

        self.player.fishCount = int(self.content[1])
        self.player.money = int(self.content[2])
        self.player.moneyInBank = int(self.content[3])
        self.player.fishMultiplier = int(self.content[4])

        self.stats.totalFishCaught = int(self.content[5])
        self.stats.totalMoneyMade = int(self.content[6])
        self.stats.hoursSpentFishing = int(self.content[7])
        self.stats.moneyMadeFromInterest = int(self.content[8])
        self.stats.timesGottenDrunk = int(self.content[9])
        self.stats.moneyLostFromGambling = int(self.content[10])


FishE = FishE()
FishE.play()
