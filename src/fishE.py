from location import bank, docks, home, shop, tavern
from stats.stats import Stats
from template.textAdventure import Text_Adventure_Template
import time
import random
import sys
import math


class FishE:
    def __init__(self):
        self.template = Text_Adventure_Template()

        self.options = []

        self.day = 1
        self.time = 8

        self.fishCount = 0
        self.money = 0
        self.moneyInBank = 0

        self.fishMultiplier = 1

        self.stats = Stats()

        self.currentBet = 0
        self.priceForBait = 50

        self.locations = {
            "home": home.Home(self),
            "docks": docks.Docks(self),
            "shop": shop.Shop(self),
            "tavern": tavern.Tavern(self),
            "bank": bank.Bank(self),
        }

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

        if input == "1":
            self.locations["home"].run("What would you like to do?")
        elif input == "2":
            self.loadGame()
            self.locations["home"].run("What would you like to do?")

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

        self.moneyInBank += int(math.ceil(self.moneyInBank * 0.10))
        self.stats.addMoneyMadeFromInterest(int(math.ceil(self.moneyInBank * 0.10)))
        self.stats.addMoneyMade(int(math.ceil(self.moneyInBank * 0.10)))

    def saveGame(self):
        self.file = open("savefile.txt", "w")

        self.file.write("%d" % self.day)

        self.file.write("\n%d" % self.fishCount)
        self.file.write("\n%d" % self.money)
        self.file.write("\n%d" % self.moneyInBank)

        self.file.write("\n%d" % self.fishMultiplier)

        self.file.write("\n%d" % self.stats.totalFishCaught)
        self.file.write("\n%d" % self.stats.totalMoneyMade)
        self.file.write("\n%d" % self.stats.hoursSpentFishing)
        self.file.write("\n%d" % self.stats.moneyMadeFromInterest)
        self.file.write("\n%d" % self.stats.timesGottenDrunk)
        self.file.write("\n%d" % self.stats.moneyLostFromGambling)

    def loadGame(self):
        with open("savefile.txt") as f:
            self.content = f.readlines()

        self.day = int(self.content[0])

        self.fishCount = int(self.content[1])
        self.money = int(self.content[2])
        self.moneyInBank = int(self.content[3])

        self.fishMultiplier = int(self.content[4])

        self.stats.totalFishCaught = int(self.content[5])
        self.stats.totalMoneyMade = int(self.content[6])
        self.stats.hoursSpentFishing = int(self.content[7])
        self.stats.moneyMadeFromInterest = int(self.content[8])
        self.stats.timesGottenDrunk = int(self.content[9])
        self.stats.moneyLostFromGambling = int(self.content[10])


FishE = FishE()
FishE.play()
