import math

# @author Daniel McCoy Stephenson
class TimeService:
    def __init__(self, player, stats):
        self.player = player
        self.stats = stats
        
        self.day = 1
        self.time = 8

    def increaseTime(self):
        self.time += 1

        if self.time > 23:
            self.time = 0

        if self.time == 8:
            self.increaseDay()

    def increaseDay(self):
        self.time = 8
        self.day += 1

        moneyToAdd = int(math.ceil(self.player.moneyInBank * 0.10))
        self.player.moneyInBank += moneyToAdd
        self.stats.moneyMadeFromInterest += moneyToAdd
        self.stats.totalMoneyMade += moneyToAdd