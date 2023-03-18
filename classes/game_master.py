import classes.board as board
import classes.turn as turn


class GameMaster:
    turn_queue: list[turn.Turn]
    current_turn: turn.Turn

    def __init__(self):
        self.turn_queue = []
