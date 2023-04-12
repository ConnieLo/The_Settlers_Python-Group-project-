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
        self.current_turn: int = 0
        self.board = Board()

    def next_turn(self) -> Turn:
        player = self.turn_queue[self.current_turn % 4]
        turn = Turn(self, player, self.current_turn)
        turn.take_turn()
        self.current_turn += 1
        return turn

    def new_settlement(self, owner: Player, settlement_type: str, position: tuple) -> Settlement:
        active_player = self.turn_queue[self.current_turn % 4]
        return self.board.new_settlement(owner, settlement_type, position)

    def pass_resources(self, roll: int) -> None:
        for s in self.board.get_settlements():
            s.grant_resources(roll)


""" DO NOT TOUCH PLS - IN PROGRESS - UI
# Define the font
font = pygame.font.Font(None, 36)
    # A helper method used in draw()
    def draw_text(screen, text, x, y, color=(255, 255, 255), font=None):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)


    # Displays the current player's turn.
    def draw(game_master: GameMaster, screen):
        # Clear the screen
        screen.fill((0, 0, 0))

        # Get the current player
        current_player = game_master.turn_queue[game_master.current_turn % 4]

        # Display the current player's turn
        draw_text(f"Current Turn: {game_master.current_turn}", 10, 10)
        draw_text(f"Current Player: {current_player.name} ({current_player.color})", 10, 50)

        # Update the screen
        pygame.display.flip()
"""