import pygame

from classes.turn import Turn
from classes.player import Player
from classes.board import Board
from classes.settlement import Settlement
from typing import List

# TESTING INFO
# next_turn() should create and activate a new instance of the turn class. The active player of this turn should
# cycle through the 4 different players in the turn queue
# new_settlement() should instance a new settlement belonging to whichever player is the active player on the
# current turn. this settlement should be added to the board


PLAYER_COLOURS = [
    (255, 0, 0),  # RED
    (50, 100, 255),  # BLUE
    (50, 255, 50),  # GREEN
    (255, 220, 0)  # YELLOW
]

class GameMaster:
    def __init__(self):
        self.turn_queue: List[Turn] = [
            Player("player {}".format(i), PLAYER_COLOURS[i]) for i in range(4)
        ]
        self.current_turn: int = -1 #initialised as -1 so that first turn instance will advance it to player 0
        self.turn_inst = None
        self.next_turn()
        self.board = Board()
        self.saved_tuples = []
        self.tuple_count = {}
        self.last_checked_tuple = None
        self.initialised = False    #does nothing yet, going to use this for the start of the game when each player must place 2 settlements and roads

    def next_turn(self) -> Turn:
        self.current_turn += 1
        player = self.turn_queue[self.current_turn % 4]
        print("next turn")
        self.turn_inst = Turn(self, player, self.current_turn)

    def check_three_same_tuples(self, positions: list) -> bool:
        for position in positions:
            if position != self.last_checked_tuple:
                self.saved_tuples.append(position)
                self.last_checked_tuple = position
                if position in self.tuple_count:
                    self.tuple_count[position] += 1
                else:
                    self.tuple_count[position] = 1
                if self.tuple_count[position] == 3:
                    return True
        return False

    def new_settlement(self, owner: Player, settlement_type: str, position: tuple) -> Settlement:
        active_player = self.turn_queue[self.current_turn % 4]
        if self.check_three_same_tuples(position):
            owner.increment_victory_points()
            owner.increment_number_of_settlements()
            self.board.new_settlement(owner, settlement_type)
        return True
    
    def new_road(self, owner, position):
        return self.board.new_road(owner, position)

    def pass_resources(self, roll: int) -> None:
        for s in self.board.get_settlements():
            s.grant_resources(roll)


# UI to display the number of turns so far and the current player's turn
pygame.font.init()
font = pygame.font.Font(None, 36)
# A helper method used in draw method
def draw_text(screen, text, x, y, color=(255, 255, 255), font=None):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw(game_master: GameMaster, screen):
    # Get the current player
    current_player = game_master.turn_queue[game_master.current_turn % 4]
    # Display the current player's turn
    draw_text(screen, f"Number of turns: {game_master.current_turn}", 10, 150, font=font)
    draw_text(screen, f"Current Player: {current_player.name}", 10, 200, font=font)
    # Update the screen
