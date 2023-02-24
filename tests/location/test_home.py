from src.location.enum.locationType import LocationType
from src.location import home
from src.player.player import Player
from src.stats.stats import Stats
from src.template.textAdventureTemplate import TextAdventureTemplate
from src.world.timeService import TimeService
from unittest.mock import MagicMock

def createHome():
    template = TextAdventureTemplate()
    currentPrompt = "What would you like to do?"
    player = Player()
    stats = Stats()
    timeService = TimeService(player, stats)
    return home.Home(template, currentPrompt, player, stats, timeService)

def test_initialization():
    # call
    home = createHome()
    
    # check
    assert home.template != None
    assert home.currentPrompt != None
    assert home.player != None
    assert home.stats != None
    assert home.timeService != None

def test_run_sleep_action():
    # prepare
    homeInstance = createHome()
    homeInstance.template.showOptions = MagicMock(return_value = "1")
    homeInstance.sleep = MagicMock()
    
    # call
    nextLocation = homeInstance.run("What would you like to do?")
    
    # check
    homeInstance.sleep.assert_called_once()
    assert nextLocation == LocationType.HOME

def test_run_see_stats_action():
    # prepare
    homeInstance = createHome()
    homeInstance.template.showOptions = MagicMock(return_value = "2")
    homeInstance.displayStats = MagicMock()
    
    # call
    nextLocation = homeInstance.run("What would you like to do?")
    
    # check
    homeInstance.displayStats.assert_called_once()
    assert nextLocation == LocationType.HOME
    
def test_run_go_to_docks_action():
    # prepare
    homeInstance = createHome()
    homeInstance.template.showOptions = MagicMock(return_value = "3")
    
    # call
    nextLocation = homeInstance.run("What would you like to do?")
    
    # check
    assert nextLocation == LocationType.DOCKS

def test_run_quit_action():
    # prepare
    homeInstance = createHome()
    homeInstance.template.showOptions = MagicMock(return_value = "4")
    
    # call
    nextLocation = homeInstance.run("What would you like to do?")
    
    # check
    assert nextLocation == LocationType.NONE
    
def test_sleep():
    # prepare
    homeInstance = createHome()
    homeInstance.timeService.increaseDay = MagicMock()
    
    # call
    homeInstance.sleep()
    
    # check
    homeInstance.timeService.increaseDay.assert_called_once()
    assert homeInstance.currentPrompt == "You sleep until the next morning."

def test_displayStats():
    # prepare
    homeInstance = createHome()
    homeInstance.template.lotsOfSpace = MagicMock()
    home.print = MagicMock()
    home.input = MagicMock()
    
    # call
    homeInstance.displayStats()
    
    # check
    assert homeInstance.template.lotsOfSpace.call_count == 2
    assert home.print.call_count == 6
    assert home.input.call_count == 1