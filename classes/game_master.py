from classes import *


class GameMaster:
    turn_queue: list[Turn]
    current_turn: Turn

    def __init__(self):
        self.turn_queue = []

    # AT the start of each turn, goes through every settlement and assigns the relevant resorces to the player
    def pass_resources(self, roll):
        for s in board.get_settlments():
            s.grant_resources(roll)