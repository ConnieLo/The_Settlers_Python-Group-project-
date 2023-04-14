import unittest

from classes.board import Board
from classes.player import Player


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertEqual(len(self.board.tiles), 19)
        self.assertIsNotNone(self.board.grid)
        self.assertEqual(len(self.board.settlements), 0)

    def test_generate_tiles(self):
        tiles = self.board.generate_tiles()
        self.assertEqual(len(tiles), 19)
        desert_count = sum(1 for num, res in tiles if res == "desert")
        self.assertEqual(desert_count, 1)

    def test_new_settlement(self):
        owner = Player("test", "red")
        settlement_info = [(5, "wood")]
        self.board.new_settlement(owner, settlement_info)
        self.assertEqual(len(self.board.settlements), 1)

