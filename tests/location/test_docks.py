from src.location.enum.locationType import LocationType
from src.location import docks
from src.player.player import Player
from src.stats.stats import Stats
from src.template.textAdventureTemplate import TextAdventureTemplate
from src.world.timeService import TimeService
from unittest.mock import MagicMock

def createDocks():
    template = TextAdventureTemplate()
    currentPrompt = "What would you like to do?"
    player = Player()
    stats = Stats()
    timeService = TimeService(player, stats)
    return docks.Docks(template, currentPrompt, player, stats, timeService)

def test_initialization():
    # call
    docksInstance = createDocks()
    
    # check
    assert docksInstance.template != None
    assert docksInstance.currentPrompt != None
    assert docksInstance.player != None
    assert docksInstance.stats != None
    assert docksInstance.timeService != None

def test_run_fish_action():
    # prepare
    docksInstance = createDocks()
    docksInstance.template.showOptions = MagicMock(return_value = "1")
    docksInstance.fish = MagicMock()
    
    # call
    nextLocation = docksInstance.run("What would you like to do?")
    
    # check
    docksInstance.fish.assert_called_once()
    assert nextLocation == LocationType.DOCKS

def test_run_go_home_action():
    # prepare
    docksInstance = createDocks()
    docksInstance.template.showOptions = MagicMock(return_value = "2")
    
    # call
    nextLocation = docksInstance.run("What would you like to do?")
    
    # check
    assert nextLocation == LocationType.HOME

def test_run_go_to_shop_action():
    # prepare
    docksInstance = createDocks()
    docksInstance.template.showOptions = MagicMock(return_value = "3")
    
    # call
    nextLocation = docksInstance.run("What would you like to do?")
    
    # check
    assert nextLocation == LocationType.SHOP

def test_run_go_to_tavern_action():
    # prepare
    docksInstance = createDocks()
    docksInstance.template.showOptions = MagicMock(return_value = "4")
    
    # call
    nextLocation = docksInstance.run("What would you like to do?")
    
    # check
    assert nextLocation == LocationType.TAVERN

def test_run_go_to_bank_action():
    # prepare
    docksInstance = createDocks()
    docksInstance.template.showOptions = MagicMock(return_value = "5")
    
    # call
    nextLocation = docksInstance.run("What would you like to do?")
    
    # check
    assert nextLocation == LocationType.BANK

def test_fish():
    # prepare
    docksInstance = createDocks()
    docksInstance.template.lotsOfSpace = MagicMock()
    docksInstance.template.divider = MagicMock()
    docks.print = MagicMock()
    docks.sys.stdout.flush = MagicMock()
    docks.time.sleep = MagicMock()
    docks.random.randint = MagicMock(return_value = 3)
    docksInstance.timeService.increaseTime = MagicMock()
    
    # call
    docksInstance.fish()
    
    # check
    docksInstance.template.lotsOfSpace.assert_called_once()
    docksInstance.template.divider.assert_called_once()
    assert docks.print.call_count == 4
    assert docks.sys.stdout.flush.call_count == 4
    assert docks.time.sleep.call_count == 4
    assert docksInstance.player.fishCount == 3
    assert docksInstance.stats.totalFishCaught == 3