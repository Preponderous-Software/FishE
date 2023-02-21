import random
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
                self.getDrunk()
            else:
                self.run("You don't have enough money!")

        elif self.fishE.input == "2":
            self.gamble(
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
            self.fishE.locations["tavern"].run("What would you like to do?")
        else:
            self.gamble(
                "You didn't bet any money! What will the dice land on? Current Bet: $%d"
                % self.fishE.currentBet
            )

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