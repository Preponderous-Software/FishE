import random
import sys
import time

from location.enum.locationType import LocationType


class Docks:
    def __init__(self, fishE):
        self.fishE = fishE
        self.player = fishE.player
        self.stats = fishE.stats
        
    def run(self, prompt):
        li = ["Fish", "Go Home", "Go to Shop", "Go to Tavern", "Go to Bank"]
        self.fishE.input = self.fishE.template.showOptions(
            "You breathe in the fresh air. Salty.",
            prompt,
            li,
            self.fishE.day,
            self.fishE.time,
            self.player.money,
            self.player.fishCount,
        )

        if self.fishE.input == "1":
            self.fish()
            return LocationType.DOCKS

        elif self.fishE.input == "2":
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.HOME

        elif self.fishE.input == "3":
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.SHOP

        elif self.fishE.input == "4":
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.TAVERN

        elif self.fishE.input == "5":
            self.fishE.currentPrompt = "What would you like to do? Money in Bank: $%d" % self.player.moneyInBank
            return LocationType.BANK
            
    def fish(self):
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()

        print("Fishing... "),
        sys.stdout.flush()
        time.sleep(1)

        hours = random.randint(1, 10)

        for i in range(hours):
            print("><> ")
            sys.stdout.flush()
            time.sleep(0.5)
            self.stats.hoursSpentFishing += 1
            self.fishE.increaseTime()

        fishToAdd = random.randint(1, 10) * self.player.fishMultiplier
        self.player.fishCount += fishToAdd
        self.stats.totalFishCaught += fishToAdd

        if fishToAdd == 1:
            self.fishE.currentPrompt = "Nice catch!"
        else:
            self.fishE.currentPrompt = "You caught %d fish! It only took %d hours!" % (fishToAdd, hours)