from src.player.player import Player
from src.stats.stats import Stats
from src.world.timeService import TimeService

def createTimeService():
    player = Player()
    stats = Stats()
    return TimeService(player, stats)

def test_initialization():
    # call
    timeService = createTimeService()
    
    # check
    expected_day = 1
    expected_time = 8
    assert timeService.day == expected_day
    assert timeService.time == expected_time

def test_increaseTime():
    # prepare
    timeService = createTimeService()

    # call
    timeService.increaseTime()
    
    # check
    expected_day = 1
    expected_time = 9
    assert timeService.day == expected_day
    assert timeService.time == expected_time

def test_increaseTimeToNextDay():
    # prepare
    timeService = createTimeService()
    timeService.time = 7

    # call
    timeService.increaseTime()
    
    # check
    expected_day = 2
    expected_time = 8
    assert timeService.day == expected_day
    assert timeService.time == expected_time

def test_increaseDay():
    # prepare
    timeService = createTimeService()
    timeService.player.moneyInBank = 100
    timeService.stats.moneyMadeFromInterest = 0
    timeService.stats.totalMoneyMade = 100

    # call
    timeService.increaseDay()
    
    # check
    expected_day = 2
    expected_time = 8
    assert timeService.day == expected_day
    assert timeService.time == expected_time
    assert timeService.player.moneyInBank == 110
    assert timeService.stats.moneyMadeFromInterest == 10
    assert timeService.stats.totalMoneyMade == 110