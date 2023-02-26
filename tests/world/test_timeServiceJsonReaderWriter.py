from src.player.player import Player
from src.stats.stats import Stats
from src.world import timeServiceJsonReaderWriter
from src.world.timeService import TimeService
import json
from jsonschema import validate


def createTimeServiceJsonReaderWriter():
    return timeServiceJsonReaderWriter.TimeServiceJsonReaderWriter()


def createTimeService():
    player = Player()
    stats = Stats()
    return TimeService(player, stats)


def getTimeServiceSchema():
    # load json from file
    with open("schemas/timeService.json") as json_file:
        return json.load(json_file)


def test_initialization():
    timeServiceJsonReaderWriter = createTimeServiceJsonReaderWriter()
    assert timeServiceJsonReaderWriter != None


def test_createJsonFromTimeService():
    timeServiceJsonReaderWriter = createTimeServiceJsonReaderWriter()
    timeService = createTimeService()
    timeServiceJson = timeServiceJsonReaderWriter.createJsonFromTimeService(timeService)
    assert timeServiceJson != None

    # validate
    timeServiceSchema = getTimeServiceSchema()
    validate(timeServiceJson, timeServiceSchema)


def test_createTimeServiceFromJson():
    timeServiceJsonReaderWriter = createTimeServiceJsonReaderWriter()
    timeServiceJson = {"time": 8, "day": 1}

    # validate
    timeServiceSchema = getTimeServiceSchema()
    validate(timeServiceJson, timeServiceSchema)

    player = Player()
    stats = Stats()
    timeServiceFromJson = timeServiceJsonReaderWriter.createTimeServiceFromJson(
        timeServiceJson, player, stats
    )
    assert timeServiceFromJson != None
