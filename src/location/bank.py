from location.enum.locationType import LocationType


class Bank:
    def __init__(self, fishE):
        self.fishE = fishE
        self.player = fishE.player
        self.stats = fishE.stats
    
    def run(self, prompt):
        li = ["Make a Deposit", "Make a Withdrawal", "Go to docks"]
        self.fishE.input = self.fishE.template.showOptions(
            "You're at the front of the line and the teller asks you what you want to do.",
            prompt,
            li,
            self.fishE.day,
            self.fishE.time,
            self.player.money,
            self.player.fishCount,
        )

        if self.fishE.input == "1":
            if self.player.money > 0:
                self.deposit(
                    "How much would you like to deposit? Money: $%d" % self.player.money
                )
            else:
                self.fishE.currentPrompt = "You don't have any money on you!"
            return LocationType.BANK

        elif self.fishE.input == "2":
            if self.player.moneyInBank > 0:
                self.withdraw(
                    "How much would you like to withdraw? Money In Bank: $%d" % self.player.moneyInBank
                )
            else:
                self.fishE.currentPrompt = "You don't have any money in the bank!"
            return LocationType.BANK

        elif self.fishE.input == "3":
            self.fishE.currentPrompt = "What would you like to do?"
            return LocationType.DOCKS
            
    def deposit(self, prompt):
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()
        print(prompt)
        self.fishE.template.divider()

        try:
            amount = int(input("> "))
        except ValueError:
            self.deposit("Try again. Money: $%d" % self.player.money)

        if amount <= self.player.money:
            self.player.moneyInBank += amount
            self.player.money -= amount
            
            self.fishE.currentPrompt = "$%d deposited successfully." % amount
        else:
            self.fishE.currentPrompt = "You don't have that much money on you!"
            
        return LocationType.BANK

    def withdraw(self, prompt):
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()
        print(prompt)
        self.fishE.template.divider()

        try:
            amount = int(input("> "))
        except ValueError:
            self.withdraw("Try again. Money In Bank: $%d" % self.player.moneyInBank)

        if amount <= self.player.moneyInBank:
            self.player.money += amount
            self.player.moneyInBank -= amount

            self.fishE.currentPrompt = "$%d withdrawn successfully." % amount
        else:
            self.fishE.currentPrompt = "You don't have that much money in the bank!"