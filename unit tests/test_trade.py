import unittest

from classes.player import Player
from classes.trade import Trade

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.giver = Player("aj", "blue")
        self.receiver = Player("bob", "red")
        self.giver.resources = {"wood": 5, "ore": 4, "wheat": 2}
        self.receiver.resources = {"wood": 1, "ore": 2, "wheat": 6}
        self.trade = Trade(self.giver, self.receiver, {"wood": 3, "ore": 2}, {"wheat": 4})

    def test_execute_successful(self):
        # ensure resources are initially owned correctly
        self.assertEqual(self.giver.resources, {"wood": 5, "ore": 4, "wheat": 2})
        self.assertEqual(self.receiver.resources, {"wood": 1, "ore": 2, "wheat": 6})

        # execute the trade
        self.assertTrue(self.trade.execute())

        # ensure resources are transferred correctly
        self.assertEqual(self.giver.resources, {"wood": 2, "ore": 2, "wheat": 6})
        self.assertEqual(self.receiver.resources, {"wood": 4, "ore": 4, "wheat": 2})

    def test_execute_unsuccessful(self):
        # try to execute a trade where aj doesn't have enough wood
        trade = Trade(self.giver, self.receiver, {"wood": 6, "ore": 2}, {"wheat": 4})
        self.assertFalse(trade.execute())

        # ensure no resources were transferred
        self.assertEqual(self.giver.resources, {"wood": 5, "ore": 4, "wheat": 2})
        self.assertEqual(self.receiver.resources, {"wood": 1, "ore": 2, "wheat": 6})
