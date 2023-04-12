from classes.player import Player
from random import randint

# TESTING INFO
# take_turn() this is basicly 'the big red button that says go'. Once this function is called it should signal the
# player to do whatever (build settlements/roads, buy cards etc.) and should not return until that player has
# signled they are done (clicked next turn, for the user)
# new_settlement() should prompt the master to create a new settlement.  The settlement should belong
# to whichever player is on their turn according to the game master - this isn't guaranteed to be THIS turn's
# player, but as this function should never be called unless this turn is active, it shouldn't matter


class Turn:
    def __init__(self, master, which_player, turn_no):
        self.master = master
        self.turn_no = turn_no
        self.active_player = which_player
        self.roll = [randint(1, 6), randint(1, 6)]
        print("New roll: " + str(self.roll))

    def take_turn(self):
        # Hand out resources among players
        self.master.pass_resources(sum(self.roll))

        # Prompt the player to do any trades, we shouldn't need to save the return value of this function
        self.active_player.prompt_trade()

        # Prompt the player to purchase/build new items. Pass any new roads or settlments to the game master
        new_builds = self.active_player.prompt_builds()

    def new_settlement(self, settlement_info):
        self.master.new_settlement(settlement_info)


