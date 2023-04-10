from classes.turn import Turn
from classes.player import Player
from classes.board import Board

PLAYER_COLOURS = [
    (50, 255, 50),  # GREEN
    (50, 100, 255),  # BLUE
    (255, 75, 50),  # RED
    (255, 220, 0)  # YELLOW
]

class GameMaster:
    turn_queue: list[Turn]
    current_turn: Turn

    def __init__(self, ):
        # Instancing an array of 4 players with unique names and colours
        self.turn_queue = [
            Player("player {}".format(i), PLAYER_COLOURS[i]) for i in range(4)
        ]
        self.current_turn = 0
        self.board = Board()

    # Generates and starts the next turn
    def next_turn(self):
        player = self.turn_queue[self.current_turn % 4]
        turn = Turn(self, player, self.current_turn)
        turn.take_turn()

    # AT the start of each turn, goes through every settlement and assigns the relevant resorces to the player
    def pass_resources(self, roll):
        for s in self.board.get_settlements():
            s.grant_resources(roll)