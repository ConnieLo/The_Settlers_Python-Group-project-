import pygame

from classes.turn import Turn
from classes.player import Player
from classes.board import Board


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
        return turn

    def new_settlement(self, owner, settlement_info, position):
        active_player = self.turn_queue[self.current_turn % 4]

        return self.board.new_settlement(owner, settlement_info, position)

    # AT the start of each turn, goes through every settlement and assigns the relevant resorces to the player
    def pass_resources(self, roll):
        for s in self.board.get_settlements():
            s.grant_resources(roll)

    # def display_bank(self, surface, x, y, icon_images, resource_images):              #  by aj here i was trying to add a bank in UI
    #     bank_info = [
    #         {"text": f"Resources", "icon": None},
    #         {"text": f"Brick: {self.bank['brick']}", "icon": "brick"},
    #         {"text": f"Ore: {self.bank['ore']}", "icon": "ore"},
    #         {"text": f"Wheat: {self.bank['wheat']}", "icon": "wheat"},
    #         {"text": f"Wood: {self.bank['wood']}", "icon": "wood"},
    #         {"text": f"Sheep: {self.bank['sheep']}", "icon": "sheep"},
    #         {"text": f"Development Cards", "icon": None},
    #         {"text": f"Knight: {self.bank['knight']}", "icon": "knight"},
    #         {"text": f"Victory Point: {self.bank['victory_point']}", "icon": "victory_point"},
    #         {"text": f"Road Building: {self.bank['road_building']}", "icon": "road_building"},
    #         {"text": f"Monopoly: {self.bank['monopoly']}", "icon": "monopoly"},
    #         {"text": f"Year of Plenty: {self.bank['year_of_plenty']}", "icon": "year_of_plenty"},
    #     ]
    #
    #     font = pygame.font.Font(None, 24)
    #     icon_y_offset = 0
    #
    #     for item in bank_info:
    #         if item["icon"]:
    #             icon = resource_images[item["icon"]]
    #             surface.blit(icon, (x, y + icon_y_offset))
    #
    #         text = font.render(item["text"], True, (255, 255, 255))
    #         text_width, text_height = text.get_size()
    #         text_x_offset = (icon.get_width() if item["icon"] else 0) + 5
    #
    #         surface.blit(text, (x + text_x_offset, y + icon_y_offset))
    #
    #         if item["icon"]:
    #             icon_y_offset += max(icon.get_height(), text_height) + 5
    #         else:
    #             icon_y_offset += text_height + 5


        # for the bank

    def display_bank_image(self, surface, x, y, bank):
        surface.blit(bank, (x, y))