from location.enum.locationType import LocationType


class Shop:
    def __init__(self, fishE):
        self.fishE = fishE
    
    def run(self, p):
        prompt = p
        li = ["Buy/Sell", "Go to Docks"]
        self.fishE.input = self.fishE.template.showOptions(
            "The shopkeeper winks at you as you behold his collection of fishing poles.",
            prompt,
            li,
            self.fishE.day,
            self.fishE.time,
            self.fishE.money,
            self.fishE.fishCount,
        )

        if self.fishE.input == "1":
            self.buysell("What would you like to do?")
            return LocationType.SHOP

        elif self.fishE.input == "2":
            self.fishE.increaseTime()
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
    def buysell(self, p):
        li = ["Sell Fish", "Buy Better Bait ( $%d )" % self.fishE.priceForBait, "Back"]
        self.fishE.input = self.fishE.template.showOptions(
            "The shopkeeper waits for you to make a decision.",
            p,
            li,
            self.fishE.day,
            self.fishE.time,
            self.fishE.money,
            self.fishE.fishCount,
        )

        if self.fishE.input == "1":
            self.fishE.money += self.fishE.fishCount * 5
            self.fishE.stats.addMoneyMade(self.fishE.fishCount * 5)
            self.fishE.fishCount = 0

            self.buysell("You sold all of your fish!")

        elif self.fishE.input == "2":
            if self.fishE.money < self.fishE.priceForBait:
                self.buysell("You don't have enough money!")
            else:
                self.fishE.fishMultiplier += 1
                self.fishE.money -= self.fishE.priceForBait

                self.fishE.priceForBait = self.fishE.priceForBait * 1.25

                self.buysell("You bought some better bait!")

        elif self.fishE.input == "3":
            self.fishE.currentPrompt = "What would you like to do?"