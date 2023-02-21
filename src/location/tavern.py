import random
import sys
import time

from location.enum.locationType import LocationType


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
                self.getDrunk()
            else:
                self.run("You don't have enough money!")

        elif self.fishE.input == "2":
            self.gamble(
                "What will the dice land on? Current Bet: $%d" % self.fishE.currentBet
            )
            return LocationType.TAVERN

        elif self.fishE.input == "3":
            self.fishE.increaseTime()
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
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
        self.fishE.currentPrompt = "You have a headache."
        return LocationType.HOME
        
    def gamble(self, p):
        li = ["1", "2", "3", "4", "5", "6", "Change Bet", "Back"]
        self.input = int(
            self.fishE.template.showOptions(
                "Once you place your bet, the burly man in front of you will throw the dice.",
                p,
                li,
                self.fishE.day,
                self.fishE.time,
                self.fishE.money,
                self.fishE.fishCount,
            )
        )

        if 1 <= self.input <= 6 and self.fishE.currentBet > 0:
            self.diceThrow = random.randint(1, 6)

            if self.input == self.diceThrow:
                self.fishE.money += self.currentBet
                self.fishE.stats.addMoneyMade(self.currentBet)
                self.currentBet = 0
                self.gamble(
                    "You guessed correctly! Care to try again? Current Bet: $%d"
                    % self.currentBet
                )
            else:
                self.fishE.money -= self.currentBet
                self.fishE.stats.addMoneyLostFromGambling(self.currentBet)
                self.currentBet = 0
                self.gamble(
                    "The dice rolled a %d! You lost your money! Care to try again? Current Bet: $%d"
                    % (self.diceThrow, self.currentBet)
                )
        elif self.input == 7:
            self.changeBet(
                "How much money would you like to bet? Money: $%d" % self.money
            )
        elif self.input == 8:
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.TAVERN
        else:
            self.gamble(
                "You didn't bet any money! What will the dice land on? Current Bet: $%d"
                % self.fishE.currentBet
            )
            return LocationType.TAVERN

    def changeBet(self, p):
        self.prompt = p
        self.template.lotsOfSpace()
        self.template.divider()
        print(self.prompt)
        self.template.divider()

        try:
            self.amount = int(input("> "))
        except ValueError:
            self.deposit("Try again. Money: $%d" % self.money)

        if self.amount <= self.money:
            self.currentBet = self.amount

            self.gamble(
                "What will the dice land on? Current Bet: $%d" % self.currentBet
            )
        else:
            self.deposit(
                "You don't have that much money on you! Money: $%d" % self.money
            )