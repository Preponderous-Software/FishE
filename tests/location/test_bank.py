from src.location.enum.locationType import LocationType
from src.location import bank
from src.player.player import Player
from src.stats.stats import Stats
from src.template.textAdventureTemplate import TextAdventureTemplate
from src.world.timeService import TimeService
from unittest.mock import MagicMock

def createBank():
    template = TextAdventureTemplate()
    currentPrompt = "What would you like to do?"
    player = Player()
    stats = Stats()
    timeService = TimeService(player, stats)
    return bank.Bank(template, currentPrompt, player, stats, timeService)

def test_initialization():
    # call
    bankInstance = createBank()
    
    # check
    assert bankInstance.template != None
    assert bankInstance.currentPrompt != None
    assert bankInstance.player != None
    assert bankInstance.stats != None
    assert bankInstance.timeService != None

def test_run_make_deposit_success():
    # prepare
    bankInstance = createBank()
    bankInstance.template.showOptions = MagicMock(return_value="1")
    bankInstance.player.money = 100
    bankInstance.deposit = MagicMock()
    
    # call
    nextLocation = bankInstance.run("What would you like to do?")
    
    # check
    bankInstance.deposit.assert_called_once()
    assert nextLocation == LocationType.BANK

def test_run_make_deposit_failure_no_money():
    # prepare
    bankInstance = createBank()
    bankInstance.template.showOptions = MagicMock(return_value="1")
    bankInstance.deposit = MagicMock()
    
    # call
    nextLocation = bankInstance.run("What would you like to do?")
    
    # check
    bankInstance.deposit.assert_not_called()
    assert nextLocation == LocationType.BANK

def test_run_make_withdrawal_success():
    # prepare
    bankInstance = createBank()
    bankInstance.template.showOptions = MagicMock(return_value="2")
    bankInstance.player.moneyInBank = 100
    bankInstance.withdraw = MagicMock()
    
    # call
    nextLocation = bankInstance.run("What would you like to do?")
    
    # check
    bankInstance.withdraw.assert_called_once()
    assert nextLocation == LocationType.BANK

def test_run_make_withdrawal_failure_no_money():
    # prepare
    bankInstance = createBank()
    bankInstance.template.showOptions = MagicMock(return_value="2")
    bankInstance.withdraw = MagicMock()
    
    # call
    nextLocation = bankInstance.run("What would you like to do?")
    
    # check
    bankInstance.withdraw.assert_not_called()
    assert nextLocation == LocationType.BANK

def test_run_go_to_docks_action():
    # prepare
    bankInstance = createBank()
    bankInstance.template.showOptions = MagicMock(return_value="3")
    
    # call
    nextLocation = bankInstance.run("What would you like to do?")
    
    # check
    assert nextLocation == LocationType.DOCKS
    
def test_deposit_success():
    # prepare
    bankInstance = createBank()
    bankInstance.template.lotsOfSpace = MagicMock()
    bankInstance.template.divider = MagicMock()
    bankInstance.player.money = 100
    bank.print = MagicMock()
    bank.input = MagicMock(return_value="10")
    
    # call
    bankInstance.deposit("How much?")
    
    # check
    bank.print.assert_called_once()
    assert bankInstance.player.moneyInBank == 10
    assert bankInstance.player.money == 90

def test_deposit_failure_not_enough_money():
    # prepare
    bankInstance = createBank()
    bankInstance.template.lotsOfSpace = MagicMock()
    bankInstance.template.divider = MagicMock()
    bankInstance.player.money = 5
    bank.print = MagicMock()
    bank.input = MagicMock(return_value="10")
    
    # call
    bankInstance.deposit("How much?")
    
    # check
    bank.print.assert_called_once()
    assert bankInstance.player.moneyInBank == 0
    assert bankInstance.player.money == 5

def test_withdraw_success():
    # prepare
    bankInstance = createBank()
    bankInstance.template.lotsOfSpace = MagicMock()
    bankInstance.template.divider = MagicMock()
    bankInstance.player.moneyInBank = 100
    bank.print = MagicMock()
    bank.input = MagicMock(return_value="10")
    
    # call
    bankInstance.withdraw("How much?")
    
    # check
    bank.print.assert_called_once()
    assert bankInstance.player.moneyInBank == 90
    assert bankInstance.player.money == 10

def test_withdraw_failure_not_enough_money():
    # prepare
    bankInstance = createBank()
    bankInstance.template.lotsOfSpace = MagicMock()
    bankInstance.template.divider = MagicMock()
    bankInstance.player.moneyInBank = 5
    bank.print = MagicMock()
    bank.input = MagicMock(return_value="10")
    
    # call
    bankInstance.withdraw("How much?")
    
    # check
    bank.print.assert_called_once()
    assert bankInstance.player.moneyInBank == 5
    assert bankInstance.player.money == 0