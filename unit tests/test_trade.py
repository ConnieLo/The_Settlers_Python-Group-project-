import unittest

from classes.player import Player
from classes.trade import Trade

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.giver = Player("aj", "blue")
        self.receiver = Player("bob", "red")
        self.giver.resources.update({"wood": 1, "ore": 1, "wheat": 1})
        self.receiver.resources.update({"sheep": 1})
        self.trade = Trade(self.giver, self.receiver, {"wood": 1, "ore": 1}, {"sheep": 1})

    def test_execute_successful(self):
        # execute the trade
        self.assertTrue(self.trade.execute())

        # ensure resources are transferred correctly
        # self.assertEqual(self.giver.resources, {"wood": 0, "ore": 0, "wheat": 1})
        # self.assertEqual(self.receiver.resources, {"wood": 1, "ore": 1, "sheep": 0})
        giver_res = self.giver.resources
        rec_res = self.receiver.resources

        self.assertEqual(0, giver_res["wood"])
        self.assertEqual(0, giver_res["ore"])
        self.assertEqual(1, giver_res["wheat"])
        self.assertEqual(1, rec_res["wood"])
        self.assertEqual(1, rec_res["ore"])
        self.assertEqual(0, rec_res["sheep"])

    def test_execute_unsuccessful(self):
        impossible_trades = [
            Trade(self.giver, self.receiver, {"wood": 2, "ore": 2}, {"sheep": 1}),  # G can't afford
            Trade(self.giver, self.receiver, {"wood": 1, "ore": 1}, {"sheep": 2}),  # R can't afford
            Trade(self.giver, self.receiver, {"wood": 2, "ore": 2}, {"sheep": 2}),  # Neither can afford
            Trade(self.giver, self.receiver, {"wood": 1, "ore": 1, "pineapples": 1}, {"sheep": 1}) # Resources that don't exist
        ]
        for t in impossible_trades:
            # Save the initial resources
            giver_res = self.giver.resources
            rec_res = self.receiver.resources

            # try to execute an impossible trade
            self.trade = t
            self.assertFalse(self.trade.execute())

            # ensure no resources were transferred
            self.assertEqual(giver_res, self.giver.resources)
            self.assertEqual(rec_res, self.receiver.resources)
