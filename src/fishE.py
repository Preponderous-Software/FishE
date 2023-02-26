import json
import os
from location import bank, docks, home, shop, tavern
from location.enum.locationType import LocationType
from player.player import Player
from prompt.prompt import Prompt
from player.playerJsonReaderWriter import PlayerJsonReaderWriter
from world.timeServiceJsonReaderWriter import TimeServiceJsonReaderWriter
from world.timeService import TimeService
from stats.stats import Stats
from ui.userInterface import UserInterface


# @author Daniel McCoy Stephenson
class FishE:
    def __init__(self):
        self.running = True

        self.playerJsonReaderWriter = PlayerJsonReaderWriter()
        self.timeServiceJsonReaderWriter = TimeServiceJsonReaderWriter()

        # if save file exists, load it
        if os.path.exists("data/player.json"):
            playerSaveFile = open("data/player.json", "r")
            self.player = self.playerJsonReaderWriter.readPlayerFromFile(
                playerSaveFile
            )
            playerSaveFile.close()
        else:
            self.player = Player()

        self.stats = Stats()

        # if save file exists, load it
        if os.path.exists("data/timeService.json"):
            timeServiceSaveFile = open("data/timeService.json", "r")
            self.timeService = self.timeServiceJsonReaderWriter.createTimeServiceFromJson(
                json.load(timeServiceSaveFile), self.player, self.stats
            )
            timeServiceSaveFile.close()
        else:
            self.timeService = TimeService(self.player, self.stats)

        self.prompt = Prompt("What would you like to do?")

        self.userInterface = UserInterface(self.prompt, self.timeService, self.player)

        self.locations = {
            LocationType.BANK: bank.Bank(
                self.userInterface,
                self.prompt,
                self.player,
                self.stats,
                self.timeService,
            ),
            LocationType.DOCKS: docks.Docks(
                self.userInterface,
                self.prompt,
                self.player,
                self.stats,
                self.timeService,
            ),
            LocationType.HOME: home.Home(
                self.userInterface,
                self.prompt,
                self.player,
                self.stats,
                self.timeService,
            ),
            LocationType.SHOP: shop.Shop(
                self.userInterface,
                self.prompt,
                self.player,
                self.stats,
                self.timeService,
            ),
            LocationType.TAVERN: tavern.Tavern(
                self.userInterface,
                self.prompt,
                self.player,
                self.stats,
                self.timeService,
            ),
        }

        self.currentLocation = LocationType.HOME

    def play(self):
        while self.running:
            # change location
            nextLocation = self.locations[self.currentLocation].run()

            if nextLocation == LocationType.NONE:
                self.running = False

            self.currentLocation = nextLocation

            # increase time & save
            self.timeService.increaseTime()
            self.save()

    def save(self):
        # create data directory
        if not os.path.exists("data"):
            os.makedirs("data")

        playerSaveFile = open("data/player.json", "w")
        self.playerJsonReaderWriter.writePlayerToFile(self.player, playerSaveFile)

        timeServiceSaveFile = open("data/timeService.json", "w")
        self.timeServiceJsonReaderWriter.writeTimeServiceToFile(self.timeService, timeServiceSaveFile)
    
    def load(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        
        if not os.path.exists("data/player.json"):
            return
    
        playerSaveFile = open("data/player.json", "r")
        self.player = self.playerJsonReaderWriter.readPlayerFromFile(playerSaveFile)

        timeServiceSaveFile = open("data/timeService.json", "r")
        self.timeService = self.timeServiceJsonReaderWriter.readTimeServiceFromFile(timeServiceSaveFile, self.player, self.stats)
        

if __name__ == "__main__":
    FishE = FishE()
    FishE.play()
