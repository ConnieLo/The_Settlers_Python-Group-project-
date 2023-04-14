import unittest

from classes.board import Board
from classes.player import Player


#########################################
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

        # Test the distribution of resources according to the rules of Catan
        resource_counts = {res: 0 for res in ["sheep", "wheat", "wood", "ore", "clay"]}
        for _, res in tiles:
            if res != "desert":
                resource_counts[res] += 1
        for count in resource_counts.values():
            self.assertEqual(count, 4)

    def test_new_settlement(self):
        owner = Player("test", "red")
        settlement_info = [(5, "wood")]
        self.board.new_settlement(owner, settlement_info)
        self.assertEqual(len(self.board.settlements), 1)
        settlement = self.board.settlements[0]
        self.assertEqual(settlement.owner, owner)
        self.assertEqual(settlement.tiles, settlement_info)

    def test_get_settlements(self):
        owner = Player("test", "red")
        settlement_info = [(5, "wood")]
        self.board.new_settlement(owner, settlement_info)
        settlements = self.board.get_settlements()
        self.assertEqual(len(settlements), 1)

    def test_get_tile_info(self):
        tile_info = self.board.get_tile_info(0)
        self.assertIsNotNone(tile_info)

# if __name__ == '__main__':
#     unittest.main()


# from unittest import TestCase
#
#
# class TestBoard(TestCase):
#     def test_generate_tiles(self):
#         self.fail()
#
#     def test_new_settlement(self):
#         self.fail()
#
#     def test_get_settlements(self):
#         self.fail()
#
#     def test_get_tile_info(self):
#         self.fail()
#
#     def test_draw_board(self):
#         self.fail()


# #############before#####################
#
# class TestBoard(unittest.TestCase):
#
#     def setUp(self):
#         self.board = Board()
#
#     def test_initialization(self):
#         self.assertEqual(len(self.board.tiles), 19)
#         self.assertIsNotNone(self.board.grid)
#         self.assertEqual(len(self.board.settlements), 0)
#
#     def test_generate_tiles(self):
#         tiles = self.board.generate_tiles()
#         self.assertEqual(len(tiles), 19)
#         desert_count = sum(1 for num, res in tiles if res == "desert")
#         self.assertEqual(desert_count, 1)
#
#     def test_new_settlement(self):
#         owner = Player("test", "red")
#         settlement_info = [(5, "wood")]
#         self.board.new_settlement(owner, settlement_info)
#         self.assertEqual(len(self.board.settlements), 1)
#
#     def test_get_settlements(self):
#         owner = Player("test", "red")
#         settlement_info = [(5, "wood")]
#         self.board.new_settlement(owner, settlement_info)
#         settlements = self.board.get_settlements()
#         self.assertEqual(len(settlements), 1)
#
#     def test_get_tile_info(self):
#         tile_info = self.board.get_tile_info(0)
#         self.assertIsNotNone(tile_info)
