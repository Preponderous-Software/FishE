import random
import sys
import time

from location.enum.locationType import LocationType

from player.player import Player
from world.timeService import TimeService
from stats.stats import Stats
from template.textAdventureTemplate import TextAdventureTemplate

# @author Daniel McCoy Stephenson
class Tavern:
    def __init__(self, template: TextAdventureTemplate, currentPrompt: str, player: Player, stats: Stats, timeService: TimeService):
        self.template = template
        self.currentPrompt = currentPrompt
        self.player = player
        self.stats = stats
        self.timeService = timeService
        
        self.currentBet = 0
    
    def run(self, prompt):        
        li = ["Get drunk ( $10 )", "Gamble", "Go to Docks"]
        input = self.template.showOptions(
            "You sit at the bar, watching the barkeep clean a mug with a dirty rag.",
            prompt,
            li,
            self.timeService.day,
            self.timeService.time,
            self.player.money,
            self.player.fishCount,
        )

        if input == "1":
            if self.player.money >= 10:
                self.getDrunk()
                return LocationType.HOME
            else:
                self.currentPrompt = "You don't have enough money."
                return LocationType.TAVERN

        elif input == "2":
            self.gamble(
                "What will the dice land on? Current Bet: $%d" % self.currentBet
            )
            return LocationType.TAVERN

        elif input == "3":
            self.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
    def getDrunk(self):        
        self.template.lotsOfSpace()
        self.template.divider()

        self.player.money -= 10

        for i in range(3):
            print("... ")
            sys.stdout.flush()
            time.sleep(1)

        self.stats.timesGottenDrunk += 1

        self.timeService.increaseDay()
        self.currentPrompt = "You have a headache."
        
    def gamble(self, prompt):        
        li = ["1", "2", "3", "4", "5", "6", "Change Bet", "Back"]
        input = int(
            self.template.showOptions(
                "Once you place your bet, the burly man in front of you will throw the dice.",
                prompt,
                li,
                self.timeService.day,
                self.timeService.time,
                self.player.money,
                self.player.fishCount,
            )
        )

        if 1 <= input <= 6 and self.currentBet > 0:
            self.diceThrow = random.randint(1, 6)

            if input == self.diceThrow:
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
        elif input == 7:
            self.changeBet(
                "How much money would you like to bet? Money: $%d" % self.player.money
            )
        elif input == 8:
            self.currentPrompt = "What would you like to do?"
        else:
            self.gamble(
                "You didn't bet any money! What will the dice land on? Current Bet: $%d"
                % self.currentBet
            )

    def changeBet(self, prompt):        
        self.template.lotsOfSpace()
        self.template.divider()
        print(prompt)
        self.template.divider()

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
            self.currentPrompt = "You don't have that much money on you! Money: $%d" % self.player.money