import random
import sys
import time

from location.enum.locationType import LocationType
from player.player import Player
from prompt.prompt import Prompt
from world.timeService import TimeService
from stats.stats import Stats
from ui.userInterface import UserInterface


# @author Daniel McCoy Stephenson
class Docks:
    def __init__(
        self,
        userInterface: UserInterface,
        currentPrompt: Prompt,
        player: Player,
        stats: Stats,
        timeService: TimeService,
    ):
        self.userInterface = userInterface
        self.currentPrompt = currentPrompt
        self.player = player
        self.stats = stats
        self.timeService = timeService

    def run(self):
        li = ["Fish", "Go Home", "Go to Shop", "Go to Tavern", "Go to Bank"]
        input = self.userInterface.showOptions(
            "You breathe in the fresh air. Salty.", li
        )

        if input == "1":
            self.fish()
            return LocationType.DOCKS

        elif input == "2":
            self.currentPrompt.text = "What would you like to do?"
            return LocationType.HOME

        elif input == "3":
            self.currentPrompt.text = "What would you like to do?"
            return LocationType.SHOP

        elif input == "4":
            self.currentPrompt.text = "What would you like to do?"
            return LocationType.TAVERN

        elif input == "5":
            self.currentPrompt.text = (
                "What would you like to do? Money in Bank: $%d"
                % self.player.moneyInBank
            )
            return LocationType.BANK

    def fish(self):
        self.userInterface.lotsOfSpace()
        self.userInterface.divider()

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
            self.currentPrompt.text = "Nice catch!"
        else:
            self.currentPrompt.text = "You caught %d fish! It only took %d hours!" % (
                fishToAdd,
                hours,
            )
