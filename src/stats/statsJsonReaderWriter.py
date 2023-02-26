import json
from stats.stats import Stats


class StatsJsonReaderWriter:
    def createJsonFromStats(self, stats: Stats):
        return {
            "totalFishCaught": stats.totalFishCaught,
            "totalMoneyMade": stats.totalMoneyMade,
            "hoursSpentFishing": stats.hoursSpentFishing,
            "moneyMadeFromInterest": stats.moneyMadeFromInterest,
            "timesGottenDrunk": stats.timesGottenDrunk,
            "moneyLostFromGambling": stats.moneyLostFromGambling,
        }

    def createStatsFromJson(self, statsJson):
        stats = Stats()
        stats.totalFishCaught = statsJson["totalFishCaught"]
        stats.totalMoneyMade = statsJson["totalMoneyMade"]
        stats.hoursSpentFishing = statsJson["hoursSpentFishing"]
        stats.moneyMadeFromInterest = statsJson["moneyMadeFromInterest"]
        stats.timesGottenDrunk = statsJson["timesGottenDrunk"]
        stats.moneyLostFromGambling = statsJson["moneyLostFromGambling"]
        return stats

    def readStatsFromFile(self, statsJsonFile):
        statsJson = json.load(statsJsonFile)
        return self.createStatsFromJson(statsJson)

    def writeStatsToFile(self, stats, statsJsonFile):
        statsJson = self.createJsonFromStats(stats)
        json.dump(statsJson, statsJsonFile)
