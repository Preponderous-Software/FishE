from location import bank, docks, home, shop, tavern
from location.enum.locationType import LocationType
from player.player import Player
from prompt.prompt import Prompt
from world.timeService import TimeService
from stats.stats import Stats
from ui.userInterface import UserInterface


# @author Daniel McCoy Stephenson
class FishE:
    def __init__(self):
        self.running = True

        self.player = Player()
        self.stats = Stats()

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


if __name__ == "__main__":
    FishE = FishE()
    FishE.play()
