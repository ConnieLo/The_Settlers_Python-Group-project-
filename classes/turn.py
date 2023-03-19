import classes.player as player
import classes.game_master as gm
from random import randint


class Turn:
    active_player: player.Player
    master: gm.GameMaster

    def __init__(self, master, which_player, turn_no):
        self.master = master
        self.turn_no = turn_no
        self.active_player = which_player
        self.roll = [randint(1, 6), randint(1, 6)]

    def prod_resources(self):
        roll_total = sum(self.roll)
