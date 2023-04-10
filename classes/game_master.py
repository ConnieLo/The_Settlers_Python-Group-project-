from classes.turn import Turn
from classes.player import Player
from classes.board import Board

PLAYER_COLOURS = [
    (255, 0, 0),  # RED
    (50, 100, 255),  # BLUE
    (50, 255, 50),  # GREEN
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

    def new_settlement(self, settlement_info):
        active_player = self.turn_queue[self.current_turn % 4]
        self.board.new_settlement(active_player, settlement_info)

    # AT the start of each turn, goes through every settlement and assigns the relevant resorces to the player
    def pass_resources(self, roll):
        for s in self.board.get_settlements():
            s.grant_resources(roll)