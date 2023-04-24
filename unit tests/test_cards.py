from unittest import TestCase
from classes import game_master, player, dev_card_manager
import unittest


class TestCards(unittest.TestCase):
    def setUp(self):
        self.master = game_master.GameMaster()
        self.players = self.master.turn_queue
        self.card_player = self.players[0]
        dev_card_manager.init(self.master)

    def test_monopoly(self):
        # Give each player wood (grow up)
        for player in self.players:
            player.resources["wood"] += 1

        # Play the card
        dev_card_manager.play_card(self.card_player, "Monopoly")

        self.assertEqual(self.card_player.resources["wood"], 4)
