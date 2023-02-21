import sys
import time


class Tavern:
    def __init__(self, fishE):
        self.fishE = fishE
    
    def run(self, p):
        li = ["Get drunk ( $10 )", "Gamble", "Go to Docks"]
        self.fishE.input = self.fishE.template.showOptions(
            "You sit at the bar, watching the barkeep clean a mug with a dirty rag.",
            p,
            li,
            self.fishE.day,
            self.fishE.time,
            self.fishE.money,
            self.fishE.fishCount,
        )

        if self.fishE.input == "1":
            if self.fishE.money >= 10:
                self.fishE.getDrunk()
            else:
                self.run("You don't have enough money!")

        elif self.fishE.input == "2":
            self.fishE.gamble(
                "What will the dice land on? Current Bet: $%d" % self.fishE.currentBet
            )

        elif self.fishE.input == "3":
            self.fishE.increaseTime()
            self.fishE.locations["docks"].run("What would you like to do?")
            
    def getDrunk(self):
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()

        self.fishE.money -= 10

        for i in range(3):
            print("... ")
            sys.stdout.flush()
            time.sleep(1)

        self.fishE.stats.addTimesGottenDrunk(1)

        self.fishE.increaseDay()
        self.fishE.locations["home"].run("Your head is pounding after last night.")