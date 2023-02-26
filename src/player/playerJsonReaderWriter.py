import json
from player.player import Player

class PlayerJsonReaderWriter:
    
    def createJsonFromPlayer(self, player):
        return {
            "fishCount": player.fishCount,
            "fishMultiplier": player.fishMultiplier,
            "money": player.money,
            "moneyInBank": player.moneyInBank
        }

    def createPlayerFromJson(self, playerJson):
        player = Player()
        player.fishCount = playerJson["fishCount"]
        player.fishMultiplier = playerJson["fishMultiplier"]
        player.money = playerJson["money"]
        player.moneyInBank = playerJson["moneyInBank"]
        return player

    def writePlayerToFile(self, player, jsonFile):
        playerJson = self.createJsonFromPlayer(player)
        json.dump(playerJson, jsonFile)
    
    def readPlayerFromFile(self, jsonFile):
        playerJson = json.load(jsonFile)
        return self.createPlayerFromJson(playerJson)