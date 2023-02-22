import random
import sys
import time

from location.enum.locationType import LocationType


class Tavern:
    def __init__(self, fishE):
        self.fishE = fishE
        self.player = fishE.player
        self.stats = fishE.stats
        
        self.currentBet = 0
    
    def run(self, prompt):        
        li = ["Get drunk ( $10 )", "Gamble", "Go to Docks"]
        input = self.fishE.template.showOptions(
            "You sit at the bar, watching the barkeep clean a mug with a dirty rag.",
            prompt,
            li,
            self.fishE.day,
            self.fishE.time,
            self.player.money,
            self.player.fishCount,
        )

        if input == "1":
            if self.player.money >= 10:
                self.getDrunk()
            else:
                self.fishE.currentPrompt = "You don't have enough money."
                return LocationType.TAVERN

        elif input == "2":
            self.gamble(
                "What will the dice land on? Current Bet: $%d" % self.currentBet
            )
            return LocationType.TAVERN

        elif input == "3":
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
    def getDrunk(self):        
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()

        self.player.money -= 10

        for i in range(3):
            print("... ")
            sys.stdout.flush()
            time.sleep(1)

        self.stats.timesGottenDrunk += 1

        self.fishE.increaseDay()
        self.fishE.currentPrompt = "You have a headache."
        return LocationType.HOME
        
    def gamble(self, prompt):        
        li = ["1", "2", "3", "4", "5", "6", "Change Bet", "Back"]
        self.input = int(
            self.fishE.template.showOptions(
                "Once you place your bet, the burly man in front of you will throw the dice.",
                prompt,
                li,
                self.fishE.day,
                self.fishE.time,
                self.player.money,
                self.player.fishCount,
            )
        )

        if 1 <= self.input <= 6 and self.currentBet > 0:
            self.diceThrow = random.randint(1, 6)

            if self.input == self.diceThrow:
                self.player.money += self.currentBet
                self.stats.moneyMadeFromGambling += self.currentBet
                self.currentBet = 0
                self.gamble(
                    "You guessed correctly! Care to try again? Current Bet: $%d"
                    % self.currentBet
                )
            else:
                self.player.money -= self.currentBet
                self.stats.moneyLostFromGambling += self.currentBet
                self.currentBet = 0
                self.gamble(
                    "The dice rolled a %d! You lost your money! Care to try again? Current Bet: $%d"
                    % (self.diceThrow, self.currentBet)
                )
        elif self.input == 7:
            self.changeBet(
                "How much money would you like to bet? Money: $%d" % self.player.money
            )
        elif self.input == 8:
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.TAVERN
        else:
            self.gamble(
                "You didn't bet any money! What will the dice land on? Current Bet: $%d"
                % self.currentBet
            )
            return LocationType.TAVERN

    def changeBet(self, prompt):        
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()
        print(prompt)
        self.fishE.template.divider()

        try:
            self.amount = int(input("> "))
        except ValueError:
            self.deposit("Try again. Money: $%d" % self.player.money)

        if self.amount <= self.player.money:
            self.currentBet = self.amount

            self.gamble(
                "What will the dice land on? Current Bet: $%d" % self.currentBet
            )
        else:
            self.fishE.currentPrompt = "You don't have that much money on you! Money: $%d" % self.player.money
            return LocationType.TAVERN