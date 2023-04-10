from classes.player import Player
from random import randint


class Turn:
    def __init__(self, master, which_player, turn_no):
        self.master = master
        self.turn_no = turn_no
        self.active_player = which_player
        self.roll = [randint(1, 6), randint(1, 6)]

    def take_turn(self):
        # Hand out resources among players
        self.master.pass_resources(sum(self.roll))

        # Prompt the player to do any trades, we shouldn't need to save the return value of this function
        self.active_player.prompt_trade()

        # Prompt the player to purchase/build new items. Pass any new roads or settlments to the game master
        new_builds = self.active_player.prompt_builds()
        self.master.update_board(new_builds)

    def new_settlement(self, settlement_info):
        self.master.new_settlement(settlement_info)


