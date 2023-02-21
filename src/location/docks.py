import random
import sys
import time


class Docks:
    def __init__(self, fishE):
        self.fishE = fishE
        
    def run(self, p):
        self.fishE.prompt = p
        li = ["Fish", "Go Home", "Go to Shop", "Go to Tavern", "Go to Bank"]
        self.fishE.input = self.fishE.template.showOptions(
            "You breathe in the fresh air. Salty.",
            self.fishE.prompt,
            li,
            self.fishE.day,
            self.fishE.time,
            self.fishE.money,
            self.fishE.fishCount,
        )

        if self.fishE.input == "1":
            self.fish()

        elif self.fishE.input == "2":
            self.fishE.increaseTime()
            self.fishE.locations["home"].run("What would you like to do?")

        elif self.fishE.input == "3":
            self.fishE.increaseTime()
            self.fishE.locations["shop"].run("What would you like to do?")

        elif self.fishE.input == "4":
            self.fishE.increaseTime()
            self.fishE.locations["tavern"].run("What would you like to do?")

        elif self.fishE.input == "5":
            self.fishE.increaseTime()
            self.fishE.locations["bank"].run(
                "What would you like to do? Money in Bank: $%d" % self.fishE.moneyInBank
            )
            
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
            time.sleep(1)
            self.fishE.increaseTime()
            self.fishE.stats.addHoursSpentFishing(1)

        self.fishE.fishCount = 1 * self.fishE.fishMultiplier
        self.fishE.stats.addFishCaught(self.fishE.fishCount)

        if self.fishE.fishCount == 1:
            self.fishE.locations["docks"].run("Nice catch! It only took %d hour!" % hours)
        else:
            self.fishE.locations["docks"].run(
                "You caught %d fish! It only took %d hours!" % (self.fishE.fishCount, hours)
            )