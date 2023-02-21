class Stats:
    def __init__(self):
        self.totalFishCaught = 0
        self.totalMoneyMade = 0
        self.hoursSpentFishing = 0
        self.moneyMadeFromInterest = 0
        self.timesGottenDrunk = 0
        self.moneyLostFromGambling = 0

    def addFishCaught(self, amount):
        self.totalFishCaught += amount

    def addMoneyMade(self, amount):
        self.totalMoneyMade += amount

    def addHoursSpentFishing(self, amount):
        self.hoursSpentFishing += amount

    def addMoneyMadeFromInterest(self, amount):
        self.moneyMadeFromInterest += amount

    def addTimesGottenDrunk(self, amount):
        self.timesGottenDrunk += amount

    def addMoneyLostFromGambling(self, amount):
        self.moneyLostFromGambling += amount

    def getTotalFishCaught(self):
        return self.totalFishCaught

    def getTotalMoneyMade(self):
        return self.totalMoneyMade

    def getHoursSpentFishing(self):
        return self.hoursSpentFishing

    def getMoneyMadeFromInterest(self):
        return self.moneyMadeFromInterest

    def getTimesGottenDrunk(self):
        return self.timesGottenDrunk

    def getMoneyLostFromGambling(self):
        return self.moneyLostFromGambling