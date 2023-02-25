from src.player.player import Player


def createPlayer():
    return Player()


def test_initialization():
    # call
    player = createPlayer()

    # check
    assert player.fishCount == 0
    assert player.money == 0
    assert player.moneyInBank == 0
    assert player.fishMultiplier == 1
