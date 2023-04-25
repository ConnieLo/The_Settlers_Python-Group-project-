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
        for r in ("wood", "sheep", "wheat", "clay", "ore"):
            # Give each player one of that resource
            for p in self.players:
                p.resources[r] = 1

            # Play the card
            dev_card_manager.monopoly(self.card_player, r)

            # Check the card player has gained the resource
            self.assertEqual(self.card_player.resources[r], 4)

            # check the other players have lost that resource
            for p in self.players[1:]:
                self.assertEqual(p.resources[r], 0)

    def test_yop(self):
        for r in ("wood", "sheep", "wheat", "clay", "ore"):
            # Play the card
            dev_card_manager.year_of_plenty(self.card_player, r)
            self.assertEqual(self.card_player.resources[r], 2)
