import random
import sys
import time

from location.enum.locationType import LocationType
from player.player import Player
from world.timeService import TimeService
from stats.stats import Stats
from template.textAdventureTemplate import TextAdventureTemplate

# @author Daniel McCoy Stephenson
class Docks:
    def __init__(self, template: TextAdventureTemplate, currentPrompt: str, player: Player, stats: Stats, timeService: TimeService):
        self.template = template
        self.currentPrompt = currentPrompt
        self.player = player
        self.stats = stats
        self.timeService = timeService
        
    def run(self, prompt):
        li = ["Fish", "Go Home", "Go to Shop", "Go to Tavern", "Go to Bank"]
        input = self.template.showOptions(
            "You breathe in the fresh air. Salty.",
            prompt,
            li,
            self.timeService.day,
            self.timeService.time,
            self.player.money,
            self.player.fishCount,
        )

        if input == "1":
            self.fish()
            return LocationType.DOCKS

        elif input == "2":
            self.currentPrompt = "What would you like to do?"
            return LocationType.HOME

        elif input == "3":
            self.currentPrompt = "What would you like to do?"
            return LocationType.SHOP

        elif input == "4":
            self.currentPrompt = "What would you like to do?"
            return LocationType.TAVERN

        elif input == "5":
            self.currentPrompt = "What would you like to do? Money in Bank: $%d" % self.player.moneyInBank
            return LocationType.BANK
            
    def fish(self):
        self.template.lotsOfSpace()
        self.template.divider()

        print("Fishing... "),
        sys.stdout.flush()
        time.sleep(1)

        hours = random.randint(1, 10)

        for i in range(hours):
            print("><> ")
            sys.stdout.flush()
            time.sleep(0.5)
            self.stats.hoursSpentFishing += 1
            self.timeService.increaseTime()

        fishToAdd = random.randint(1, 10) * self.player.fishMultiplier
        self.player.fishCount += fishToAdd
        self.stats.totalFishCaught += fishToAdd

        if fishToAdd == 1:
            self.currentPrompt = "Nice catch!"
        else:
            self.currentPrompt = "You caught %d fish! It only took %d hours!" % (fishToAdd, hours)