from src.player import playerJsonReaderWriter
from src.player.player import Player
import json
from jsonschema import validate


def createPlayerJsonReaderWriter():
    return playerJsonReaderWriter.PlayerJsonReaderWriter()


def createPlayer():
    return Player()


def getPlayerSchema():
    # load json from file
    with open("schemas/player.json") as json_file:
        return json.load(json_file)


def test_initialization():
    playerJsonReaderWriter = createPlayerJsonReaderWriter()
    assert playerJsonReaderWriter != None


def test_createJsonFromPlayer():
    playerJsonReaderWriter = createPlayerJsonReaderWriter()
    player = createPlayer()
    playerJson = playerJsonReaderWriter.createJsonFromPlayer(player)

    # check schema
    playerSchema = getPlayerSchema()
    validate(playerJson, playerSchema)


def test_createPlayerFromJson():
    playerJson = {
        "fishCount": 0,
        "fishMultiplier": 1,
        "money": 0,
        "moneyInBank": 0,
        "priceForBait": 50,
    }

    playerJsonReaderWriter = createPlayerJsonReaderWriter()
    player = playerJsonReaderWriter.createPlayerFromJson(playerJson)

    assert player.fishCount == playerJson["fishCount"]
    assert player.fishMultiplier == playerJson["fishMultiplier"]
    assert player.money == playerJson["money"]
    assert player.moneyInBank == playerJson["moneyInBank"]
