class Bank:
    def __init__(self, fishE):
        self.fishE = fishE
    
    def run(self, p):
        li = ["Make a Deposit", "Make a Withdrawal", "Go to docks"]
        self.fishE.input = self.fishE.template.showOptions(
            "You're at the front of the line and the teller asks you what you want to do.",
            p,
            li,
            self.fishE.day,
            self.fishE.time,
            self.fishE.money,
            self.fishE.fishCount,
        )

        if self.fishE.input == "1":
            if self.fishE.money > 0:
                self.deposit(
                    "How much would you like to deposit? Money: $%d" % self.fishE.money
                )
            else:
                self.fishE.locations["bank"].run("You don't have anything to deposit!")

        elif self.fishE.input == "2":
            if self.fishE.moneyInBank > 0:
                self.withdraw(
                    "How much would you like to withdraw? Money In Bank: $%d"
                    % self.fishE.moneyInBank
                )
            else:
                self.fishE.locations["bank"].run("You don't have any money in the bank!")

        elif self.fishE.input == "3":
            self.fishE.increaseTime()
            self.fishE.locations["docks"].run("What would you like to do?")
            
    def deposit(self, p):
        self.fishE.prompt = p
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()
        print(self.fishE.prompt)
        self.fishE.template.divider()

        try:
            self.fishE.amount = int(input("> "))
        except ValueError:
            self.fishE.deposit("Try again. Money: $%d" % self.fishE.money)

        if self.fishE.amount <= self.fishE.money:
            self.fishE.moneyInBank += self.fishE.amount
            self.fishE.money -= self.fishE.amount

            self.fishE.locations["bank"].run("$%d deposited successfully." % self.fishE.amount)
        else:
            self.fishE.locations["bank"].run("You don't have that much money on you!")

    def withdraw(self, p):
        self.fishE.prompt = p
        self.fishE.template.lotsOfSpace()
        self.fishE.template.divider()
        print(self.fishE.prompt)
        self.fishE.template.divider()

        try:
            self.fishE.amount = int(input("> "))
        except ValueError:
            self.fishE.withdraw("Try again. Money In Bank: $%d" % self.fishE.moneyInBank)

        if self.fishE.amount <= self.fishE.moneyInBank:
            self.fishE.money += self.fishE.amount
            self.fishE.moneyInBank -= self.fishE.amount

            self.fishE.locations["bank"].run("$%d withdrawn successfully." % self.fishE.amount)
        else:
            self.fishE.locations["bank"].run("You don't have that much money in the bank!")