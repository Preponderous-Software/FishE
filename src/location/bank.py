from pstats import Stats
from location.enum.locationType import LocationType
from player.player import Player
from world.timeService import TimeService
from template.textAdventureTemplate import TextAdventureTemplate

# @author Daniel McCoy Stephenson
class Bank:
    def __init__(self, template: TextAdventureTemplate, currentPrompt: str, player: Player, stats: Stats, timeService: TimeService):
        self.template = template
        self.currentPrompt = currentPrompt
        self.player = player
        self.stats = stats
        self.timeService = timeService

    def run(self, prompt):
        li = ["Make a Deposit", "Make a Withdrawal", "Go to docks"]
        input = self.template.showOptions(
            "You're at the front of the line and the teller asks you what you want to do.",
            prompt,
            li,
            self.timeService.time,
            self.timeService.day,
            self.player.money,
            self.player.fishCount,
        )

        if input == "1":
            if self.player.money > 0:
                self.deposit(
                    "How much would you like to deposit? Money: $%d" % self.player.money
                )
            else:
                self.currentPrompt = "You don't have any money on you!"
            return LocationType.BANK

        elif input == "2":
            if self.player.moneyInBank > 0:
                self.withdraw(
                    "How much would you like to withdraw? Money In Bank: $%d" % self.player.moneyInBank
                )
            else:
                self.currentPrompt = "You don't have any money in the bank!"
            return LocationType.BANK

        elif input == "3":
            self.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
    def deposit(self, prompt):
        self.template.lotsOfSpace()
        self.template.divider()
        print(prompt)
        self.template.divider()

        try:
            amount = int(input("> "))
        except ValueError:
            self.deposit("Try again. Money: $%d" % self.player.money)

        if amount <= self.player.money:
            self.player.moneyInBank += amount
            self.player.money -= amount
            
            self.currentPrompt = "$%d deposited successfully." % amount
        else:
            self.currentPrompt = "You don't have that much money on you!"

    def withdraw(self, prompt):
        self.template.lotsOfSpace()
        self.template.divider()
        print(prompt)
        self.template.divider()

        try:
            amount = int(input("> "))
        except ValueError:
            self.withdraw("Try again. Money In Bank: $%d" % self.player.moneyInBank)

        if amount <= self.player.moneyInBank:
            self.player.money += amount
            self.player.moneyInBank -= amount

            self.currentPrompt = "$%d withdrawn successfully." % amount
        else:
            self.currentPrompt = "You don't have that much money in the bank!"