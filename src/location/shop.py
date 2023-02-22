import random
from location.enum.locationType import LocationType


class Shop:
    def __init__(self, fishE):
        self.fishE = fishE
        self.player = fishE.player
        self.stats = fishE.stats
    
    def run(self, prompt):
        prompt = prompt
        li = ["Buy/Sell", "Go to Docks"]
        self.fishE.input = self.fishE.template.showOptions(
            "The shopkeeper winks at you as you behold his collection of fishing poles.",
            prompt,
            li,
            self.fishE.day,
            self.fishE.time,
            self.player.money,
            self.player.fishCount,
        )

        if self.fishE.input == "1":
            self.buysell("What would you like to do?")
            return LocationType.SHOP

        elif self.fishE.input == "2":
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
    def buysell(self, prompt):        
        li = ["Sell Fish", "Buy Better Bait ( $%d )" % self.fishE.priceForBait, "Back"]
        self.fishE.input = self.fishE.template.showOptions(
            "The shopkeeper waits for you to make a decision.",
            prompt,
            li,
            self.fishE.day,
            self.fishE.time,
            self.player.money,
            self.player.fishCount,
        )

        if self.fishE.input == "1":
            moneyToAdd = self.player.fishCount * random.randint(3, 5)
            self.player.money += moneyToAdd
            self.stats.totalMoneyMade += moneyToAdd
            self.player.fishCount = 0

            self.buysell("You sold all of your fish!")

        elif self.fishE.input == "2":
            if self.player.money < self.fishE.priceForBait:
                self.buysell("You don't have enough money!")
            else:
                self.player.fishMultiplier += 1
                self.player.money -= self.fishE.priceForBait

                self.fishE.priceForBait = self.fishE.priceForBait * 1.25

                self.buysell("You bought some better bait!")

        elif self.fishE.input == "3":
            self.fishE.currentPrompt = "What would you like to do?"